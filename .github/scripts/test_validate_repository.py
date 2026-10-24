#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
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

import json
import os
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

    def run(self, event: dict | None = None) -> subprocess.CompletedProcess[str]:
        """Run the validator, under `event` as the payload of the run that started it.

        The suite runs inside CI, whose own event names this repository, so
        the variable is cleared unless a test hands over a payload of its own.
        """
        self.run_git('add', '-A')
        env = {k: v for k, v in os.environ.items() if k != 'GITHUB_EVENT_PATH'}
        if event is not None:
            payload = self.root.parent / f'{self.root.name}-event.json'
            payload.write_text(json.dumps(event), encoding='utf-8')
            env['GITHUB_EVENT_PATH'] = str(payload)
        return subprocess.run(
            [sys.executable, '.github/scripts/validate-repository.py'],
            cwd=self.root, capture_output=True, text=True, env=env,
        )

    def cleanup(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)
        (self.root.parent / f'{self.root.name}-event.json').unlink(missing_ok=True)


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


# Built in halves for the reason the validator gives: initialisation, and
# Template Sync after it, rewrite the whole placeholder in this file too.
PLACEHOLDER = 'OWNER' + '/' + 'REPOSITORY'


class TestPlaceholders(ValidatorTestCase):
    """A placeholder is expected in the template and a defect after initialisation."""

    CONFIG = '.github/ISSUE_TEMPLATE/config.yml'
    LINK = (
        'blank_issues_enabled: false\n'
        'contact_links:\n'
        "  - name: Discussions\n"
        f"    url: 'https://github.com/{PLACEHOLDER}/discussions'\n"
        "    about: 'Questions.'\n"
    )

    def test_the_template_keeps_its_placeholders(self) -> None:
        self.repo.write('.github/TEMPLATE_INIT', 'Not initialised yet.\n')
        self.repo.write(self.CONFIG, self.LINK)
        self.repo.write('.github/CODEOWNERS', '* @your-org/your-team\n')
        self.assertClean(self.repo.run())

    def test_a_contact_link_left_on_the_placeholder_is_reported(self) -> None:
        self.repo.write(self.CONFIG, self.LINK)
        self.assertFinding(self.repo.run(), f'still names {PLACEHOLDER}')

    def test_a_replaced_contact_link_passes(self) -> None:
        self.repo.write(self.CONFIG, self.LINK.replace(PLACEHOLDER, 'octo/widget'))
        self.assertClean(self.repo.run())

    def test_a_comment_naming_the_placeholder_is_not_a_link(self) -> None:
        self.repo.write(self.CONFIG, f'# Replace {PLACEHOLDER} below.\nblank_issues_enabled: false\n')
        self.assertClean(self.repo.run())

    def test_a_codeowners_rule_naming_the_placeholder_team_is_reported(self) -> None:
        self.repo.write('.github/CODEOWNERS', '/docs/   @your-org/your-team\n')
        self.assertFinding(self.repo.run(), 'owns nothing')

    def test_a_commented_codeowners_rule_is_left_alone(self) -> None:
        self.repo.write('.github/CODEOWNERS', '# /docs/   @your-org/your-team\n* @octo\n')
        self.assertClean(self.repo.run())

    def test_initialisation_cannot_rewrite_the_check(self) -> None:
        """The defect: initialisation turned the placeholder in the validator
        into the repository's name, and the check failed every repository
        right after initialisation, on the link it had filled in."""
        here = pathlib.Path(__file__).resolve().parent
        for name in ('validate-repository.py', 'test_validate_repository.py'):
            self.assertNotIn(PLACEHOLDER, (here / name).read_text(encoding='utf-8'), name)

    def test_the_placeholder_elsewhere_is_not_this_checks_business(self) -> None:
        # A seed or a workflow comment may name it on purpose.
        self.repo.write('docs/guide.md', f'Run `gh attestation verify --repo {PLACEHOLDER}`.\n')
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


class TestCompiledCode(ValidatorTestCase):
    """Nobody can review a binary, so none is committed (OpenSSF OSPS-QA-05)."""

    def commit(self, rel: str, data: bytes) -> subprocess.CompletedProcess[str]:
        path = self.repo.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return self.repo.run()

    def test_an_elf_binary_is_reported_whatever_it_is_called(self) -> None:
        self.assertFinding(self.commit('tools/helper.dat', b'\x7fELF\x02\x01\x01' + b'\0' * 64), 'an ELF executable')

    def test_a_mach_o_binary_is_reported(self) -> None:
        self.assertFinding(self.commit('bin/tool', b'\xcf\xfa\xed\xfe' + b'\0' * 64), 'a Mach-O')

    def test_a_windows_binary_is_reported(self) -> None:
        header = bytearray(b'MZ' + b'\0' * 0x7E)
        header[0x3C:0x40] = (0x40).to_bytes(4, 'little')
        header[0x40:0x44] = b'PE\0\0'
        self.assertFinding(self.commit('setup.bin', bytes(header)), 'a Windows executable')

    def test_text_that_happens_to_start_with_mz_is_not(self) -> None:
        self.repo.write('notes/MZ.txt', 'MZ is where the notes start, and that is all.\n' * 3)
        self.assertClean(self.repo.run())

    def test_a_java_class_is_reported(self) -> None:
        self.assertFinding(self.commit('out/App.class', b'\xca\xfe\xba\xbe\x00\x00\x00\x41'), 'compiled Java class')

    def test_python_bytecode_is_reported_by_suffix(self) -> None:
        self.assertFinding(self.commit('pkg/mod.pyc', b'\x6f\x0d\x0d\x0a' + b'\0' * 12), 'a .pyc file')

    def test_a_jar_is_reported(self) -> None:
        self.assertFinding(self.commit('libs/thing.jar', b'PK\x03\x04' + b'\0' * 26), 'a .jar file')

    def test_the_build_tools_wrapper_jars_pass(self) -> None:
        for rel in ('gradle/wrapper/gradle-wrapper.jar',
                    'android/gradle/wrapper/gradle-wrapper.jar',
                    '.mvn/wrapper/maven-wrapper.jar'):
            (self.repo.root / rel).parent.mkdir(parents=True, exist_ok=True)
            (self.repo.root / rel).write_bytes(b'PK\x03\x04' + b'\0' * 26)
        self.assertClean(self.repo.run())

    def test_a_binary_marked_reviewed_passes(self) -> None:
        self.repo.write('.gitattributes', 'tests/fixtures/*.elf binary reviewed-binary\n')
        self.assertClean(self.commit('tests/fixtures/hello.elf', b'\x7fELF\x02\x01\x01' + b'\0' * 64))

    def test_an_image_is_not_compiled_code(self) -> None:
        self.repo.write('.gitattributes', '*.png binary\n')
        self.assertClean(self.commit('assets/logo.png', b'\x89PNG\r\n\x1a\n' + b'\0' * 32))


class TestPublicRepository(ValidatorTestCase):
    """A public repository keeps no vulnerability issue form: an issue there is public."""

    FORM = '.github/ISSUE_TEMPLATE/Vulnerability-Report.yaml'
    PUBLIC = {'repository': {'full_name': 'octo/widget', 'private': False, 'visibility': 'public'}}
    PRIVATE = {'repository': {'full_name': 'octo/widget', 'private': True, 'visibility': 'private'}}

    def setUp(self) -> None:
        super().setUp()
        self.repo.write(self.FORM, "name: 'Vulnerability Report'\ndescription: 'Private repositories only.'\n")

    def test_a_public_repository_keeping_the_form_is_reported(self) -> None:
        self.assertFinding(self.repo.run(self.PUBLIC), 'published the moment it is filed')

    def test_an_event_naming_only_the_private_flag_is_read_too(self) -> None:
        self.assertFinding(self.repo.run({'repository': {'private': False}}), 'delete the form')

    def test_a_private_repository_keeps_it(self) -> None:
        self.assertClean(self.repo.run(self.PRIVATE))

    def test_the_template_keeps_it_for_the_private_repositories_it_generates(self) -> None:
        self.repo.write('.github/TEMPLATE_INIT', 'Not initialised yet.\n')
        self.assertClean(self.repo.run(self.PUBLIC))

    def test_a_public_repository_without_the_form_passes(self) -> None:
        (self.repo.root / self.FORM).unlink()
        self.assertClean(self.repo.run(self.PUBLIC))

    def test_a_run_that_cannot_tell_checks_nothing(self) -> None:
        for event in (None, {'schedule': '0 3 * * 1'}, {'repository': 'octo/widget'}):
            self.assertClean(self.repo.run(event))

    def test_an_unreadable_event_is_not_a_crash(self) -> None:
        self.repo.run_git('add', '-A')
        env = dict(os.environ, GITHUB_EVENT_PATH=str(self.repo.root / 'missing.json'))
        result = subprocess.run([sys.executable, '.github/scripts/validate-repository.py'],
                                cwd=self.repo.root, capture_output=True, text=True, env=env)
        self.assertClean(result)


# The owner's half of docs/Prompts.md exactly as the template ships it, from
# the comment that closes the Golden Path prompts to the end. It is copied here
# rather than read from the page, so an owner writing prompts of their own
# never turns these tests red; a deliberate change to that half updates both.
OWNER_HALF = '''<!-- The Golden Path prompts end here. Everything below this comment is this repository's own, and no template writes to it. -->

---

## ✍️ This Repository's Prompts

> [!TIP]
> **Write this repository's own prompts here**: prompts that only make sense in
> it, such as ones for using it, changing it or understanding how it works. Give
> each a `###` heading, a **Use when** line, a **Fill in** line if it has
> placeholders, and the prompt in one `text` block. If you have many, group them
> under `##` sections of your own after this one. Nothing upstream ever writes
> here. Prompts that work in any repository, and how to write a good one, are in
> the [universal prompts](https://github.com/tannergolden/intelligence/blob/Development/docs/Prompts.md).

---

<div align="center">

**The template's prompts above. Yours below.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
'''
GOLDEN_PATH_HALF = '''# Prompts

<!-- The Golden Path prompts start here. Write nothing inside. -->

### Fit My Project Into This Scaffold

**Use when** you have just generated a repository.

'''


class TestPromptsPage(ValidatorTestCase):
    """The owner's half of docs/Prompts.md, held still in the template alone."""

    def setUp(self) -> None:
        super().setUp()
        self.page = GOLDEN_PATH_HALF + OWNER_HALF
        self.repo.write('.github/TEMPLATE_INIT', 'This repository has not been initialised yet.\n')

    def test_the_page_as_shipped_passes(self) -> None:
        self.repo.write('docs/Prompts.md', self.page)
        self.assertClean(self.repo.run())

    def test_a_change_to_the_golden_path_prompts_passes(self) -> None:
        self.repo.write('docs/Prompts.md', self.page.replace(
            '### Fit My Project Into This Scaffold', '### Fit My Project Into This Layout'))
        self.assertClean(self.repo.run())

    def test_a_change_to_the_owners_section_is_reported(self) -> None:
        self.repo.write('docs/Prompts.md', self.page.replace(
            "Write this repository's own prompts here", 'Write your own prompts here'))
        self.assertFinding(self.repo.run(), "the owner's section changed")

    def test_a_missing_closing_comment_is_reported(self) -> None:
        self.repo.write('docs/Prompts.md', self.page.replace(
            '<!-- The Golden Path prompts end here.', '<!-- The prompts end here.'))
        self.assertFinding(self.repo.run(), 'one opening and one closing comment')

    def test_an_owner_writing_prompts_after_initialisation_passes(self) -> None:
        self.repo.write('docs/Prompts.md', self.page.replace(
            "Write this repository's own prompts here", 'Write our own prompts here'))
        (self.repo.root / '.github' / 'TEMPLATE_INIT').unlink()
        self.assertClean(self.repo.run())


class TestFooterLicence(ValidatorTestCase):
    """A footer links its licence from the repository root, and names none."""

    PAGE = '# Page\n\nBody.\n\nBuilt with care. {clause}\n'
    CLAUSE = 'Distributed under the terms in [LICENSE](/LICENSE).'

    def page(self, clause: str, rel: str = 'docs/Page.md') -> None:
        self.repo.write(rel, self.PAGE.format(clause=clause))

    def test_the_root_link_passes(self) -> None:
        self.page(self.CLAUSE)
        self.assertClean(self.repo.run())

    def test_a_named_licence_is_reported(self) -> None:
        self.page('Distributed under the MIT License.')
        self.assertFinding(self.repo.run(), 'the footer names its licence, MIT')

    def test_a_named_licence_beside_the_link_is_reported(self) -> None:
        self.page('Distributed under the Apache License 2.0, in [LICENSE](/LICENSE).')
        self.assertFinding(self.repo.run(), 'the footer names its licence, Apache')

    def test_a_relative_link_is_reported(self) -> None:
        """It resolves where it is, and breaks when the page is copied to another depth."""
        self.page('Distributed under the terms in [LICENSE](../LICENSE).')
        self.assertFinding(self.repo.run(), 'does not link its licence from the repository root')

    def test_a_footer_with_no_link_is_reported(self) -> None:
        self.page("Distributed under the terms in this repository's LICENSE.")
        self.assertFinding(self.repo.run(), 'does not link its licence from the repository root')

    def test_another_name_for_the_licence_file_passes(self) -> None:
        self.page('Distributed under the terms in [COPYING](/COPYING).')
        self.assertClean(self.repo.run())

    def test_a_clause_quoted_as_code_is_not_a_footer(self) -> None:
        self.repo.write('docs/Guide.md', (
            '# Guide\n\nNever write `Distributed under the MIT License.` in a footer.\n\n'
            '```markdown\nDistributed under the MIT License.\n```\n'
        ))
        self.assertClean(self.repo.run())

    def test_only_markdown_is_read(self) -> None:
        self.repo.write('NOTICE.txt', 'Distributed under the MIT License.\n')
        self.assertClean(self.repo.run())

    def test_the_template_is_held_to_it_as_well(self) -> None:
        """Unlike a placeholder, a stale footer is a defect before initialisation too."""
        self.repo.write('.github/TEMPLATE_INIT', 'This repository has not been initialised yet.\n')
        self.page('Distributed under the MIT License.', 'docs/templates/Seed.md')
        self.assertFinding(self.repo.run(), 'the footer names its licence')


class TestGitUnavailable(unittest.TestCase):
    """A git that cannot answer must say so, not raise."""

    def test_outside_a_checkout_it_explains_itself(self) -> None:
        root = pathlib.Path(tempfile.mkdtemp(prefix='validate-nogit-'))
        self.addCleanup(shutil.rmtree, root, True)
        scripts = root / '.github/scripts'
        scripts.mkdir(parents=True)
        (scripts / 'validate-repository.py').write_text(
            SCRIPT.read_text(encoding='utf-8'), encoding='utf-8')

        result = subprocess.run(
            [sys.executable, '.github/scripts/validate-repository.py'],
            cwd=root, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertNotIn('Traceback', result.stderr)
        self.assertIn('::error::', result.stdout)
        self.assertIn('unverified rather than clean', result.stdout)


if __name__ == '__main__':
    unittest.main(verbosity=2)
