<!--
title: '🤝 CONTRIBUTING GUIDELINES'
description: 'How to contribute, covering branching, commits, code style, testing, and the pull-request process.'
tags: [contributing, standards, workflow, community]
category: community
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🤝 CONTRIBUTING GUIDELINES

<a name="top"></a>

**Accelerating the engineering ecosystem through structured and safe contributions.**

_Small diffs. Green gates. Shared standards._

</div>

---

## 🎯 Our Philosophy

We value **small, frequent, and high-quality** contributions that adhere to our established patterns. Every change should move us closer to a more stable, secure, and context-ready ecosystem. We do not accept "code dumps" - every line must be justified and tested.

> [!IMPORTANT]
> All contributors - whether human engineers or AI agents - must read and adhere to the **[engineering standards](https://github.com/tannergolden/standards/blob/Development/docs/README.md)** before submitting code.

---

## 🏗️ Getting Started

### 1. Prepare Your Environment

- Fork the repository (for external contributors).
- Set up your local toolchain so it matches CI. The exact command is this project's own - whatever `.github/workflows/checks.yml` is configured to run is the authority, so start there if you are unsure.

- Review the **[Testing Strategy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Testing-Strategy.md)** to understand our testing layers.

> [!TIP]
> **New here?** Start with an issue labelled **`good first issue`** or **`help wanted`** - these are small, well-scoped tasks that need no deep context. Maintainers keep a few open on purpose (see [Governance](GOVERNANCE.md)).

### 2. Branching Strategy

- **Target Branch:** Always target **`Development`** for new features. `Release` is the production line and is promoted to, never committed to directly.
- **Naming Convention:** Use descriptive prefixes:
  - `feat/description`
  - `bugfix/issue-description`
  - `docs/update-description`
- Detailed workflows are available in **[Branching Strategy & Workflow](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Branching-Strategy-&-Workflow.md)**.

---

## 🧱 Development Standards

### Commit Message Conventions

We strictly enforce **Conventional Commits** (`type(scope): summary`). This is critical because our release pipelines read these messages to automatically generate changelogs and determine semantic version numbers.

- **Format**: `type(scope): 🩹 summary`
- **Types (the full enforced set)**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`, `security`.
- **Message Format**: the full standard, including the required scope and the required body, is **[Conventional Commits](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Conventional-Commits.md)**.

### Code Quality Checklist

- **Linting**: All code must pass the linter before submission. Run this project's lint command locally - the one configured as `lint-command` in `.github/workflows/checks.yml`.
- **Testing**: Unit tests are required for all logic updates. Run the `test-command` from the same file to verify.
- **Documentation**: Update the relevant `docs/` files if your change impacts project behavior or setup instructions.

### Test Policy (required)

This is a **mandated policy**, not a preference:

- **Every change that adds or changes functionality MUST add or update tests** covering the new behavior. A PR that changes logic without touching tests will be asked to add them.
- **Document the tests you add** in the PR description - say what behavior each new test pins down, so reviewers can confirm coverage matches intent.
- **Bug fixes get a regression test** that fails before the fix and passes after.
- The suite must be green before review begins.

### Coding Style

- **Formatting**: this project's formatter is the authority, and its lint command must pass. Record which one it is in `docs/technical/` so the choice is written down somewhere rather than inferred.
- **Naming**: follow the prevailing convention of the language you are writing in. Consistency with the surrounding file beats consistency with any other project.
- **Types**: where the language has a strict mode, use it. Prefer an explicit type at a public boundary over an inferred one.
- **Logic**: favour pure functions and immutability; use guard clauses rather than deep nesting; raise errors with enough context to act on and handle them at a boundary.

### Testing Standards

- **Location**: co-locate unit tests (`foo.test.*`) next to source; keep E2E/integration suites under `tests/`.
- **Mocking**: always mock network/API calls; isolate pure logic from heavy dependencies.
- **Structure**: `describe("Unit", …)` / `it("should <behaviour> when <condition>", …)` with descriptive assertions.
- **Gate**: the test suite must pass before merge; add meaningful tests for every logic change, not assertions that cannot fail.

### Workflow (CI) Authoring

- **Naming**: `kebab-case.yml`; emoji-prefixed job names; explicit `on:` triggers.
- **Security**: pin third-party actions to a full commit SHA or a stable tag; declare a top-level `permissions: {}` and grant scopes per job; never print secrets.
- **Reliability**: set `timeout-minutes` on every job that has `steps:` - GitHub does not accept it on a job that calls a reusable workflow, so a stub cannot carry one and the callee sets its own. Use `concurrency` groups. Keep workflow logic short: anything longer than a few lines belongs in a script under `.github/scripts/`, where it can be tested, rather than inline YAML where it cannot.

---

## 🚀 The Pull Request Process

### 1. Opening the PR

- Target the **`Development`** branch.
- Complete the **[Pull Request Template](pull_request_template.md)** in its entirety. Empty descriptions will be closed.
- **Sign off your commits (DCO).** By adding a `Signed-off-by` line you certify the [Developer Certificate of Origin](https://developercertificate.org/) - that you wrote the change or have the right to submit it. This is machine-checked: the **✍️ DCO Sign-Off** job fails any PR whose human-authored commits lack the trailer (bot PRs are exempt). Git does it for you:

  ```bash
  git commit -s -m "feat(scope): 🎯 summary"
  ```

  This appends `Signed-off-by: Your Name <you@example.com>` using your git identity. Contributions licensed inbound under the repository's [MIT License](../LICENSE).

### 2. CI/CD Gating

- Every PR triggers a CI workflow containing: Linting, Unit Tests, Build Verification, and Security Analysis.
- **Zero-Failure Policy**: All checks must be green before the review phase begins.

### 3. Review Etiquette

- Expect a maintainer review before merge (repos with a single maintainer may run on the shipped 0-approval ruleset - CI still gates every merge).
- Be responsive to feedback.
- Use standard feedback prefixes: `[BLOCKER]`, `[SUGGESTION]`, or `[NIT]`.
- See our **[Pull Requests & Code Reviews](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Pull-Requests-&-Code-Reviews.md)** rubric for the full checklist.

---

## 🤖 Automation vs. Manual

Knowing what a workflow already does for you is what keeps a contribution
small. Every row below names a file that exists in `.github/workflows/`; the
logic it calls lives in `tannergolden/standards`.

| Task                       | Handling     | Tooling                                                      |
| :------------------------- | :----------- | :----------------------------------------------------------- |
| **Lint, Test & Build**     | 🤖 Automated | `checks.yml` (required check `ci`)                           |
| **Secret Scanning**        | 🤖 Automated | `checks.yml` (required check `secrets`)                      |
| **Static Analysis**        | 🤖 Automated | `checks.yml` (CodeQL, advisory)                              |
| **Workflow Linting**       | 🤖 Automated | `checks.yml` (actionlint, zizmor)                            |
| **PR Title Validation**    | 🤖 Automated | `governance.yml`                                             |
| **DCO Sign-Off Check**     | 🤖 Automated | `governance.yml` (required check `pr`; bot PRs exempt)       |
| **PR Triage & Labeling**   | 🤖 Automated | `governance.yml`                                             |
| **Stale Issue Cleanup**    | 🤖 Automated | `governance.yml` (weekly)                                    |
| **Slash Commands**         | 🤖 Automated | `governance.yml`                                             |
| **Runner Egress Audit**    | 🤖 Automated | Harden-Runner (first step of every job)                      |
| **Code Formatting**        | 🤖 Automated | `auto-format.yml` (opens a PR, never pushes to your branch)  |
| **Dependency Updates**     | 🤖 Automated | Dependabot + `dependabot-automerge.yml` (patch & minor only) |
| **CI Failure Escalation**  | 🤖 Automated | `ci-failure-alert.yml`                                       |
| **Stub Ceiling Checks**    | 🤖 Automated | `verify-stubs.yml` (daily)                                   |
| **Branch Protection**      | 🤖 Automated | Rulesets, applied by dispatching `apply-standards.yml`       |
| **Merge Gate (green CI)**  | 🤖 Automated | Required status checks, set by those rulesets                |
| **Priority Assessment**    | 🧑‍💻 Manual    | Human Review                                                 |
| **Architectural Sign-off** | 🧑‍💻 Manual    | Code Review Approval                                         |
| **Merging to Production**  | 🧑‍💻 Manual    | Human Promotion                                              |

---

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Context-ready contributions. Predictable growth.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
