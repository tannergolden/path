#!/usr/bin/env python3
"""Check every stub's permission ceiling against the workflow it calls.

WHY THIS EXISTS. A caller's `permissions:` block is a CEILING, not a grant:
it caps what the called workflow may request. Ask for less than the callee
declares and the run fails at STARTUP - no job, no step, no log, nothing in
the Actions tab to read. Ask for more and you have handed a workflow scopes
it never said it needed.

IT READS TWO REFS, AND THAT IS THE POINT. The stubs pin `@v1`, so the check
resolves them against `v1` - the code that actually runs. But `v1` is a
MOVING tag, so the same commit can pass at one moment and fail at another:
push a stub that uses something newer than the current release and it fails
until the release moves. That is a true failure, but a DIFFERENT one from a
typo, so it is reported differently. The standards default branch is read
purely to tell the two apart:

    missing at v1, missing on the default branch  -> a real mistake
    missing at v1, PRESENT on the default branch  -> waiting on a release

Run it from the repository root, with the standards checked out at `v1` in
`.standards/` and optionally at its default branch in `.standards-latest/`:

    python3 .github/scripts/verify-stub-ceilings.py
"""

from __future__ import annotations

import os
import pathlib
import re
import sys

import yaml

HERE = pathlib.Path('.github/workflows')
PINNED = pathlib.Path('.standards/.github/workflows')
LATEST = pathlib.Path('.standards-latest/.github/workflows')
CALL = re.compile(r'tannergolden/standards/\.github/workflows/([\w.-]+\.ya?ml)@(\S+)')


def load(path: pathlib.Path):
    return yaml.safe_load(path.read_text(encoding='utf-8')) if path.is_file() else None


# GitHub accepts `permissions: read-all` / `write-all` as shorthand for every
# scope, and `permissions: {}` for none. Both are legal in a callee and
# neither is a mapping, so calling .items() on one used to raise
# AttributeError - a raw traceback here, caused by somebody reformatting a
# workflow in another repository.
ALL_SCOPES = (
    'actions', 'attestations', 'checks', 'contents', 'deployments',
    'discussions', 'id-token', 'issues', 'packages', 'pages',
    'pull-requests', 'repository-projects', 'security-events',
    'statuses',
)


def permissions_of(node):
    perms = (node or {}).get('permissions')
    if perms is None:
        return None                       # inherit; not "declares none"
    if isinstance(perms, str):
        level = perms.replace('-all', '')
        return {} if level == 'none' else {s: level for s in ALL_SCOPES}
    return dict(perms)


def ceiling_of(doc):
    # The union of what the callee's own jobs ask for. write beats read
    # wherever both appear, so the result does not depend on the order the
    # jobs are declared.
    #
    # A job with no block of its own inherits the workflow-level one, which is
    # a legal and common style. Reading only the job blocks made such a callee
    # look like it wanted nothing, and every stub calling it was then reported
    # "wider than declared" - telling the maintainer to remove a ceiling the
    # callee actually needs, which is the startup failure this check exists to
    # prevent.
    # ABSENT and EMPTY are different answers, so the test is `is None` and
    # never truthiness. A job writing `permissions: {}` has declared it wants
    # nothing; `or top` made that fall through to the workflow-level block,
    # so the checker demanded those scopes from every stub calling it - which
    # is advice to GRANT a job privileges it explicitly refused. The stub side
    # below already reads it this way; this side did not.
    top = permissions_of(doc) or {}
    want = {}
    for inner in (doc.get('jobs') or {}).values():
        declared = permissions_of(inner)
        for scope, level in (top if declared is None else declared).items():
            if want.get(scope) != 'write':
                want[scope] = level
    return want


def inputs_of(doc):
    # A bare `workflow_call:` parses as None, not {}. So does a bare
    # `on: workflow_call` written inline, which makes the outer lookup return
    # a string rather than a mapping.
    on = (doc or {}).get(True) or (doc or {}).get('on') or {}
    if isinstance(on, str):
        on = {on: {}}
    if isinstance(on, list):
        on = {k: {} for k in on}
    spec = on.get('workflow_call') or {}
    return set(spec.get('inputs') or {})


def main() -> int:
    broken, pending, checked = [], [], 0
    comparable = LATEST.is_dir()

    # Both extensions, on both sides. GitHub accepts .yaml for a stub and for
    # a reusable workflow alike; globbing only *.yml meant renaming a stub
    # silently dropped it from the check while this job still reported green.
    stubs = sorted(set(HERE.glob('*.yml')) | set(HERE.glob('*.yaml')))

    for f in stubs:
        doc = yaml.safe_load(f.read_text(encoding='utf-8')) or {}
        for job_id, job in (doc.get('jobs') or {}).items():
            m = CALL.search(str(job.get('uses', '')))
            if not m:
                continue
            name = m.group(1)
            pinned = load(PINNED / name)
            latest = load(LATEST / name) if comparable else None

            if pinned is None:
                if latest is not None:
                    pending.append(
                        f"{f.name}: job '{job_id}' calls {name}, which exists on the "
                        f"standards default branch but is NOT in the release v1 points "
                        f"at. Cut a release with move-major; this check clears itself "
                        f"on its daily run.")
                else:
                    broken.append(
                        f"{f.name}: job '{job_id}' calls {name}, which does not exist in "
                        f"tannergolden/standards at v1 or on its default branch.")
                continue

            checked += 1

            # Passing an input a reusable workflow does not declare is not
            # ignored - it fails the run.
            unknown = sorted(set(job.get('with') or {}) - inputs_of(pinned))
            if unknown:
                nowhere = sorted(set(unknown) - (inputs_of(latest) if latest else set()))
                if latest is not None and not nowhere:
                    pending.append(
                        f"{f.name}: job '{job_id}' passes {unknown}, which {name} accepts "
                        f"on the standards default branch but NOT at v1. Cut a release "
                        f"with move-major; this check clears itself on its daily run.")
                else:
                    broken.append(
                        f"{f.name}: job '{job_id}' passes {nowhere or unknown}, which "
                        f"{name} does not accept - the run fails, it is not ignored.")

            want = ceiling_of(pinned)
            # Same inheritance rule on this side: a stub job with no block of
            # its own is capped by the workflow-level one.
            have = permissions_of(job)
            if have is None:
                have = permissions_of(doc) or {}
            if have != want:
                if latest is not None and have == ceiling_of(latest):
                    pending.append(
                        f"{f.name}: job '{job_id}' declares the ceiling {name} asks for on "
                        f"the standards default branch, not the one at v1 ({want}). Cut a "
                        f"release with move-major; this check clears itself on its daily run.")
                else:
                    missing = {k: v for k, v in want.items() if have.get(k) != v}
                    extra = {k: v for k, v in have.items() if k not in want}
                    detail = []
                    if missing:
                        detail.append(f"missing or too narrow: {missing} (this fails the run at startup)")
                    if extra:
                        detail.append(f"wider than declared: {extra}")
                    broken.append(
                        f"{f.name}: job '{job_id}' declares {have or '{}'}; "
                        f"{name} asks for {want}. " + '; '.join(detail))

    for problem in broken:
        print(f"::error title=Stub ceiling::{problem}")
    for problem in pending:
        print(f"::error title=Waiting on a release::{problem}")
    if not comparable:
        print("::warning title=Stub ceiling::Could not read the standards default branch, "
              "so a genuine mistake cannot be told apart from a change awaiting release.")

    verdict = (
        f"{checked} stub(s) checked, {len(broken)} problem(s), "
        f"{len(pending)} waiting on a release."
    )
    print("\n" + verdict)

    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a', encoding='utf-8') as handle:
            handle.write("### 🔬 Stub ceilings\n\n" + verdict + "\n")
            for problem in broken:
                handle.write(f"\n- ❌ {problem}\n")
            for problem in pending:
                handle.write(f"\n- ⏳ {problem}\n")
            if pending and not broken:
                handle.write(
                    "\n> [!NOTE]\n> Nothing here is wrong with the stubs: they use "
                    "standards changes that are merged but not released. Cut a release "
                    "with `move-major`, or wait for the daily run once you have.\n")

    return 1 if (broken or pending) else 0


if __name__ == '__main__':
    sys.exit(main())
