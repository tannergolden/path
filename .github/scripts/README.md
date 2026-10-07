<!--
title: '🔬 REPOSITORY SCRIPTS'
description: 'The checks this repository runs on its own configuration, and the tests that guard them.'
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

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                          | Purpose                                                              |
| :------------------------------------------------------------- | :------------------------------------------------------------------- |
| [`README.md`](README.md)                                       | This file.                                                           |
| [`test_gitignore.py`](test_gitignore.py)                       | Tests for this repository's .gitignore.                              |
| [`test_validate_repository.py`](test_validate_repository.py)   | Tests for the repository validator.                                  |
| [`test_verify_stub_ceilings.py`](test_verify_stub_ceilings.py) | Tests for the stub ceiling checker.                                  |
| [`validate-repository.py`](validate-repository.py)             | Validate this repository's own configuration.                        |
| [`verify-stub-ceilings.py`](verify-stub-ceilings.py)           | Check every stub's permission ceiling against the workflow it calls. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from each docstring. Who
runs them:

- `checks.yml` runs `validate-repository.py` as the `ci` job's `lint-command`,
  and every `test_*.py` here as its `test-command`. That discovers a test
  added beside a new script without anyone remembering to list it.
- `verify-stubs.yml` runs `verify-stub-ceilings.py`.

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
