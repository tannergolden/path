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

### Added

- **Golden Path prompts for staying current and following the standards**,
  in `docs/Prompts.md`, with an index at the top of the template's section:
  Get Ready For A Template Sync and Review A Template Sync Pull Request
  around each sync you run, Bring In The Latest Agent Rules for the pull
  request 🔁 Intelligence Sync opens, and ten read-only audits of a
  repository against `tannergolden/standards`, from Check This Repository
  Against The Standards to Check What Is Left To Do By Hand.

### Changed

- **Dependabot opens one pull request a month**, not one per ecosystem: the
  workflows, the development container and the scripts' requirements join a
  multi-ecosystem group, `dependencies`, which holds the monthly schedule and
  the `build` commit prefix. A major update in it holds that month's pull
  request for a person. An ecosystem you added to `.github/dependabot.yml`
  keeps a pull request of its own until it joins the group: give it
  `multi-ecosystem-group: 'dependencies'` and `patterns: ['*']`, and take out
  its `schedule` and `commit-message`, which Dependabot refuses on a member.

## [1.4.1] - 2026-10-25

> [!NOTE]
> **Most of this release's updates work through `tannergolden/standards`**,
> and reached every repository on `@v1` with its v1.18.0, released just before
> this one: every action the shared workflows pin, and a `timeout-minutes`
> input on the 🧪 Lint, Test & Build job for a suite that runs close to its
> fifteen minutes.

### Changed

- **The development container takes `common-utils` 2**, the feature's current
  major, in place of 1.
- **`scorecard.yml` and `verify-stubs.yml` pin the actions' current
  releases**: harden-runner 2.22.2, codeql-action's upload-sarif 4.39.1 and
  setup-python 7.1.0, as Dependabot proposed in every repository generated
  from this template.

## [1.4.0] - 2026-10-25

> [!NOTE]
> **These changes work through `tannergolden/standards`**, not through this
> template, and reached every repository on `@v1` with its v1.17.0, released
> just before this one:
>
> - the secret scan passing a merge queue, and the Actions event policy for
>   the governance stub;
> - initialisation removing the Vulnerability Report issue form from a
>   public repository;
> - CI and 🏷️ Cut Release installing the scripts' requirements before they
>   run them;
> - trusted publishing to npm and crates.io, the licence attached to each
>   release, and the summary prompt at the top of drafted release notes;
> - Dependency Review as a required check, and every required check accepted
>   from GitHub Actions alone, once 🎯 Apply Standards reapplies the rulesets.

_(New repositories only)_ marks a file seeded once, which a sync never brings
to a repository that already exists. _(Template only)_ marks one that
initialisation deletes.

### Added

- **🔁 Intelligence Sync** (`intelligence-sync.yml`): every Monday it proposes
  the shared agent rules from `tannergolden/intelligence` as one pull request,
  which lands only when you merge it. It is silent in the template itself.
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
- **`examples/`**, for runnable examples of the project in use, reserved like
  `packages/` and `benchmarks/` until the project needs it _(new repositories
  only)_. The prompt for fitting a project into the scaffold names it beside
  them.

### Changed

- **The required `pr` check runs on `pull_request`**, and on `merge_group`,
  instead of `pull_request_target`, which GitHub's default policy blocks in a
  public repository without an event policy from 2 December 2026 at the
  latest. Only the pull request triage and the first-time welcome still use
  it.
- **The checks run in the template itself.** `ci`, `secrets`, `codeql`,
  `lint` and `pr` are no longer silent there, so what ships is checked before
  it reaches a generated repository.
- **The guards name this template alone.** Each job that is silent in the
  golden path template names only `path` in its `if:`, and the workflow
  comments, the README and the Template Sync guide say the same. A generated
  repository's jobs run exactly as before.
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
- The development container installs Python and the scripts' requirements,
  and gitleaks from Ubuntu's archive, so the `pre-commit` hook scans what is
  staged.
- **The secrets table** in `.github/workflows/README.md` gives every secret
  an expiry or a rotation, says npm and crates.io publish without a token
  once a package has its first version, and says PyPI still needs its token.
  The release stub's `package` job says the same.
- The required checks are listed with Dependency Review wherever the
  documents name them.
- The README points at the project README seed, and at the standards'
  checklist for making a repository public.
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
- **The required `pr` check has a workflow of its own**, `semantic-pr.yml`.
  Beside the triage in `governance.yml`, which runs on `pull_request_target`,
  it was listed a second time, skipped, on every pull request. If you keep a
  `governance.yml` of your own, delete its `pr` job, or the check runs twice.

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
- The Source Code seed recommended a `lib/` layer that `src/` does not ship
  and no other document names. It now has the three layers `src/` has, with
  the rules `src/README.md` gives them.
- The technical documents' README named five of the six areas the fill-in
  standards lay out, leaving out `benchmarks/`.
- The workflow comments, the seeds and the Template Sync guide no longer
  misstate which jobs run in a template, what a release carries, what
  initialisation rewrites, or whether a sync pull request's checks run.
- The folder READMEs said 🗂️ Machined Indexes redraws their logs after every
  push. It runs after a push to the default branch.
- **Each check shows once on a pull request.** A push to a pull request's
  branch, and the branch's creation, started a second run of 🚦 Checks,
  🔄 Template Sync, 🎯 Standards Lifecycle, 🗂️ Machined Indexes,
  🖌️ Code Style Formatter, 🛡️ OpenSSF Scorecard and 🔬 Verify Stub Ceilings
  whose every job skipped, and each skipped job showed on the pull request
  beside the real one. A push now starts them on `Development` alone, and
  🎯 Standards Lifecycle no longer starts on `create`. The push triggers name
  the default branch, as 🚨 CI Failure Alerts' filter does: rename
  `Development` and rename it there too.

### Security

- Initialisation removes the Vulnerability Report issue form from a public
  repository, where an issue would publish the report, and the repository
  validator fails a repository made public later that still carries it.
- The `pr` job in `semantic-pr.yml` no longer grants `statuses: write`. The
  standards stopped asking for it in v1.17.0: the semantic title check
  writes no commit status, and a grant it never uses would let the
  third-party action post a status under any name, a required check's
  included.

## [1.3.0] - 2026-10-19

The notes for 1.3.0 and every earlier release were not kept: this release's
page was generated with no entries, and earlier pages were pruned. The commit
history up to
[`bbc8bba`](https://github.com/tannergolden/path/commit/bbc8bba9fe8d1374a199d3e93a45c5ec7825a1a7),
where `v1.3.0` was cut, is the record.

[Unreleased]: https://github.com/tannergolden/path/compare/v1...Development
[1.4.1]: https://github.com/tannergolden/path/releases/tag/v1.4.1
[1.4.0]: https://github.com/tannergolden/path/releases/tag/v1.4.0
[1.3.0]: https://github.com/tannergolden/path/tree/bbc8bba9fe8d1374a199d3e93a45c5ec7825a1a7

---

<div align="center">

**Read what changed before you take it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
