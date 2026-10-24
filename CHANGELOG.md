<!--
title: '📒 CHANGELOG'
description: 'What changed in each release of this template, newest first, so an owner can see what a Template Sync will bring before running it.'
type: record
-->

<div align="center">

# 📒 CHANGELOG

<a name="top"></a>

**Every release of the template, and what it changed.**

_Read it before you sync._

</div>

---

Each release of this template is what 🔄 Template Sync offers a generated
repository, so this is the place to read what a sync will bring before running
it. The format follows [Keep a Changelog](https://keepachangelog.com/), and the
versions follow [Semantic Versioning](https://semver.org/): a new major is one
no generated repository follows until its owner chooses to.

**This file belongs to the template alone.** Initialisation deletes it from
every generated repository, whose own release notes are its changelog.

---

## [Unreleased]

> [!IMPORTANT]
> **Cut this release after the standards release it relies on.** Four of the
> changes below work through `tannergolden/standards` rather than through this
> template: the secret scan passing a merge queue, the Actions event policy
> for the governance stub, initialisation removing the Vulnerability Report
> issue form from a public repository, and CI installing the scripts'
> requirements before it runs them. Each takes effect once the standards'
> `v1` moves past it.

_(New repositories only)_ marks a file seeded once, which a sync never brings
to a repository that already exists. _(Template only)_ marks one that
initialisation deletes.

### Added

- **🔁 Intelligence Sync** (`intelligence-sync.yml`): every Monday it proposes
  the shared agent rules from `tannergolden/intelligence` as one pull request,
  which lands only when you merge it. It is silent in the two templates.
- **`docs/Prompts.md`**: the Golden Path's prompts, kept current by a sync,
  and a section for this repository's own prompts that the template never
  changes. It holds the prompts for fitting a project into the scaffold and
  for using your account's community health files.
- **🛡️ OpenSSF Scorecard** (`scorecard.yml`): a weekly supply-chain score on
  public repositories, with its findings filed under code scanning.
- **Git hooks** in `.github/scripts/hooks/`: `commit-msg` checks the
  Conventional Commit header, the `Signed-off-by:` trailer and the author as
  CI does, and `pre-commit` scans staged changes with gitleaks when it is
  installed. The development container switches them on, and `test_hooks.py`
  holds them to CI's rules.
- **`.github/VULNERABILITY_REPORT.yml`**, the form for private vulnerability
  reports, and **`.github/ACCESSIBILITY.md`**.
- **A Maintainers table** in `GOVERNANCE.md`, which the code of conduct and the
  security policy now send people to.
- **Seeds** for a runbook, incident response, a threat model, a dependency
  policy, getting started, a roadmap, a glossary, the release process,
  release verification, an architecture overview and the project's own
  README, under `docs/templates/`.
- **`.github/scripts/requirements.txt`**, pinning the scripts' one dependency,
  PyYAML, by version and hash. Every install of it requires the hashes.
- **A placeholder check** in the repository validator: once initialised, a
  contact link still naming the owner-and-repository placeholder, or a
  CODEOWNERS rule naming `@your-org/your-team`, fails the `ci` check.
- **A footer check** in the repository validator: a document whose footer
  names its licence, or links it any way but `[LICENSE](/LICENSE)` from the
  repository root, fails the `ci` check, here and in every generated
  repository, so no page goes stale when the licence changes.
- **A compiled-code check** in the repository validator: an executable, a
  library, a compiled class, Python bytecode or a Java archive committed
  anywhere fails the `ci` check, recognised by its contents rather than its
  name. A binary the project must keep is marked `reviewed-binary` in
  `.gitattributes`, and the Gradle and Maven wrapper jars pass.
- **`merge_group` triggers** on every required check, so a merge queue gets a
  result from each.
- **Dependabot** for the development container and the scripts'
  requirements, a group for security updates, and an explicit three-day
  cooldown.
- **ADR-0001**, the decision to keep decision records _(new repositories
  only)_.
- **SPDX headers** on every repository script and test.
- A note in the preview deploy stub that a repository created after 15 July
  2026 signs its OIDC tokens with an immutable subject.
- `.git-blame-ignore-revs` _(new repositories only)_, a commit message
  template, and this changelog _(template only)_.
- The seven documentation folders the standards keep, each with a README.

### Changed

- **The required `pr` check runs on `pull_request`**, and on `merge_group`,
  instead of `pull_request_target`, which GitHub's default policy blocks in a
  public repository without an event policy from 2 December 2026 at the
  latest. Only the pull request triage and the first-time welcome still use
  it.
- **The checks run in the template itself.** `ci`, `secrets`, `codeql`,
  `lint` and `pr` are no longer silent there, so what ships is checked before
  it reaches a generated repository.
- **Release pruning is a decision, not a side effect.** The `prune` task of
  📦 Release runs only when dispatched, and previews by default.
- **The code of conduct** is adapted from Contributor Covenant 3.0. Its
  reporting route starts with a maintainer's private contact, since
  **Report content** reaches maintainers only in a public repository an
  organization owns.
- **The security policy** describes the project rather than the template: a
  fallback when private reporting is off, response times a solo maintainer
  can keep, scope, safe harbour, and an end-of-support rule.
- **The governance rules** say who holds administrative access on a personal
  account, that the shipped rulesets exempt admins, and how to keep a
  workflow or a bot token from supplying a required review.
- **Footers name no licence.** Each links to `LICENSE` from the repository
  root, so a repository that chooses a different licence edits nothing else,
  and a document copied to another folder, as every seed is, still reaches it.
- The development container installs Python and the scripts' requirements.
- 🔬 Verify Stub Ceilings installs the pinned requirements before it runs,
  and runs when the checker or its requirements change.
- The CI failure alert watches the Scorecard workflow, and starts only for
  runs on Development.
- The contributing guide, the pull request template and the tooling form are
  consistent with each other and language neutral, and the contributing guide
  says how AI-assisted contributions are handled.
- The discussion forms' README says which categories GitHub creates, and how
  to add one for each other form.
- Hidden keyword lists dropped from the documents' frontmatter.

### Removed

- `.github/DISCUSSION_TEMPLATE/polls.yaml`: GitHub applies no form to a poll.
  A sync removes it where it was never changed.
- `docs/introduction/Integrating-Your-Project.md` and
  `docs/introduction/Using-Your-Account-Defaults.md`, whose prompts moved into
  `docs/Prompts.md`. A repository that already has them keeps its copies.

### Fixed

- `.gitignore` no longer drops the Gradle and Maven wrapper jars, archives and
  Keynote decks under `assets/`, a folder named `env` on a case-insensitive
  file system, or a `downloads/` folder below the root. It now ignores
  Terraform state and variables, keystores, private keys, credential stores,
  `.envrc` and the common tool caches.
- The issue chooser's comments no longer contradict each other about who
  replaces the Discussions link.
- The security policy promised 90 days for a medium severity fix, beyond the
  60 days the OpenSSF Best Practices badge allows.
- The workflow comments, the seeds and the Template Sync guide no longer
  misstate which jobs run in a template, what a release carries, what
  initialisation rewrites, or whether a sync pull request's checks run.
- The folder READMEs said 🗂️ Machined Indexes redraws their logs after every
  push. It runs after a push to the default branch.

### Security

- Initialisation removes the Vulnerability Report issue form from a public
  repository, where an issue would publish the report, and the repository
  validator fails a repository made public later that still carries it.

## [1.3.0] - 2026-10-19

The notes for 1.3.0 and every earlier release were not kept: this release's
page was generated with no entries, and earlier pages were pruned. The commit
history up to
[`bbc8bba`](https://github.com/tannergolden/path/commit/bbc8bba9fe8d1374a199d3e93a45c5ec7825a1a7),
where `v1.3.0` was cut, is the record.

[Unreleased]: https://github.com/tannergolden/path/compare/v1...Development
[1.3.0]: https://github.com/tannergolden/path/tree/bbc8bba9fe8d1374a199d3e93a45c5ec7825a1a7

---

<div align="center">

**Read what changed before you take it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
