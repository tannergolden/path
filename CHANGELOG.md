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

- **🛡️ OpenSSF Scorecard** (`scorecard.yml`): a weekly supply-chain score on
  public repositories, with its findings filed under code scanning.
- **Git hooks** in `.github/scripts/hooks/`: `commit-msg` checks the
  Conventional Commit header and the `Signed-off-by:` trailer, and
  `pre-commit` scans staged changes with gitleaks when it is installed. The
  development container switches them on, and `test_hooks.py` holds them to
  the rules CI applies.
- **`.github/VULNERABILITY_REPORT.yml`**, the form for private vulnerability
  reports, and **`.github/ACCESSIBILITY.md`**.
- **A Maintainers table** in `GOVERNANCE.md`, which the code of conduct and the
  security policy now send people to.
- **Seeds** for a runbook, incident response, a threat model, getting started,
  a roadmap, a glossary, the release process, release verification and an
  architecture overview, under `docs/templates/`.
- **`.github/scripts/requirements.txt`**, pinning the scripts' one dependency,
  PyYAML, by version and hash, instead of relying on the runner image.
- **A placeholder check** in the repository validator: once initialised, a
  contact link still naming `OWNER/REPOSITORY` or a CODEOWNERS rule naming
  `@your-org/your-team` fails the `ci` check.
- **`merge_group` triggers** on every required check, so a merge queue gets a
  result from each (the secret scan's needs the standards release that
  carries it).
- **Dependabot** for the development container and the scripts'
  requirements, a group for security updates, and an explicit three-day
  cooldown.
- `.git-blame-ignore-revs`, a commit message template, and this changelog.
- The seven documentation folders the standards keep, each with a README.
- A prompt for fitting a project into the scaffold, and guidance on when to
  keep a layout of your own.
- A prompt for using the community health files your account already keeps,
  removing only the copies here that you choose.

### Changed

- **The required `pr` check runs on `pull_request`**, and on `merge_group`,
  instead of `pull_request_target`. GitHub blocks `pull_request_target` in
  public repositories without an event policy from 2 December 2026; only the
  pull request triage still uses it.
- **The checks run in the template itself.** `ci`, `secrets`, `codeql`,
  `lint` and `pr` are no longer silent there, so what ships is checked before
  it reaches a generated repository.
- **Release pruning is a decision, not a side effect.** The `prune` task of
  📦 Release runs only when dispatched, and previews by default.
- **The code of conduct** is adapted from Contributor Covenant 3.0, with a
  reporting route that reaches the maintainers.
- **The security policy** describes the project rather than the template: a
  fallback when private reporting is off, response times a solo maintainer
  can keep, scope, safe harbour, and an end-of-support rule.
- **Footers name no licence.** A repository that chooses a different licence
  no longer has to edit every document.
- The development container installs Python and the scripts' requirements.
- 🔬 Verify Stub Ceilings installs the pinned requirements before it runs.
- The CI failure alert watches the Scorecard workflow.
- The contributing guide, the pull request template and the tooling form are
  consistent with each other and language neutral, and the contributing guide
  says how AI-assisted contributions are handled.
- The failure alert starts only for runs on Development.
- Hidden keyword lists dropped from the documents' frontmatter.

### Fixed

- `.gitignore` no longer drops the Gradle and Maven wrapper jars, or archives
  and Keynote decks under `assets/`, and now ignores Terraform state and
  variables, keystores, private keys, `.envrc` and the common tool caches.
- The issue chooser's comments no longer contradict each other about who
  replaces the Discussions link.

### Security

- Initialisation removes the Vulnerability Report issue form from a public
  repository, where an issue would publish the report (needs the standards
  release that carries it).

## [1.3.0] - 2026-10-19

The notes for 1.3.0 and every earlier release were not kept: this release's
page was generated with no entries, and earlier pages were pruned. The commit
history up to the `v1.3.0` tag is the record.

[Unreleased]: https://github.com/tannergolden/path/compare/v1.3.0...Development
[1.3.0]: https://github.com/tannergolden/path/releases/tag/v1.3.0

---

<div align="center">

**Read what changed before you take it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](LICENSE).

</div>
