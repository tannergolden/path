<!--
This template becomes the body of your pull request. Fill in every section
(empty descriptions are closed); delete a line that truly does not apply or
mark it N/A.
- Title: Conventional Commit - <type>(<scope>): summary. The squash commit
  inherits it and feeds the changelog, so make it accurate.
- Branch: a short-lived <type>/<topic> (feat/*, fix/*, docs/*) into Development.
- Scope: one intent. Aim for under 300 lines and 10 files; the size labeler
  tags `size: large` past 200 changed lines and `size: extra large` past 500.
- Open as a Draft for early feedback; mark Ready for Review once CI is green.
- Never paste secrets into code, logs, or screenshots.
-->

## 📝 Summary

- **What changed** (2-4 sentences):
- **Why** (the problem it solves; link the issue / ADR / discussion):

## 🎯 Type

- [ ] ✨ Feature
- [ ] 🐞 Bug fix
- [ ] ♻️ Refactor
- [ ] ⚡️ Performance
- [ ] 🔒 Security
- [ ] 🧪 Tests only
- [ ] 📚 Docs
- [ ] ⚙️ Build / CI
- [ ] 🧹 Chore / Maintenance
- [ ] 💥 Breaking change <!-- if checked, complete Risk & Rollback below -->

## 🔗 Linked issues

- Closes #
- Refs #

## ✅ Validation

- [ ] Local gates green: this project's own lint, test, and build commands (the ones `.github/workflows/checks.yml` runs)
- **Tests** (required for behavior changes; say what each new test pins down, and add a regression test for bug fixes):
- **Coverage**: [ ] Unit · [ ] Integration · [ ] E2E · [ ] N/A
- **Manual steps** a reviewer can follow to reproduce the result:
  1. [step]
  2. [step]
- **Evidence** for UI or behavior changes (before -> after screenshots, recordings, or logs; redact secrets; add alt text on images):

## 💥 Risk & Rollback

- **Blast radius / breaking impact** (migration steps if any):
- **Risk level**: Low / Medium / High
- **Rollback plan** (revert PR, disable flag, restore config):

## 🧭 Rollout _(if applicable)_

- **Feature flag** (name + default):
- **Dependencies** (linked PRs, migrations, config toggles):

## 📚 Docs & release notes

- [ ] Docs updated (link) or N/A:
- **Release note** (one user-facing sentence):

## ✅ Author checklist

- [ ] One intent, sized for review (explain if the labeler tags it `size: large` or bigger)
- [ ] Conventional Commit **title**, and commits **signed off** for DCO (`git commit -s`)
- [ ] Local gates green (lint, test, build)
- [ ] Tests added or updated for logic changes; documented above
- [ ] No secrets committed; scanner alerts resolved
- [ ] Docs updated when behavior or setup changed
- [ ] Any AI-assisted work followed this project's agent instructions, if it has any
- [ ] Targeting `Development`; ready to **squash merge** on green CI

<!--
Reviewer rubric (see docs/distribution/Pull-Requests-&-Code-Reviews.md):
- Blocking: Correctness (edge cases + requirement met), Security (secrets,
  least privilege), Testability (coverage matches intent).
- High: Readability. Medium: Parity with established patterns.
- Merge needs 🧪 Lint, Test & Build, 🔍 Scan for Secrets, and ✍️ DCO Sign-Off green.
- Tag feedback by intent: [BLOCKER] / [SUGGESTION] / [NIT] / [QUESTION].
-->

<!-- Keep the lines below exactly as-is for GitHub to credit co-authors. -->
<!--
Co-authored-by: Name <email@example.com>
-->
