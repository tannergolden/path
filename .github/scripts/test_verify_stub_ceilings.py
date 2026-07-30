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

    def test_a_job_with_no_block_inherits_the_workflow_level_one(self) -> None:
        doc = {'permissions': {'contents': 'read'}, 'jobs': {'j': {}}}
        self.assertEqual(check.ceiling_of(doc), {'contents': 'read'})

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


if __name__ == '__main__':
    unittest.main(verbosity=2)
