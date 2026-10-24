<!--
title: '🪝 GIT HOOKS'
description: 'The git hooks this repository ships, what each catches before a commit is recorded, and how to switch them on.'
type: index
-->

<div align="center">

# 🪝 GIT HOOKS

<a name="top"></a>

**The mistakes a pull request would reject, caught before the commit exists.**

_Checked locally. Enforced in CI._

</div>

---

## 💡 What This Folder Is For

Every pull request runs the canonical checks: a Conventional Commit for each
message, a `Signed-off-by:` trailer for the DCO, and a scan for secrets. They
run after a push, though, and a commit that fails them has to be rewritten.
These hooks run the same checks on your machine, at the moment of committing,
when fixing the mistake costs nothing.

**CI stays the authority.** A hook can be skipped with `--no-verify` or never
switched on, and the checks in the pull request still run either way. The
hooks follow the rules in the standards; where they disagree, the standards
win.

---

## 🚀 Switching Them On

Git runs hooks from `.git/hooks/` unless told otherwise, and that folder is not
part of the repository. Point git at this one, once per clone:

```bash
git config core.hooksPath .github/scripts/hooks
```

The [development container](../../../.devcontainer/README.md) runs that for
you when it is created. `pre-commit` scans only when
[gitleaks](https://github.com/gitleaks/gitleaks) is installed, and says so when
it is not.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                      | Purpose                                                                                                                                         |
| :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| [`commit-msg`](commit-msg) | Checks a commit message before git records it: a Conventional Commit header with a scope, and the Signed-off-by trailer the DCO check requires. |
| [`pre-commit`](pre-commit) | Scans what is staged for secrets before git records it, with gitleaks when it is installed.                                                     |
| [`README.md`](README.md)   | This file.                                                                                                                                      |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from the comment each
hook opens with.

---

<div align="center">

**A failed check costs least before the commit exists.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../../../LICENSE).

</div>
