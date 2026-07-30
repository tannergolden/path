#!/usr/bin/env python3
"""Validate this repository's own configuration.

WHY THIS EXISTS. The `ci` job in `checks.yml` fails when lint, test and
build all resolve to
nothing, because a check that checked nothing must not report green. A
scaffold with no source code in it yet would trip that on its first run -
but "no source code" is not the same as "nothing to validate". Every file
that decides how this repository behaves is here from the start, and a typo
in any of them breaks something quietly.

So this is the placeholder that is not a placeholder. It runs as the
`lint-command` until you point that at your project's real linter, and what
it checks stays true afterwards.

WHAT IT DOES NOT DO. It never looks at source code, and it knows nothing
about any language. Link checking and spelling are separate jobs in the
called workflow already; workflow semantics and security are the `lint` job.
This
covers the gap between them: the configuration files nothing else parses.

Exits non-zero on the first category with findings, listing all of them.
Annotations are emitted in GitHub's format when running under Actions, so
findings land on the file and line in the diff.
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
IN_ACTIONS = os.environ.get('GITHUB_ACTIONS') == 'true'

# Anything git ignores is not ours to judge, and anything binary cannot be
# read as text. Both are excluded by asking git what it tracks.
BINARY_SUFFIXES = {
    '.png', '.jpg', '.jpeg', '.gif', '.webp', '.ico', '.pdf',
    '.woff', '.woff2', '.ttf', '.otf', '.zip', '.gz', '.mp4',
}

problems: list[str] = []


def report(path: pathlib.Path, line: int | None, message: str) -> None:
    rel = path.relative_to(ROOT).as_posix()
    where = f'{rel}:{line}' if line else rel
    problems.append(f'{where}: {message}')
    if IN_ACTIONS:
        pos = f',line={line}' if line else ''
        print(f'::error file={rel}{pos}::{message}')


def tracked_files() -> list[pathlib.Path]:
    out = subprocess.run(
        ['git', 'ls-files', '-z'],
        cwd=ROOT, check=True, capture_output=True, text=True,
    ).stdout
    return [ROOT / p for p in out.split('\0') if p]


def is_text(path: pathlib.Path) -> bool:
    return path.suffix.lower() not in BINARY_SUFFIXES


def read(path: pathlib.Path) -> str | None:
    """Read as UTF-8, reporting rather than raising when it is not."""
    raw = path.read_bytes()
    try:
        return raw.decode('utf-8')
    except UnicodeDecodeError as exc:
        report(path, None, f'not valid UTF-8: {exc}')
        return None


# VS Code and dev containers read JSONC - JSON that allows comments and a
# trailing comma. Their files are genuinely valid; a strict parser is the one
# that is wrong. Comments are blanked rather than deleted so that a reported
# line number still points at the right line.
JSONC_DIRS = {'.vscode', '.devcontainer'}


def strip_jsonc(text: str) -> str:
    out: list[str] = []
    i, n = 0, len(text)
    in_string = escaped = False
    while i < n:
        ch = text[i]
        if in_string:
            out.append(ch)
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == '"':
                in_string = False
            i += 1
        elif ch == '"':
            in_string = True
            out.append(ch)
            i += 1
        elif text.startswith('//', i):
            while i < n and text[i] != '\n':
                out.append(' ')
                i += 1
        elif text.startswith('/*', i):
            while i < n and not text.startswith('*/', i):
                out.append('\n' if text[i] == '\n' else ' ')
                i += 1
            out.append('  ')
            i += 2
        else:
            out.append(ch)
            i += 1
    # Trailing commas, once comments can no longer hide one.
    return re.sub(r',(\s*[}\]])', r' \1', ''.join(out))


def check_json(path: pathlib.Path, text: str) -> None:
    jsonc = path.parent.name in JSONC_DIRS
    try:
        json.loads(strip_jsonc(text) if jsonc else text)
    except json.JSONDecodeError as exc:
        kind = 'JSONC' if jsonc else 'JSON'
        report(path, exc.lineno, f'invalid {kind}: {exc.msg}')


def check_yaml(path: pathlib.Path, text: str) -> None:
    import yaml  # runner-provided; see the guard in main()

    try:
        # Every document, because an issue form or a multi-document config
        # can be valid up to a separator and broken after it.
        list(yaml.safe_load_all(text))
    except yaml.YAMLError as exc:
        mark = getattr(exc, 'problem_mark', None)
        line = mark.line + 1 if mark else None
        detail = getattr(exc, 'problem', None) or str(exc).splitlines()[0]
        report(path, line, f'invalid YAML: {detail}')


# A ref that is a branch moves under you; a bare `uses:` has no ref at all.
# Neither is acceptable in a workflow that runs with this repository's token.
#
# `re.I` because a commit SHA is hex either way, and the `$` anchor means the
# quotes have to come off first - see `unquote` below.
UNPINNED = re.compile(r'^\s*(?:-\s*)?uses:\s*([^\s#]+)\s*(?:#.*)?$')
PINNED_REF = re.compile(r'@(?:[0-9a-f]{40}|v\d+(?:\.\d+){0,2})$', re.I)


def unquote(ref: str) -> str:
    """Strip the YAML quoting the pattern captured but the ref does not have.

    `uses: 'actions/checkout@v4'` is valid YAML, correctly pinned, and the
    dominant scalar style in these workflows. Matched raw against a `$`-anchored
    pattern, the trailing quote meant nothing ever looked pinned, and a properly
    pinned action was reported as "pinned to a branch" - a message that is not
    merely unhelpful but the opposite of true.
    """
    for quote in ("'", '"'):
        if len(ref) >= 2 and ref.startswith(quote) and ref.endswith(quote):
            return ref[1:-1]
    return ref


def check_pins(path: pathlib.Path, text: str) -> None:
    for number, line in enumerate(text.splitlines(), start=1):
        match = UNPINNED.match(line)
        if not match:
            continue
        ref = unquote(match.group(1))
        if ref.startswith('./') or ref.startswith('docker://'):
            continue
        if '@' not in ref:
            report(path, number, f'`{ref}` has no ref: pin it to a tag or a commit')
        elif not PINNED_REF.search(ref):
            report(path, number, f'`{ref}` is pinned to a branch: use a tag or a commit')


# The two exemptions this repository's OWN configuration requires.
#
# .gitattributes forces `eol=crlf` on Windows scripts, so git checks them out
# with CRLF on the runner. Failing them demanded a file that cannot exist:
# satisfying the linter violated .gitattributes, and satisfying .gitattributes
# reddened the required `ci` check, with no way to have both.
CRLF_SUFFIXES = {'.bat', '.cmd', '.ps1'}

# .editorconfig sets `[*.md] trim_trailing_whitespace = false`, because two
# trailing spaces are Markdown's hard line break. There they are syntax, not
# noise - and every seeded document is Markdown.
TRAILING_WS_EXEMPT_SUFFIXES = {'.md', '.markdown'}


def check_whitespace(path: pathlib.Path, text: str) -> None:
    """The parts of .editorconfig a parser cannot enforce on its own."""
    suffix = path.suffix.lower()
    if '\r\n' in text and suffix not in CRLF_SUFFIXES:
        report(path, None, 'CRLF line endings; this repository is LF only')
    if text and not text.endswith('\n'):
        report(path, len(text.splitlines()), 'no newline at end of file')
    if suffix in TRAILING_WS_EXEMPT_SUFFIXES:
        return
    for number, line in enumerate(text.splitlines(), start=1):
        if line != line.rstrip():
            report(path, number, 'trailing whitespace')


def main() -> int:
    try:
        import yaml  # noqa: F401
    except ImportError:
        print(
            '::error::PyYAML is not available, so the YAML in this repository '
            'cannot be validated. Install it (pip install pyyaml) or point '
            "`lint-command` at your project's own linter."
        )
        return 1

    files = [p for p in tracked_files() if p.is_file() and is_text(p)]
    if not files:
        print('::error::git reported no tracked files, so nothing was checked.')
        return 1

    for path in files:
        text = read(path)
        if text is None:
            continue
        check_whitespace(path, text)
        suffix = path.suffix.lower()
        if suffix == '.json':
            check_json(path, text)
        elif suffix in ('.yml', '.yaml'):
            check_yaml(path, text)
            if path.parent.name == 'workflows':
                check_pins(path, text)

    counts = {
        'files': len(files),
        'yaml': sum(1 for p in files if p.suffix.lower() in ('.yml', '.yaml')),
        'json': sum(1 for p in files if p.suffix.lower() == '.json'),
    }
    summary = (
        f"{counts['files']} tracked text files checked "
        f"({counts['yaml']} YAML, {counts['json']} JSON)"
    )

    if problems:
        print(f'\n{summary}. {len(problems)} problem(s):\n')
        for problem in problems:
            print(f'  {problem}')
        return 1

    print(f'{summary}. No problems.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
