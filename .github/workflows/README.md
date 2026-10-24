<!--
title: '🌿 TRIGGER WORKFLOWS'
description: 'Every workflow in this repository: the name it shows in the Actions tab, what triggers it, and what it does.'
type: index
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
pinned to `@v1`, or, for 🔁 Intelligence Sync, in
[`tannergolden/intelligence`](https://github.com/tannergolden/intelligence)
pinned to `@v0`. The logic lives there, so a fix published once arrives here
without a pull request. Two files run steps of their own instead:
`verify-stubs.yml`, which checks the stubs against the standards, and
`scorecard.yml`, whose score is only accepted from a workflow that keeps to
OpenSSF Scorecard's rules about its own steps.

The stubs are **grouped by concern** - every read-only gate in `checks.yml`,
everything that reacts to people in `governance.yml` - so one push produces one
run to read rather than a dozen. Each file is yours to edit or delete. The
only thing upstream that ever writes here is 🔄 Template Sync, only when you
run it, and only by pull request: it merges the template's fixes to these stubs
with your own edits, never brings back one you deleted, and leaves alone any
you switch off in [`.github/template-sync`](../template-sync).

---

## 📝 File Log

Triggers are each file's `on:` events. A cron is in UTC, and `workflow_dispatch`
means it can also be run by hand from the Actions tab.

<!-- AUTO-INDEX:BEGIN dir=. style=log fields=name,on -->

| Entry                                                  | Name                                   | Triggers                                                                                                                                                                                                                                                                               | Purpose                                                                                                                                                                                                                                                                                                 |
| :----------------------------------------------------- | :------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`apply-standards.yml`](apply-standards.yml)           | &#x1F3AF; Apply Standards              | `workflow_dispatch`                                                                                                                                                                                                                                                                    | Dispatch-only. Run it to apply the shared label taxonomy, and to write the repository settings and the branch and tag rulesets.                                                                                                                                                                         |
| [`auto-format.yml`](auto-format.yml)                   | &#x1F58C;&#xFE0F; Code Style Formatter | `push`, `workflow_dispatch`                                                                                                                                                                                                                                                            | Formats what a formatter can settle, so review is never spent on style.                                                                                                                                                                                                                                 |
| [`auto-index.yml`](auto-index.yml)                     | &#x1F5C2;&#xFE0F; Machined Indexes     | `push`, `workflow_dispatch`                                                                                                                                                                                                                                                            | Keeps every machined index in this repository current: each folder's README log, the decision index among them, and the indexes in README.md.                                                                                                                                                           |
| [`checks.yml`](checks.yml)                             | &#x1F6A6; Checks                       | `push`, `pull_request`, `merge_group`, `schedule` (`0 3 * * 1`), `workflow_dispatch`                                                                                                                                                                                                   | Everything that VERIFIES a change, in one file: lint/test/build, the secret scan, CodeQL, and the workflow lint.                                                                                                                                                                                        |
| [`ci-failure-alert.yml`](ci-failure-alert.yml)         | &#x1F6A8; CI Failure Alerts            | `workflow_run` (`Development`)                                                                                                                                                                                                                                                         | Opens a labeled issue when a watched workflow fails on a long-lived branch, and closes it again when that workflow recovers.                                                                                                                                                                            |
| [`cut-release.yml`](cut-release.yml)                   | &#x1F3F7;&#xFE0F; Cut Release          | `workflow_dispatch`                                                                                                                                                                                                                                                                    | Publishes this template's releases: `vX.Y.Z` for the version, and the moving `vX` that every repository generated from it follows through &#x1F504; Template Sync.                                                                                                                                      |
| [`dependabot-automerge.yml`](dependabot-automerge.yml) | &#x1F9BE; Automate Dependabot          | `pull_request`                                                                                                                                                                                                                                                                         | Approves and queues Dependabot's patch and minor updates.                                                                                                                                                                                                                                               |
| [`governance.yml`](governance.yml)                     | &#x2696;&#xFE0F; Governance            | `pull_request`, `merge_group`, `pull_request_target`, `issues`, `issue_comment`, `schedule` (`0 4 * * 1`), `workflow_dispatch`                                                                                                                                                         | Everything that REACTS to humans, in one file: pull request title and sign-off validation, onboarding and triage, the stale sweep, and the slash commands in issue comments.                                                                                                                            |
| [`intelligence-sync.yml`](intelligence-sync.yml)       | &#x1F501; Intelligence Sync            | `schedule` (`23 6 * * 1`), `workflow_dispatch`                                                                                                                                                                                                                                         | Keeps the universal rules for AI coding agents current in this repository's root AGENTS.md: the block between the INTELLIGENCE markers, which tannergolden/intelligence renders and releases.                                                                                                           |
| [`lifecycle.yml`](lifecycle.yml)                       | &#x1F3AF; Standards Lifecycle          | `push`, `create`, `schedule` (`0 7 * * 1`), `workflow_dispatch`                                                                                                                                                                                                                        | This repository's relationship with the standards, in one file: claimed for its new owner at generation, and told - once - when a new major of the standards exists.                                                                                                                                    |
| [`maintenance.yml`](maintenance.yml)                   | &#x1F9F9; Maintenance                  | `schedule` (`0 6 * * 1`), `workflow_dispatch`                                                                                                                                                                                                                                          | Scheduled housekeeping, in one file: the weekly prune of stale deployments, and the draft-release cleanup.                                                                                                                                                                                              |
| [`preview-deploy.yml`](preview-deploy.yml)             | &#x1F680; Preview Deploy               | `push` (`Preview`), `workflow_dispatch`                                                                                                                                                                                                                                                | Builds a branch and publishes it somewhere reviewable before it is promoted.                                                                                                                                                                                                                            |
| [`prune-runs.yml`](prune-runs.yml)                     | &#x1F9F9; Prune Run History            | `schedule` (`30 6 * * 1`), `workflow_dispatch`                                                                                                                                                                                                                                         | Keeps the Actions tab readable.                                                                                                                                                                                                                                                                         |
| [`README.md`](README.md)                               | -                                      | -                                                                                                                                                                                                                                                                                      | This file.                                                                                                                                                                                                                                                                                              |
| [`release.yml`](release.yml)                           | &#x1F4E6; Release                      | `schedule` (`0 5 * * 1`), `release`, `workflow_dispatch`                                                                                                                                                                                                                               | The whole release chain, in one file: draft the notes through the week, publish the assets when a release is cut, optionally push the package to its registries, and - only when someone asks - prune old releases.                                                                                     |
| [`scorecard.yml`](scorecard.yml)                       | &#x1F6E1;&#xFE0F; OpenSSF Scorecard    | `push`, `schedule` (`0 2 * * 1`), `branch_protection_rule`                                                                                                                                                                                                                             | Scores this repository's supply-chain security with OpenSSF Scorecard - branch protection, pinned dependencies, token permissions, dangerous workflow patterns, signed releases and the rest - and files every finding under Security &#x2192; Code scanning, where it is tracked like any other alert. |
| [`template-sync.yml`](template-sync.yml)               | &#x1F504; Template Sync                | `push`, `pull_request`, `workflow_dispatch`                                                                                                                                                                                                                                            | Brings this repository up to date with the template it was generated from WHEN YOU ASK, and never otherwise: run &#x1F504; Template Sync from the Actions tab.                                                                                                                                          |
| [`verify-stubs.yml`](verify-stubs.yml)                 | &#x1F52C; Verify Stub Ceilings         | `push` (`.github/workflows/**`, `.github/scripts/verify-stub-ceilings.py`, `.github/scripts/requirements.txt`), `pull_request` (`.github/workflows/**`, `.github/scripts/verify-stub-ceilings.py`, `.github/scripts/requirements.txt`), `schedule` (`15 7 * * *`), `workflow_dispatch` | Checks that every stub in this repository declares the permission ceiling its called workflow actually needs, and passes only inputs that workflow accepts.                                                                                                                                             |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch,
from each file's `name:`, its `on:` events and its opening comment.

---

## 🛡️ The Secrets They Read

These are every secret the stubs here pass on, through `secrets: inherit`, to
the workflows they call. None is created for you. Add each under
<kbd>Settings</kbd> → <kbd>Secrets and variables</kbd> → <kbd>Actions</kbd>,
except the one the table files under Dependabot.

| Secret                                     | Read by                                                                                 | Add it when                                                                                 | Without it                                                                                                                                                                                                                                | Expiry and rotation                                                                                                 |
| :----------------------------------------- | :-------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| `ADMIN_TOKEN`                              | 🎯 Apply Standards                                                                      | You write the settings or the rulesets with it                                              | Those two jobs stop and name the missing token; the labels still apply                                                                                                                                                                    | 7 days. Make another when you next apply the standards                                                              |
| `BOT_ACCESS_TOKEN`                         | 🔄 Template Sync, 🗂️ Machined Indexes, 🖌️ Code Style Formatter and 🔁 Intelligence Sync | You want their pull requests to run CI and carry workflow files, or the template is private | Each opens its pull request with the built-in token, so its checks wait for someone with write access to approve them, and it holds back what it changed under `.github/workflows/`; Template Sync cannot fetch a private template at all | A year at most. Renew it before it lapses: the jobs that read it fail until it is renewed or deleted                |
| `BOT_ACCESS_TOKEN`, as a Dependabot secret | 🦾 Automate Dependabot                                                                  | **Allow GitHub Actions to create and approve pull requests** is off                         | The approval falls back to the built-in token, which GitHub refuses with that setting off                                                                                                                                                 | The same token: renew both copies together                                                                          |
| `GITLEAKS_LICENSE`                         | 🚦 Checks, `secrets` job                                                                | An organization owns this repository; the key is free                                       | The scan is skipped, the required check stays green, and one issue says so                                                                                                                                                                | None to set: it unlocks the scanner and reaches nothing else                                                        |
| `DEPLOY_TOKEN`                             | 🚀 Preview Deploy                                                                       | Your `deploy-command` needs a credential                                                    | The command finds `$DEPLOY_TOKEN` empty                                                                                                                                                                                                   | The shortest your provider allows, and every 90 days at most                                                        |
| `NPM_TOKEN`                                | 📦 Release, `package` job, `npm: true`                                                  | The package's first version, which npm needs before it offers a trusted publisher           | npm publishes through trusted publishing, from a trusted publisher naming this repository and `release.yml`, with `node-version: '24.x'` in the stub; without one the job fails and says what to add                                      | Delete it once trusted publishing works: npm is removing direct publishing with a token, announced for January 2027 |
| `PYPI_API_TOKEN`                           | 📦 Release, `package` job, `pypi: true`                                                 | You publish for real, not as a dry run                                                      | The job tries trusted publishing, which PyPI refuses from a reusable workflow, and fails with its reason                                                                                                                                  | Scoped to the one project, and replaced every 90 days                                                               |
| `CARGO_REGISTRY_TOKEN`                     | 📦 Release, `package` job, `crates: true`                                               | The crate's first version, which crates.io needs before it offers a trusted publisher       | The job mints a token that lives 30 minutes through trusted publishing, from a trusted publisher naming this repository and `release.yml`; without one it fails and says why                                                              | Delete it once trusted publishing works                                                                             |
| `REGISTRY_USERNAME`, `REGISTRY_PASSWORD`   | 📦 Release, `package` job, `container: true`                                            | You push to a registry other than GHCR                                                      | GHCR signs in with the built-in token; any other registry fails                                                                                                                                                                           | Every 90 days at most                                                                                               |

**A Dependabot run reads only Dependabot's secrets**, under <kbd>Settings</kbd>
→ <kbd>Secrets and variables</kbd> → <kbd>Dependabot</kbd>, so a
`BOT_ACCESS_TOKEN` kept under Actions alone is empty there. `DEPLOY_TOKEN` may
live in the `preview` environment instead, beside that environment's
reviewers, since the deploy job runs in it.

**Every secret here has a date.** Where a registry offers trusted
publishing, use it and keep no secret at all. Give every other token the
shortest expiry its job allows, and at most the 90 days the standards'
[rotation policy](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md#-rotation--expiry-policy)
sets for a third-party key, and put its renewal in a calendar the day you make
it. Revoke one at once if it leaks, or when someone who could read it leaves.

What each token must be allowed to do: `ADMIN_TOKEN` in the standards'
[Creating the ADMIN_TOKEN](https://github.com/tannergolden/standards/blob/Development/docs/operations/Branch-Protection.md#-creating-the-admin_token),
and `BOT_ACCESS_TOKEN` in [The Token](../template-sync.md#-the-token). Each
called workflow declares the secrets it reads under `secrets:` in its
`workflow_call` block, which is where to look when a stub changes.

---

## ⚠️ Before You Change One

- **The checks run everywhere; most jobs that act on a repository do not run
  in the two golden path templates.** Everything in `checks.yml`, the `pr` check
  in `governance.yml`, `verify-stubs.yml`, `scorecard.yml`, `prune-runs.yml`
  and `auto-index.yml` run in the templates as they do here. A job whose guard
  names the two templates alongside `is_template` does nothing in either and
  comes alive in every other repository, a template derived from one of them
  included. Initialisation and `release.yml` stay silent in every template: a
  template never initialises itself, and releases with `cut-release.yml`.
  `template-sync.yml` checks its list in a template, and `cut-release.yml` runs
  only in a template until a repository released by tag adopts it.
- **`governance.yml` mixes two kinds of trigger on purpose.** The `pr` check
  reads only, so it runs on `pull_request` and `merge_group`; the triage and
  the first-time welcome write labels and comments on a fork's pull request,
  so they run on `pull_request_target`, which GitHub's default policy blocks
  in a public repository, on 2 December 2026 at the latest, unless an Actions
  event policy allows it. 🎯 Apply Standards writes that policy, and it lists
  every event the file uses. Add a trigger to the file, and add it to the
  policy through `actions.event_policy` in a settings override: the next
  settings run puts the policy back as its settings file has it.
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

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
