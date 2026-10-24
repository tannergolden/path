#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""Tests for the git hooks in .github/scripts/hooks/.

WHY THIS EXISTS. The hooks repeat, on a contributor's machine, the checks a
pull request runs: the commit-message and DCO rules, and the secret scan. A
hook that has drifted from those rules is worse than none, because it either
blocks a commit CI would accept or waves through one CI will reject after
the push. Every case below is one the standards' own checkers decide.

Each test runs the real hook as a subprocess, the way git does.

Run it:

    python3 .github/scripts/test_hooks.py
"""

from __future__ import annotations

import os
import pathlib
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest

HOOKS = pathlib.Path(__file__).resolve().parent / 'hooks'
COMMIT_MSG = HOOKS / 'commit-msg'
PRE_COMMIT = HOOKS / 'pre-commit'

SIGNOFF = 'Signed-off-by: Ada Lovelace <ada@example.com>'


class CommitMsgTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.dir = pathlib.Path(tempfile.mkdtemp(prefix='commit-msg-test-'))

    def tearDown(self) -> None:
        shutil.rmtree(self.dir, ignore_errors=True)

    def check(self, message: str) -> subprocess.CompletedProcess[str]:
        path = self.dir / 'COMMIT_EDITMSG'
        path.write_text(message, encoding='utf-8')
        return subprocess.run(
            [sys.executable, str(COMMIT_MSG), str(path)],
            capture_output=True, text=True,
        )

    def assertAccepted(self, message: str) -> None:
        result = self.check(message)
        self.assertEqual(result.returncode, 0, result.stderr)

    def assertRejected(self, message: str, reason: str) -> None:
        result = self.check(message)
        self.assertEqual(result.returncode, 1, f'accepted: {message!r}')
        self.assertIn(reason, result.stderr)


class TestHeader(CommitMsgTestCase):
    def test_a_scoped_header_with_a_signoff_is_accepted(self) -> None:
        self.assertAccepted(f'feat(scripts): add a hook\n\nWhy it exists.\n\n{SIGNOFF}\n')

    def test_an_emoji_before_the_subject_is_accepted(self) -> None:
        self.assertAccepted(f'docs(readme): 📝 say how hooks switch on\n\n{SIGNOFF}\n')

    def test_a_breaking_marker_is_accepted(self) -> None:
        self.assertAccepted(f'feat(workflows)!: rename a job\n\n{SIGNOFF}\n')

    def test_the_scope_is_required(self) -> None:
        self.assertRejected(f'feat: add a hook\n\n{SIGNOFF}\n', 'has no scope')

    def test_an_unknown_type_is_rejected(self) -> None:
        self.assertRejected(f'feature(scripts): add a hook\n\n{SIGNOFF}\n', 'is not an allowed type')

    def test_a_capitalised_subject_is_rejected(self) -> None:
        self.assertRejected(f'fix(scripts): Add a hook\n\n{SIGNOFF}\n', 'lowercase letter')

    def test_a_header_that_is_not_conventional_is_rejected(self) -> None:
        self.assertRejected(f'Add a hook\n\n{SIGNOFF}\n', 'does not match')

    def test_an_overlong_header_is_rejected(self) -> None:
        self.assertRejected(f'fix(scripts): {"a" * 100}\n\n{SIGNOFF}\n', 'limit 100')

    def test_every_allowed_type_is_accepted(self) -> None:
        for kind in ('feat', 'fix', 'docs', 'style', 'refactor', 'perf', 'test',
                     'build', 'ci', 'chore', 'revert', 'security'):
            with self.subTest(kind=kind):
                self.assertAccepted(f'{kind}(scripts): change a thing\n\n{SIGNOFF}\n')


class TestBody(CommitMsgTestCase):
    def test_an_em_dash_anywhere_is_rejected(self) -> None:
        self.assertRejected(f'fix(scripts): tidy\n\nOne thing \u2014 then another.\n\n{SIGNOFF}\n', 'em dash')

    def test_an_en_dash_is_rejected_with_it(self) -> None:
        self.assertRejected(f'fix(scripts): tidy\n\nPages 1\u20132.\n\n{SIGNOFF}\n', 'em dash')

    def test_a_missing_signoff_is_rejected(self) -> None:
        self.assertRejected('fix(scripts): tidy\n\nWhy.\n', 'no `Signed-off-by:` trailer')

    def test_a_signoff_inside_a_comment_does_not_count(self) -> None:
        self.assertRejected(f'fix(scripts): tidy\n\n# {SIGNOFF}\n', 'no `Signed-off-by:` trailer')

    def test_an_ai_signoff_is_rejected(self) -> None:
        self.assertRejected(
            'fix(scripts): tidy\n\nSigned-off-by: Claude <noreply@anthropic.com>\n', 'signed off by an AI'
        )

    def test_an_ai_co_author_is_allowed(self) -> None:
        self.assertAccepted(
            'fix(scripts): tidy\n\nCo-Authored-By: Claude <noreply@anthropic.com>\n' f'{SIGNOFF}\n'
        )

    def test_the_verbose_diff_below_the_scissors_is_ignored(self) -> None:
        self.assertAccepted(
            f'fix(scripts): tidy\n\n{SIGNOFF}\n'
            '# ------------------------ >8 ------------------------\n'
            'diff --git a/x b/x\n+Pages 1\u20132 Feat: anything\n'
        )


class TestExemptions(CommitMsgTestCase):
    def test_a_merge_commit_is_left_alone(self) -> None:
        self.assertAccepted("Merge branch 'Development' into feat/topic\n")

    def test_an_autosquash_marker_is_left_alone(self) -> None:
        for prefix in ('fixup! ', 'squash! ', 'amend! '):
            with self.subTest(prefix=prefix):
                self.assertAccepted(f'{prefix}feat(scripts): add a hook\n')

    def test_an_empty_message_is_left_to_git(self) -> None:
        self.assertAccepted('# Please enter the commit message.\n')


class TestPreCommit(unittest.TestCase):
    def setUp(self) -> None:
        self.bin = pathlib.Path(tempfile.mkdtemp(prefix='pre-commit-test-'))

    def tearDown(self) -> None:
        shutil.rmtree(self.bin, ignore_errors=True)

    def fake_gitleaks(self, script: str) -> None:
        path = self.bin / 'gitleaks'
        path.write_text('#!/bin/sh\n' + script, encoding='utf-8')
        path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    def run_hook(self) -> subprocess.CompletedProcess[str]:
        env = dict(os.environ, PATH=f'{self.bin}{os.pathsep}/usr/bin{os.pathsep}/bin')
        return subprocess.run(['sh', str(PRE_COMMIT)], capture_output=True, text=True, env=env)

    def test_without_gitleaks_it_explains_and_lets_the_commit_through(self) -> None:
        if shutil.which('gitleaks', path=f'{self.bin}{os.pathsep}/usr/bin{os.pathsep}/bin'):
            self.skipTest('a real gitleaks is installed system-wide')
        result = self.run_hook()
        self.assertEqual(result.returncode, 0)
        self.assertIn('gitleaks is not installed', result.stderr)

    def test_a_current_gitleaks_scans_the_staged_changes(self) -> None:
        log = self.bin / 'args'
        self.fake_gitleaks(f'echo "$@" >> "{log}"\nexit 0\n')
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('git --pre-commit --staged', log.read_text(encoding='utf-8'))

    def test_an_older_gitleaks_falls_back_to_protect(self) -> None:
        log = self.bin / 'args'
        self.fake_gitleaks(f'[ "$1" = git ] && exit 1\necho "$@" >> "{log}"\nexit 0\n')
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('protect --staged', log.read_text(encoding='utf-8'))

    def test_a_finding_blocks_the_commit(self) -> None:
        self.fake_gitleaks('[ "$1" = git ] && [ "$2" = --help ] && exit 0\nexit 1\n')
        self.assertEqual(self.run_hook().returncode, 1)


class TestInstalled(unittest.TestCase):
    def test_every_hook_is_executable(self) -> None:
        """Git runs only an executable hook, and ignores any other in silence."""
        for hook in (COMMIT_MSG, PRE_COMMIT):
            with self.subTest(hook=hook.name):
                self.assertTrue(os.access(hook, os.X_OK), f'{hook.name} is not executable')


if __name__ == '__main__':
    unittest.main()
