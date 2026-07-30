#!/usr/bin/env python3
"""Tests for the stub ceiling checker.

WHY THIS EXISTS. This program decides whether a stub's `permissions:` block
matches what its called workflow declares, and BOTH directions of a wrong
answer are expensive. Too narrow and the run dies at startup with no log;
too wide and a workflow holds scopes it never asked for. It lived in a
workflow heredoc where nothing could reach it, so every rule it enforces was
untested.

The permission functions are pure, so they are tested directly. Nothing here
reads or writes the repository it ships in.

Run it:

    python3 .github/scripts/test_verify_stub_ceilings.py
"""

from __future__ import annotations

import importlib.util
import pathlib
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent / 'verify-stub-ceilings.py'
_spec = importlib.util.spec_from_file_location('verify_stub_ceilings', SCRIPT)
check = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check)


class TestPermissionsOf(unittest.TestCase):
    """Reading one `permissions:` block, in every form GitHub accepts."""

    def test_absent_is_inherit_not_empty(self) -> None:
        # None means "no block of my own" - the caller decides what that
        # inherits. It must never be confused with an empty block.
        self.assertIsNone(check.permissions_of({}))

    def test_an_explicit_empty_block_is_empty(self) -> None:
        self.assertEqual(check.permissions_of({'permissions': {}}), {})

    def test_none_is_empty(self) -> None:
        self.assertEqual(check.permissions_of({'permissions': 'none'}), {})

    def test_read_all_expands_to_every_scope(self) -> None:
        got = check.permissions_of({'permissions': 'read-all'})
        self.assertEqual(set(got.values()), {'read'})
        self.assertEqual(set(got), set(check.ALL_SCOPES))

    def test_write_all_expands_to_every_scope(self) -> None:
        got = check.permissions_of({'permissions': 'write-all'})
        self.assertEqual(set(got.values()), {'write'})

    def test_models_is_a_scope(self) -> None:
        # GitHub added `models` for the Models API. Omitting it means a callee
        # declaring `read-all` yields a ceiling without it, and a stub that
        # correctly declares `models: read` is reported "wider than declared".
        self.assertIn('models', check.ALL_SCOPES)

    def test_a_mapping_is_copied_not_aliased(self) -> None:
        node = {'permissions': {'contents': 'read'}}
        check.permissions_of(node)['contents'] = 'write'
        self.assertEqual(node['permissions']['contents'], 'read')


class TestCeilingOf(unittest.TestCase):
    """The union across a callee's jobs, which is what a stub must declare."""

    def test_write_beats_read_in_either_order(self) -> None:
        a = {'jobs': {'x': {'permissions': {'contents': 'read'}},
                      'y': {'permissions': {'contents': 'write'}}}}
        b = {'jobs': {'y': {'permissions': {'contents': 'write'}},
                      'x': {'permissions': {'contents': 'read'}}}}
        self.assertEqual(check.ceiling_of(a), {'contents': 'write'})
        self.assertEqual(check.ceiling_of(b), {'contents': 'write'})

    def test_read_beats_none_in_either_order(self) -> None:
        # `none` is the narrowest level, so it can never narrow the union.
        # Comparing only against 'write' let it overwrite a `read` from an
        # earlier job, making the answer depend on job order.
        a = {'jobs': {'x': {'permissions': {'contents': 'read'}},
                      'y': {'permissions': {'contents': 'none'}}}}
        b = {'jobs': {'y': {'permissions': {'contents': 'none'}},
                      'x': {'permissions': {'contents': 'read'}}}}
        self.assertEqual(check.ceiling_of(a), {'contents': 'read'})
        self.assertEqual(check.ceiling_of(b), {'contents': 'read'})

    def test_write_beats_none_in_either_order(self) -> None:
        a = {'jobs': {'x': {'permissions': {'contents': 'write'}},
                      'y': {'permissions': {'contents': 'none'}}}}
        b = {'jobs': {'y': {'permissions': {'contents': 'none'}},
                      'x': {'permissions': {'contents': 'write'}}}}
        self.assertEqual(check.ceiling_of(a), {'contents': 'write'})
        self.assertEqual(check.ceiling_of(b), {'contents': 'write'})

    def test_an_unrecognised_level_is_kept_rather_than_dropped(self) -> None:
        # Better to demand a ceiling that turns out unnecessary than to drop
        # one and fail the run at startup.
        doc = {'jobs': {'x': {'permissions': {'contents': 'read'}},
                        'y': {'permissions': {'contents': 'brand-new'}}}}
        self.assertEqual(check.ceiling_of(doc), {'contents': 'brand-new'})

    def test_a_job_with_no_block_inherits_the_workflow_level_one(self) -> None:
        doc = {'permissions': {'contents': 'read'}, 'jobs': {'j': {}}}
        self.assertEqual(check.ceiling_of(doc), {'contents': 'read'})

    def test_an_explicit_empty_block_does_not_inherit(self) -> None:
        # THE ONE THAT MATTERS. A job saying `permissions: {}` has declared it
        # wants nothing. Treating that as "inherit" makes the checker demand
        # the workflow-level scopes from every stub calling it - telling the
        # maintainer to GRANT contents:write to a job that asked for none.
        doc = {'permissions': {'contents': 'write'}, 'jobs': {'j': {'permissions': {}}}}
        self.assertEqual(check.ceiling_of(doc), {})

    def test_an_explicit_none_does_not_inherit(self) -> None:
        doc = {'permissions': {'contents': 'write'}, 'jobs': {'j': {'permissions': 'none'}}}
        self.assertEqual(check.ceiling_of(doc), {})

    def test_one_job_inheriting_and_one_narrowing(self) -> None:
        doc = {
            'permissions': {'contents': 'read'},
            'jobs': {'inherits': {}, 'narrows': {'permissions': {}}},
        }
        self.assertEqual(check.ceiling_of(doc), {'contents': 'read'})

    def test_a_callee_with_no_permissions_anywhere_wants_nothing(self) -> None:
        self.assertEqual(check.ceiling_of({'jobs': {'j': {}}}), {})


class TestInputsOf(unittest.TestCase):
    """`on:` has four spellings and three of them are not a mapping."""

    def test_a_declared_input_is_found(self) -> None:
        doc = {'on': {'workflow_call': {'inputs': {'dry-run': {'type': 'boolean'}}}}}
        self.assertEqual(check.inputs_of(doc), {'dry-run'})

    def test_a_bare_workflow_call_declares_no_inputs(self) -> None:
        self.assertEqual(check.inputs_of({'on': {'workflow_call': None}}), set())

    def test_on_as_a_bare_string(self) -> None:
        self.assertEqual(check.inputs_of({'on': 'workflow_call'}), set())

    def test_on_as_a_list(self) -> None:
        self.assertEqual(check.inputs_of({'on': ['push', 'workflow_call']}), set())

    def test_yaml_one_dot_one_parses_on_as_the_boolean_true(self) -> None:
        doc = {True: {'workflow_call': {'inputs': {'keep': {'type': 'number'}}}}}
        self.assertEqual(check.inputs_of(doc), {'keep'})


class Tree:
    """A throwaway checkout: stubs here, the standards at the pinned ref."""

    def __init__(self) -> None:
        self.root = pathlib.Path(tempfile.mkdtemp(prefix='ceilings-test-'))
        (self.root / '.github/workflows').mkdir(parents=True)
        (self.root / '.standards/.github/workflows').mkdir(parents=True)

    def stub(self, name: str, body: str) -> None:
        (self.root / '.github/workflows' / name).write_text(
            textwrap.dedent(body).lstrip(), encoding='utf-8')

    def callee(self, name: str, body: str) -> None:
        (self.root / '.standards/.github/workflows' / name).write_text(
            textwrap.dedent(body).lstrip(), encoding='utf-8')

    def run(self) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=self.root, capture_output=True, text=True,
        )

    def cleanup(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)


GOOD_CALLEE = """
    on:
      workflow_call:
        inputs:
          lint-command: {type: string}
    jobs:
      j:
        permissions:
          contents: read
    """

GOOD_STUB = """
    name: 'Good'
    permissions: {}
    jobs:
      ok:
        permissions:
          contents: read
        uses: tannergolden/standards/.github/workflows/ci.yml@v1
    """


class TestSurvivesABadFile(unittest.TestCase):
    """A file it cannot read must cost that file, not the whole run."""

    def setUp(self) -> None:
        self.tree = Tree()
        self.tree.callee('ci.yml', GOOD_CALLEE)
        self.addCleanup(self.tree.cleanup)

    def test_a_clean_tree_passes(self) -> None:
        self.tree.stub('a.yml', GOOD_STUB)
        result = self.tree.run()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('1 stub(s) checked', result.stdout)

    def test_malformed_yaml_is_reported_and_the_others_still_run(self) -> None:
        # 'aaa.yml' sorts first, so an abort here would take 'zzz.yml' with it.
        self.tree.stub('aaa.yml', 'name: broken\n  bad: [indent\n')
        self.tree.stub('zzz.yml', GOOD_STUB)
        result = self.tree.run()
        self.assertNotIn('Traceback', result.stderr)
        self.assertIn('aaa.yml', result.stdout)
        self.assertIn('could not be read as YAML', result.stdout)
        self.assertIn('1 stub(s) checked', result.stdout)
        self.assertEqual(result.returncode, 1)

    def test_a_jobs_block_that_is_not_a_mapping_is_skipped(self) -> None:
        self.tree.stub('aaa.yml', 'name: odd\njobs:\n  - one\n  - two\n')
        self.tree.stub('zzz.yml', GOOD_STUB)
        result = self.tree.run()
        self.assertNotIn('Traceback', result.stderr)
        self.assertIn('1 stub(s) checked', result.stdout)

    def test_a_job_that_is_not_a_mapping_is_skipped(self) -> None:
        self.tree.stub('aaa.yml', 'name: odd\njobs:\n  weird: just-a-string\n')
        self.tree.stub('zzz.yml', GOOD_STUB)
        result = self.tree.run()
        self.assertNotIn('Traceback', result.stderr)
        self.assertIn('1 stub(s) checked', result.stdout)

    def test_a_callee_using_read_all_does_not_crash(self) -> None:
        self.tree.callee('all.yml', 'on: workflow_call\njobs:\n  j:\n    permissions: read-all\n')
        self.tree.stub('a.yml', """
            name: 'A'
            jobs:
              j:
                permissions:
                  contents: read
                uses: tannergolden/standards/.github/workflows/all.yml@v1
            """)
        result = self.tree.run()
        self.assertNotIn('Traceback', result.stderr)
        self.assertIn('1 stub(s) checked', result.stdout)


if __name__ == '__main__':
    unittest.main(verbosity=2)
