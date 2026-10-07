<!--
title: '🌿 TRIGGER WORKFLOWS'
description: 'Every workflow file in this repository: its name in the Actions tab, when it runs, what it does, and which shared workflow it calls.'
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

Times are UTC. "Dispatch" means it can also be run by hand from the Actions tab.

| File                                                   | Shows as                | Runs                                                              | Does                                                                                                                                                    |
| :----------------------------------------------------- | :---------------------- | :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`apply-standards.yml`](apply-standards.yml)           | 🎯 Apply Standards      | Dispatch only                                                     | Applies the label taxonomy and, when asked, the repository settings and rulesets. Previews by default                                                   |
| [`auto-format.yml`](auto-format.yml)                   | 🖌️ Code Style Formatter | Push to the default branch, dispatch                              | Formats whatever a formatter can settle and delivers the fix as a pull request, never a push to your branch                                             |
| [`checks.yml`](checks.yml)                             | 🚦 Checks               | Pull request, push to the default branch, Mondays 03:00, dispatch | Every gate that verifies a change: lint, test and build (`ci`), the secret scan (`secrets`), CodeQL, and the workflow lint                              |
| [`ci-failure-alert.yml`](ci-failure-alert.yml)         | 🚨 CI Failure Alerts    | A watched workflow finishing                                      | Opens an issue when a watched workflow fails on a long-lived branch, and closes it again on recovery                                                    |
| [`dependabot-automerge.yml`](dependabot-automerge.yml) | 🦾 Automate Dependabot  | Pull request                                                      | Approves and queues Dependabot's patch and minor updates. A major waits for a human                                                                     |
| [`governance.yml`](governance.yml)                     | ⚖️ Governance           | Pull request, new issue, comment, Mondays 04:00, dispatch         | Title and sign-off checks (`pr`), onboarding, labelling, the stale sweep, and the slash commands                                                        |
| [`lifecycle.yml`](lifecycle.yml)                       | 🎯 Standards Lifecycle  | Push, new branch or tag, Mondays 07:00, dispatch                  | Claims a generated repository for its owner once, then opens one issue when a new major of the standards exists                                         |
| [`maintenance.yml`](maintenance.yml)                   | 🧹 Maintenance          | Mondays 06:00, dispatch                                           | Prunes stale deployments. Deletes draft releases only on a dispatch that asks for it                                                                    |
| [`preview-deploy.yml`](preview-deploy.yml)             | 🚀 Preview Deploy       | Push to `Preview`, dispatch                                       | Builds the `Preview` branch and deploys it, once it is given a `deploy-command`                                                                         |
| [`prune-runs.yml`](prune-runs.yml)                     | 🧹 Prune Run History    | Mondays 06:30, dispatch                                           | Deletes old runs with their logs and artifacts, keeping a week of commit-triggered runs and one run per workflow                                        |
| [`release.yml`](release.yml)                           | 📦 Release              | Mondays 05:00, release published, dispatch                        | Drafts the notes, publishes the assets, pushes the package where enabled, and prunes superseded release pages                                           |
| [`verify-stubs.yml`](verify-stubs.yml)                 | 🔬 Verify Stub Ceilings | A workflow file changing, daily 07:15, dispatch                   | Proves every stub's `permissions:` ceiling and inputs match the workflow it calls, with [`verify-stub-ceilings.py`](../scripts/verify-stub-ceilings.py) |
| [`README.md`](README.md)                               | -                       | -                                                                 | This log. GitHub reads only the `.yml` and `.yaml` files in this folder                                                                                 |

Add a row here in the same change that adds a workflow.

---

## ⚠️ Before You Change One

- **Most of these are silent in the template.** A job guarded by
  `!github.event.repository.is_template` does nothing in the template and comes
  alive in every repository generated from it. `prune-runs.yml` and
  `verify-stubs.yml` carry no such guard and run in the template as well.
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
