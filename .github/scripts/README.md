<!--
title: '🔬 REPOSITORY SCRIPTS'
description: 'The checks this repository runs on its own configuration, the tests that guard them, and which workflow runs each one.'
tags: [scripts, validation, testing, python]
category: docs
-->

<div align="center">

# 🔬 REPOSITORY SCRIPTS

<a name="top"></a>

**The checks a new repository runs before it has any code of its own.**

_The first gates you have, every one under test._

</div>

---

## 💡 What This Folder Is For

A new repository has no source code to lint, but it already has configuration
that decides how it behaves: workflows, Dependabot, forms, editor settings. A
typo in any of them breaks something quietly. The scripts here check those files
from the first commit, and the tests beside them check the scripts.

They live under `.github/` so the root of the repository stays yours. Each needs
only Python 3, plus PyYAML for the ones that read YAML.

---

## 📝 File Log

| File                                                           | Run by                                         | Does                                                                                                                                                     |
| :------------------------------------------------------------- | :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`validate-repository.py`](validate-repository.py)             | `checks.yml`, as the `ci` job's `lint-command` | Checks what nothing else parses: YAML and JSON load, every workflow `uses:` is pinned to a tag or a commit, and text is UTF-8, LF, and ends in a newline |
| [`verify-stub-ceilings.py`](verify-stub-ceilings.py)           | `verify-stubs.yml`                             | Compares each stub's `permissions:` ceiling and inputs with the workflow it calls, at `v1` and at the standards' default branch                          |
| [`test_gitignore.py`](test_gitignore.py)                       | `checks.yml`, as the `ci` job's `test-command` | Runs the real `.gitignore` through `git check-ignore`: source directories survive, secrets and build output do not                                       |
| [`test_validate_repository.py`](test_validate_repository.py)   | `checks.yml`, as the `ci` job's `test-command` | Runs the validator against throwaway repositories and checks what it reports                                                                             |
| [`test_verify_stub_ceilings.py`](test_verify_stub_ceilings.py) | `checks.yml`, as the `ci` job's `test-command` | Tests the permission arithmetic the ceiling check depends on                                                                                             |
| [`README.md`](README.md)                                       | -                                              | This log                                                                                                                                                 |

Add a row here in the same change that adds a script. The `test-command`
discovers every `test_*.py` in this folder, so a test added beside a new script
runs without anyone remembering to list it.

> [!NOTE]
> **The tests keep their underscores on purpose.** `unittest` imports each
> `test_*.py` as a module, and a module name cannot contain a hyphen, which is
> the one exception the naming standard allows. The scripts are run as files,
> so their names are hyphenated like everything else.

---

## 🚀 Running Them Locally

From the root of the repository:

```bash
python3 .github/scripts/validate-repository.py
python3 -m unittest discover -s .github/scripts -p 'test_*.py'
```

`verify-stub-ceilings.py` also needs the standards checked out at `v1` in
`.standards/`, which `verify-stubs.yml` does before it runs it.

Once `lint-command` points at your project's real linter, the validator can stay
as a second gate or go. What it checks stays true either way.

---

<div align="center">

**Configuration checked from the first commit, and the checkers checked too.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../../LICENSE).

</div>
