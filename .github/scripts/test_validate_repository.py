#!/usr/bin/env python3
"""Tests for the repository validator.

WHY THIS EXISTS. `validate-repository.py` runs as the `ci` job's
`lint-command` from the first commit, which makes it the only gate a fresh
repository actually has - and it had no test. It also enforced three rules
this repository contradicts elsewhere, so it failed files that
`.gitattributes` and `.editorconfig` require to look exactly that way.

Every test builds a throwaway repository, runs the real script as a
subprocess exactly as CI does, and asserts on its exit code and output.
Nothing here reads or writes the repository it ships in.

Run it:

    python3 .github/scripts/test_validate_repository.py
"""

from __future__ import annotations

import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent / 'validate-repository.py'


class Repo:
    """A throwaway git repository with the validator installed."""

    def __init__(self) -> None:
        self.root = pathlib.Path(tempfile.mkdtemp(prefix='validate-test-'))
        self.run_git('init', '-q', '.')
        self.write('.github/scripts/validate-repository.py', SCRIPT.read_text(encoding='utf-8'))

    def run_git(self, *args: str) -> None:
        subprocess.run(['git', *args], cwd=self.root, check=True, capture_output=True)

    def write(self, rel: str, text: str, newline: str = '\n') -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.replace('\n', newline).encode('utf-8'))

    def run(self) -> subprocess.CompletedProcess[str]:
        self.run_git('add', '-A')
        return subprocess.run(
            [sys.executable, '.github/scripts/validate-repository.py'],
            cwd=self.root, capture_output=True, text=True,
        )

    def cleanup(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)


class ValidatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = Repo()
        self.addCleanup(self.repo.cleanup)

    def assertClean(self, result: subprocess.CompletedProcess[str]) -> None:
        self.assertEqual(
            result.returncode, 0,
            f'expected a clean run, got exit {result.returncode}:\n'
            f'{result.stdout}\n{result.stderr}',
        )

    def assertFinding(
        self, result: subprocess.CompletedProcess[str], fragment: str
    ) -> None:
        self.assertEqual(
            result.returncode, 1,
            f'expected a finding, got exit {result.returncode}:\n'
            f'{result.stdout}\n{result.stderr}',
        )
        self.assertIn(fragment, result.stdout)


class TestLineEndings(ValidatorTestCase):
    """LF everywhere, except where .gitattributes forces CRLF."""

    def test_crlf_in_an_ordinary_file_is_reported(self) -> None:
        self.repo.write('notes.txt', 'a\nb\n', newline='\r\n')
        self.assertFinding(self.repo.run(), 'CRLF')

    def test_crlf_is_permitted_where_gitattributes_requires_it(self) -> None:
        # .gitattributes forces `eol=crlf` on these, so git checks them out
        # with CRLF on the runner. Failing them demands a file that cannot
        # exist: satisfying the linter violates .gitattributes, and vice versa.
        #
        # The exemption comes from the declaration, so the fixture has to make
        # it - a hardcoded suffix list would pass this test without the file
        # that gives the rule its authority.
        self.repo.write('.gitattributes', '*.bat text eol=crlf\n'
                                          '*.cmd text eol=crlf\n'
                                          '*.ps1 text eol=crlf\n')
        for name in ('build.bat', 'run.cmd', 'deploy.ps1'):
            self.repo.write(name, 'echo hello\n', newline='\r\n')
        self.assertClean(self.repo.run())

    def test_crlf_is_reported_where_gitattributes_does_not_ask_for_it(self) -> None:
        # The complement, and the reason the exemption is not a suffix list:
        # the same extension is a finding in a repository that never declared
        # it. The rule is what .gitattributes says, not what the name looks
        # like.
        self.repo.write('build.bat', 'echo hello\n', newline='\r\n')
        self.assertFinding(self.repo.run(), 'CRLF')

    def test_an_extension_nobody_anticipated_is_exempt_once_declared(self) -> None:
        self.repo.write('.gitattributes', '*.vbs text eol=crlf\n')
        self.repo.write('legacy.vbs', 'WScript.Echo "hi"\n', newline='\r\n')
        self.assertClean(self.repo.run())

    def test_crlf_is_still_reported_in_a_nested_windows_lookalike(self) -> None:
        self.repo.write('scripts/build.bat.md', 'a\nb\n', newline='\r\n')
        self.assertFinding(self.repo.run(), 'CRLF')

    def test_lf_in_a_windows_script_is_still_fine(self) -> None:
        self.repo.write('build.bat', 'echo hello\n')
        self.assertClean(self.repo.run())


class TestTrailingWhitespace(ValidatorTestCase):
    """Trailing spaces are noise - except in Markdown, where they are syntax."""

    def test_trailing_whitespace_is_reported(self) -> None:
        self.repo.write('config.yml', 'key: value   \n')
        self.assertFinding(self.repo.run(), 'trailing whitespace')

    def test_a_markdown_hard_line_break_is_permitted(self) -> None:
        # Two trailing spaces are Markdown's hard line break, and
        # .editorconfig sets `[*.md] trim_trailing_whitespace = false`
        # precisely so they survive.
        self.repo.write('NOTES.md', 'line one  \nline two\n')
        self.assertClean(self.repo.run())

    def test_markdown_is_still_checked_for_everything_else(self) -> None:
        self.repo.write('NOTES.md', 'no newline at the end')
        self.assertFinding(self.repo.run(), 'no newline at end of file')


class TestActionPins(ValidatorTestCase):
    """Every `uses:` must name a tag or a commit, never a branch."""

    def workflow(self, uses: str) -> str:
        return (
            'name: t\n'
            'on: push\n'
            'jobs:\n'
            '  a:\n'
            '    runs-on: ubuntu-latest\n'
            '    steps:\n'
            f'      - uses: {uses}\n'
        )

    def test_a_branch_ref_is_reported(self) -> None:
        self.repo.write('.github/workflows/t.yml', self.workflow('actions/checkout@main'))
        self.assertFinding(self.repo.run(), 'pinned to a branch')

    def test_a_missing_ref_is_reported(self) -> None:
        self.repo.write('.github/workflows/t.yml', self.workflow('actions/checkout'))
        self.assertFinding(self.repo.run(), 'has no ref')

    def test_a_tag_is_accepted(self) -> None:
        self.repo.write('.github/workflows/t.yml', self.workflow('actions/checkout@v4'))
        self.assertClean(self.repo.run())

    def test_a_quoted_tag_is_accepted(self) -> None:
        # Single-quoted scalars are this repository's dominant YAML style, and
        # the quotes are not part of the ref.
        self.repo.write('.github/workflows/t.yml', self.workflow("'actions/checkout@v4'"))
        self.assertClean(self.repo.run())

    def test_a_double_quoted_sha_is_accepted(self) -> None:
        sha = '3d3c42e5aac5ba805825da76410c181273ba90b1'
        self.repo.write('.github/workflows/t.yml', self.workflow(f'"actions/checkout@{sha}"'))
        self.assertClean(self.repo.run())

    def test_an_uppercase_sha_is_accepted(self) -> None:
        sha = '3D3C42E5AAC5BA805825DA76410C181273BA90B1'
        self.repo.write('.github/workflows/t.yml', self.workflow(f'actions/checkout@{sha}'))
        self.assertClean(self.repo.run())

    def test_a_quoted_branch_ref_is_still_reported(self) -> None:
        self.repo.write('.github/workflows/t.yml', self.workflow("'actions/checkout@main'"))
        self.assertFinding(self.repo.run(), 'pinned to a branch')

    def test_a_quoted_bare_ref_is_still_reported(self) -> None:
        self.repo.write('.github/workflows/t.yml', self.workflow("'actions/checkout'"))
        self.assertFinding(self.repo.run(), 'has no ref')

    def test_the_message_does_not_quote_the_quotes(self) -> None:
        self.repo.write('.github/workflows/t.yml', self.workflow("'actions/checkout@main'"))
        self.assertIn('`actions/checkout@main`', self.repo.run().stdout)

    def test_a_trailing_comment_is_not_part_of_the_ref(self) -> None:
        sha = '3d3c42e5aac5ba805825da76410c181273ba90b1'
        self.repo.write(
            '.github/workflows/t.yml', self.workflow(f'actions/checkout@{sha} # v7.0.1')
        )
        self.assertClean(self.repo.run())

    def test_a_local_action_needs_no_ref(self) -> None:
        self.repo.write('.github/workflows/t.yml', self.workflow('./.github/actions/thing'))
        self.assertClean(self.repo.run())


class TestParsing(ValidatorTestCase):
    """Every YAML and JSON file has to parse."""

    def test_invalid_yaml_is_reported(self) -> None:
        self.repo.write('config.yml', 'key: [unclosed\n')
        self.assertFinding(self.repo.run(), 'invalid YAML')

    def test_invalid_json_is_reported(self) -> None:
        self.repo.write('data.json', '{"a": 1,}\n')
        self.assertFinding(self.repo.run(), 'invalid JSON')

    def test_jsonc_comments_and_trailing_commas_are_accepted(self) -> None:
        self.repo.write(
            '.vscode/settings.json',
            '{\n  // a comment\n  "a": 1,\n  /* block */\n  "b": [1, 2,],\n}\n',
        )
        self.assertClean(self.repo.run())

    def test_an_unterminated_block_comment_is_reported_in_range(self) -> None:
        # The scan runs to end-of-input when the terminator is missing, then
        # used to append two more characters past the final newline - creating
        # a line that does not exist. GitHub silently drops an annotation whose
        # line is outside the file, so the finding vanished from the diff.
        self.repo.write('.vscode/settings.json', '{\n  /* never closed\n  "a": 1\n}\n')
        result = self.repo.run()
        self.assertEqual(result.returncode, 1)
        reported = [
            int(line.split('settings.json:')[1].split(':')[0])
            for line in result.stdout.splitlines()
            if 'settings.json:' in line and 'invalid' in line
        ]
        self.assertTrue(reported, f'no finding reported:\n{result.stdout}')
        for n in reported:
            self.assertLessEqual(n, 4, f'line {n} is past the end of a 4-line file')


class TestCleanRepository(ValidatorTestCase):
    """The shape a fresh repository actually has."""

    def test_a_tidy_repository_passes(self) -> None:
        self.repo.write('README.md', '# Title\n')
        self.repo.write('config.yml', 'key: value\n')
        self.repo.write('data.json', '{"a": 1}\n')
        self.assertClean(self.repo.run())


class TestBinaryFiles(ValidatorTestCase):
    """What counts as binary is .gitattributes' answer, not a suffix list."""

    def test_a_file_gitattributes_calls_binary_is_not_read_as_text(self) -> None:
        # The bug this replaces: the suffix list covered 14 extensions where
        # .gitattributes marked about forty, so committing a logo in one of
        # the other twenty-six failed the run with "not valid UTF-8".
        self.repo.write('.gitattributes', '*.avif binary\n')
        (self.repo.root / 'logo.avif').write_bytes(b'\x00\x01\xff\xfe not utf-8')
        self.assertClean(self.repo.run())

    def test_an_undeclared_binary_is_still_skipped_by_the_nul_heuristic(self) -> None:
        # No declaration at all: git falls back to looking for a NUL byte
        # under `text=auto`, and so does this.
        (self.repo.root / 'mystery.qqq').write_bytes(b'\x00\x01\xff\xfe')
        self.assertClean(self.repo.run())

    def test_a_text_file_that_is_not_utf8_is_still_reported(self) -> None:
        # No NUL bytes and no binary declaration, so it is a text file this
        # repository cannot read - which is a real finding, not an exemption.
        (self.repo.root / 'latin1.txt').write_bytes('caf\xe9\n'.encode('latin-1'))
        self.assertFinding(self.repo.run(), 'not valid UTF-8')


if __name__ == '__main__':
    unittest.main(verbosity=2)
