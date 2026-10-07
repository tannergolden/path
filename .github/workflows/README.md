<!--
title: '🌿 TRIGGER WORKFLOWS'
description: 'Every workflow in this repository: the name it shows in the Actions tab, what triggers it, and what it does.'
tags: [workflows, github-actions, ci-cd, automation]
category: docs
-->

<div align="center">

# 🌿 TRIGGER WORKFLOWS

<a name="top"></a>

**The small files that decide when automation runs, then hand the work to the standards.**

_Every trigger here is yours. Every engine is shared._

</div>

---

## 💡 What This Folder Is For

GitHub runs a workflow only from this folder of the repository being pushed to.
So almost every file here is a **stub**: it names the events it answers and the
permissions it allows, then calls a reusable workflow in
[`tannergolden/standards`](https://github.com/tannergolden/standards/blob/Development/.github/workflows/README.md)
pinned to `@v1`. The logic lives there, so a fix published once arrives here
without a pull request.

The stubs are **grouped by concern** - every read-only gate in `checks.yml`,
everything that reacts to people in `governance.yml` - so one push produces one
run to read rather than a dozen. Each file is yours to edit or delete, and
nothing upstream ever writes to this folder.

---

## 📝 File Log

Triggers are each file's `on:` events. A cron is in UTC, and `workflow_dispatch`
means it can also be run by hand from the Actions tab.

<!-- AUTO-INDEX:BEGIN dir=. style=log fields=name,on -->

| Entry                                                  | Name                                   | Triggers                                                                                                                 | Purpose                                                                                                                                                                                                         |
| :----------------------------------------------------- | :------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`apply-standards.yml`](apply-standards.yml)           | &#x1F3AF; Apply Standards              | `workflow_dispatch`                                                                                                      | Dispatch-only. Run it to apply the shared label taxonomy, and to write the branch and tag rulesets.                                                                                                             |
| [`auto-format.yml`](auto-format.yml)                   | &#x1F58C;&#xFE0F; Code Style Formatter | `push`, `workflow_dispatch`                                                                                              | Formats what a formatter can settle, so review is never spent on style.                                                                                                                                         |
| [`auto-index.yml`](auto-index.yml)                     | &#x1F5C2;&#xFE0F; Machined Indexes     | `push`, `workflow_dispatch`                                                                                              | Keeps every machined index in this repository current: each folder's README log, the decision register, and the indexes in README.md.                                                                           |
| [`checks.yml`](checks.yml)                             | &#x1F6A6; Checks                       | `push`, `pull_request`, `schedule` (`0 3 * * 1`), `workflow_dispatch`                                                    | Everything that VERIFIES a change, in one file: lint/test/build, the secret scan, CodeQL, and the workflow lint.                                                                                                |
| [`ci-failure-alert.yml`](ci-failure-alert.yml)         | &#x1F6A8; CI Failure Alerts            | `workflow_run`                                                                                                           | Opens a labeled issue when a watched workflow fails on a long-lived branch, and closes it again when that workflow recovers.                                                                                    |
| [`dependabot-automerge.yml`](dependabot-automerge.yml) | &#x1F9BE; Automate Dependabot          | `pull_request`                                                                                                           | Approves and queues Dependabot's patch and minor updates.                                                                                                                                                       |
| [`governance.yml`](governance.yml)                     | &#x2696;&#xFE0F; Governance            | `pull_request_target`, `issues`, `issue_comment`, `schedule` (`0 4 * * 1`), `workflow_dispatch`                          | Everything that REACTS to humans, in one file: pull request title and sign-off validation, onboarding and triage, the stale sweep, and the slash commands in issue comments.                                    |
| [`lifecycle.yml`](lifecycle.yml)                       | &#x1F3AF; Standards Lifecycle          | `push`, `create`, `schedule` (`0 7 * * 1`), `workflow_dispatch`                                                          | This repository's relationship with the standards, in one file: claimed for its new owner at generation, and told - once - when a new major of the standards exists.                                            |
| [`maintenance.yml`](maintenance.yml)                   | &#x1F9F9; Maintenance                  | `schedule` (`0 6 * * 1`), `workflow_dispatch`                                                                            | Scheduled housekeeping, in one file: the weekly prune of workflow runs and stale deployments, and the draft-release cleanup.                                                                                    |
| [`preview-deploy.yml`](preview-deploy.yml)             | &#x1F680; Preview Deploy               | `push` (`Preview`), `workflow_dispatch`                                                                                  | Builds a branch and publishes it somewhere reviewable before it is promoted.                                                                                                                                    |
| [`prune-runs.yml`](prune-runs.yml)                     | &#x1F9F9; Prune Run History            | `schedule` (`30 6 * * 1`), `workflow_dispatch`                                                                           | Keeps the Actions tab readable.                                                                                                                                                                                 |
| [`README.md`](README.md)                               | -                                      | -                                                                                                                        | This file.                                                                                                                                                                                                      |
| [`release.yml`](release.yml)                           | &#x1F4E6; Release                      | `schedule` (`0 5 * * 1`), `release`, `workflow_dispatch`                                                                 | The whole release chain, in one file: draft the notes through the week, publish the assets when a release is cut, optionally push the package to its registries, and prune the releases the new one superseded. |
| [`verify-stubs.yml`](verify-stubs.yml)                 | &#x1F52C; Verify Stub Ceilings         | `push` (`.github/workflows/**`), `pull_request` (`.github/workflows/**`), `schedule` (`15 7 * * *`), `workflow_dispatch` | Checks that every stub in this repository declares the permission ceiling its called workflow actually needs, and passes only inputs that workflow accepts.                                                     |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from each file's `name:`,
its `on:` events and its opening comment.

---

## ⚠️ Before You Change One

- **Most of these are silent in the template.** A job guarded by
  `!github.event.repository.is_template` does nothing in the template and comes
  alive in every repository generated from it. `prune-runs.yml`,
  `verify-stubs.yml` and `auto-index.yml` carry no such guard and run in the
  template as well.
- **Three job ids are check names.** `ci` and `secrets` in `checks.yml`, and
  `pr` in `governance.yml`, report as `<job id> / <job name>`, which is what
  branch protection requires. Rename one and every pull request waits on a
  check that never reports.
- **`ci-failure-alert.yml` watches by name.** It matches the `name:` at the top
  of each file, so renaming a workflow means renaming it in that list too.
- **A job's `permissions:` block is a ceiling, not a grant.** Ask for less than
  the called workflow declares and the run fails before it starts, with no log
  to read. `verify-stubs.yml` exists to catch exactly that.

---

<div align="center">

**One file per concern. Every engine called, never copied.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../../LICENSE).

</div>
