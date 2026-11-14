#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""Tests for the stale research check.

WHY THIS EXISTS. The check decides which reports an owner is told to
reverify, and both directions of a wrong answer cost something: a stale
report it misses keeps being relied on, and a current one it names teaches
the owner to ignore the issue. The date arithmetic is where it would go
wrong, at a month's end, so that is tested at the edges.

Every test builds its own reports in a temporary folder. Nothing here reads
or writes the repository it ships in.

Run it:

    python3 .github/scripts/test_research_freshness.py
"""

from __future__ import annotations

import contextlib
import datetime
import importlib.util
import io
import os
import pathlib
import shutil
import tempfile
import unittest
from unittest import mock

SCRIPT = pathlib.Path(__file__).resolve().parent / 'research-freshness.py'
_spec = importlib.util.spec_from_file_location('research_freshness', SCRIPT)
fresh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fresh)

day = datetime.date.fromisoformat


def report(verified: str | None = None, *, review_by: str | None = None) -> str:
    """A report's text with its hidden frontmatter, as the Research Log template writes it."""
    fields = ''.join(f"{key}: '{value}'\n" for key, value in (('verified', verified), ('review_by', review_by))
                     if value is not None)
    return f"<!--\ntitle: 'A REPORT'\ntype: record\n{fields}-->\n\n# A Report\n"


class TestAddMonths(unittest.TestCase):
    def test_the_same_day_three_months_on(self) -> None:
        self.assertEqual(fresh.add_months(day('2026-08-14'), 3), day('2026-11-14'))

    def test_a_year_boundary(self) -> None:
        self.assertEqual(fresh.add_months(day('2026-11-20'), 3), day('2027-02-20'))

    def test_a_longer_month_ends_on_the_last_day_of_a_shorter_one(self) -> None:
        self.assertEqual(fresh.add_months(day('2026-11-30'), 3), day('2027-02-28'))
        self.assertEqual(fresh.add_months(day('2027-11-30'), 3), day('2028-02-29'))


class TestReports(unittest.TestCase):
    def setUp(self) -> None:
        self.root = pathlib.Path(tempfile.mkdtemp())
        self.folder = self.root / fresh.FOLDER
        self.folder.mkdir(parents=True)
        self.addCleanup(shutil.rmtree, self.root)

    def write(self, name: str, text: str) -> None:
        (self.folder / name).write_text(text, encoding='utf-8')

    def stale_names(self, today: str) -> list[str]:
        return [r.path.name for r in fresh.reports(self.root) if r.stale(day(today))]

    def test_a_report_is_trusted_through_the_last_day_of_its_window(self) -> None:
        self.write('Queues.md', report('2026-08-14'))
        self.assertEqual(self.stale_names('2026-11-14'), [])
        self.assertEqual(self.stale_names('2026-11-15'), ['Queues.md'])

    def test_a_report_with_no_date_or_the_placeholder_is_stale(self) -> None:
        self.write('Undated.md', '# No frontmatter at all\n')
        self.write('Placeholder.md', report('[YYYY-MM-DD]'))
        self.write('Missing.md', report())
        self.assertEqual(self.stale_names('2026-11-14'), ['Missing.md', 'Placeholder.md', 'Undated.md'])

    def test_review_by_is_the_last_trusted_day_when_there_is_no_verified_date(self) -> None:
        self.write('Skill.md', report(review_by='2026-12-01'))
        self.assertEqual(self.stale_names('2026-12-01'), [])
        self.assertEqual(self.stale_names('2026-12-02'), ['Skill.md'])

    def test_verified_wins_over_review_by(self) -> None:
        self.write('Both.md', report('2026-11-01', review_by='2026-01-01'))
        self.assertEqual(self.stale_names('2026-11-14'), [])

    def test_the_folders_readme_is_not_a_report(self) -> None:
        self.write('README.md', '# Research\n')
        self.assertEqual(fresh.reports(self.root), [])

    def test_a_repository_that_hid_its_docs_has_its_reports_read_from_there(self) -> None:
        hidden = self.root / fresh.HIDDEN
        hidden.mkdir(parents=True)
        (hidden / 'Old.md').write_text(report('2026-01-04'), encoding='utf-8')
        self.write('New.md', report('2026-11-01'))
        self.assertEqual(self.stale_names('2026-11-14'), ['Old.md'])
        self.assertEqual(len(fresh.reports(self.root)), 2)

    def test_a_missing_folder_has_nothing_to_check(self) -> None:
        empty = pathlib.Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, empty)
        self.assertEqual(fresh.reports(empty), [])

    def test_the_command_writes_the_issue_and_the_output_only_for_stale_reports(self) -> None:
        self.write('Old.md', report('2026-01-04'))
        self.write('New.md', report('2026-11-01'))
        issue = self.root / 'issue.md'
        output = self.root / 'output'
        with mock.patch.dict(os.environ, {'GITHUB_OUTPUT': str(output)}), \
                contextlib.redirect_stdout(io.StringIO()) as printed:
            code = fresh.main(['--root', str(self.root), '--today', '2026-11-14', '--body', str(issue),
                               '--link-base', 'https://example.com/blob/main/'])
        self.assertEqual(code, 0)
        self.assertIn('2 report(s)', printed.getvalue())
        self.assertEqual(output.read_text(encoding='utf-8'), 'stale=1\n')
        text = issue.read_text(encoding='utf-8')
        self.assertIn('[`Old.md`](https://example.com/blob/main/docs/technical/research/Old.md)', text)
        self.assertIn('| 2026-01-04 | 2026-04-05 |', text)
        self.assertNotIn('New.md', text)

    def test_nothing_stale_writes_no_issue(self) -> None:
        self.write('New.md', report('2026-11-01'))
        issue = self.root / 'issue.md'
        with mock.patch.dict(os.environ, {'GITHUB_OUTPUT': ''}), contextlib.redirect_stdout(io.StringIO()):
            fresh.main(['--root', str(self.root), '--today', '2026-11-14', '--body', str(issue)])
        self.assertFalse(issue.exists())


if __name__ == '__main__':
    unittest.main()
