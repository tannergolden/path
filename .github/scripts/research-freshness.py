#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Tanner Golden
# SPDX-License-Identifier: MIT
"""List the research reports that have gone stale.

WHY THIS EXISTS. A research report is trusted for three months from the day
its claims were last checked, and stale after that (RES-001 in the universal
rules). Nothing about a stale report looks wrong: it reads as confidently as
the day it was filed. So this reads the date each report in
docs/technical/research/ carries, and names every one past its window, or with
no date at all, for 🔎 Research Freshness to put in one issue.

THE DATE IS THE REPORT'S OWN. The Research Log template keeps it in the
hidden frontmatter as `verified: 'YYYY-MM-DD'`, the last time someone checked
the claims against their sources, so a report verified last week is current
however long ago it was first filed. A report written to the research skill's
own template carries `review_by` instead, the day its window closes, and that
is read as it is. A report with neither, or with the template's placeholder
still in it, cannot show its age, so it counts as stale.

It changes no file. It prints what it found, writes the issue's text where
`--body` says when there is anything to report, and sets the `stale` output
for the workflow when it runs in one.

Run it from the repository root:

    python3 .github/scripts/research-freshness.py
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime
import os
import pathlib
import re
import sys

FOLDER = pathlib.Path('docs/technical/research')
WINDOW_MONTHS = 3
FRONTMATTER = re.compile(r'\A\s*<!--(?P<body>.*?)-->', re.S)
DATE_FIELD = re.compile(r"^(?P<key>verified|review_by):[ \t]*['\"]?(?P<value>[^'\"\n]*?)['\"]?[ \t]*$", re.M)


@dataclasses.dataclass(frozen=True)
class Report:
    """One filed report, and what its date says."""

    path: pathlib.Path
    verified: datetime.date | None
    due: datetime.date | None  # the last day it is trusted; None when it carries no date

    def stale(self, today: datetime.date) -> bool:
        return self.due is None or today > self.due


def add_months(day: datetime.date, months: int) -> datetime.date:
    """The same day `months` later, or the last day of that month when it is shorter."""
    index = day.month - 1 + months
    year, month = day.year + index // 12, index % 12 + 1
    following = datetime.date(year + (month == 12), month % 12 + 1, 1)
    return datetime.date(year, month, min(day.day, (following - datetime.timedelta(days=1)).day))


def parse_date(value: str) -> datetime.date | None:
    try:
        return datetime.date.fromisoformat(value.strip())
    except ValueError:
        return None


def read(path: pathlib.Path) -> Report:
    """A report and its dates, from its own frontmatter."""
    text = path.read_text(encoding='utf-8', errors='replace')
    head = FRONTMATTER.match(text)
    fields = {m.group('key'): parse_date(m.group('value')) for m in DATE_FIELD.finditer(head.group('body'))} \
        if head else {}
    verified = fields.get('verified')
    if verified is not None:
        return Report(path, verified, add_months(verified, WINDOW_MONTHS))
    return Report(path, None, fields.get('review_by'))


def reports(root: pathlib.Path) -> list[Report]:
    """Every report in the folder, the folder's own README aside."""
    folder = root / FOLDER
    if not folder.is_dir():
        return []
    return [read(p) for p in sorted(folder.glob('*.md')) if p.name != 'README.md' and p.is_file()]


def body(stale: list[Report], root: pathlib.Path, link_base: str = '') -> str:
    """The issue that names every stale report, and what to do about each."""
    lines = [
        'Research here is trusted for three months from the day its claims were last verified (RES-001). '
        'These reports are past that, or carry no date, so nothing should rely on them as they stand:',
        '',
        '| Report | Last verified | Stale since |',
        '| :----- | :------------ | :---------- |',
    ]
    for report in stale:
        rel = report.path.relative_to(root).as_posix()
        name = f'[`{report.path.name}`]({link_base}{rel})' if link_base else f'`{rel}`'
        since = (report.due + datetime.timedelta(days=1)).isoformat() if report.due else 'no date'
        lines.append(f"| {name} | {report.verified.isoformat() if report.verified else '-'} | {since} |")
    lines += [
        '',
        'For each one, before anything relies on it: reverify its claims, add a dated log entry and move '
        '`verified` to that day, or replace it with a new research pass in the same file. This issue is '
        'updated every Monday and closes once every report is current.',
        '',
    ]
    return '\n'.join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--root', type=pathlib.Path, default=pathlib.Path('.'), help='the repository root')
    parser.add_argument('--today', type=datetime.date.fromisoformat, default=None,
                        help='the day to judge by, as YYYY-MM-DD (default: today, in UTC)')
    parser.add_argument('--body', type=pathlib.Path, help='where to write the issue text when a report is stale')
    parser.add_argument('--link-base', default='', help='a URL each report path is appended to, for the issue')
    args = parser.parse_args(argv)
    today = args.today or datetime.datetime.now(datetime.timezone.utc).date()

    found = reports(args.root)
    stale = [report for report in found if report.stale(today)]
    if not (args.root / FOLDER).is_dir():
        print(f'{FOLDER.as_posix()}/ does not exist, so there is no research to check.')
    else:
        print(f'{len(found)} report(s) in {FOLDER.as_posix()}/, {len(stale)} stale as of {today.isoformat()}.')
    for report in stale:
        why = f'verified {report.verified.isoformat()}' if report.verified else 'no date'
        print(f'  stale: {report.path.relative_to(args.root).as_posix()} ({why})')
    if stale and args.body:
        args.body.write_text(body(stale, args.root, args.link_base), encoding='utf-8')
    output = os.environ.get('GITHUB_OUTPUT')
    if output:
        with open(output, 'a', encoding='utf-8') as handle:
            handle.write(f'stale={len(stale)}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
