<!--
title: '▶️ EXAMPLES'
description: 'Runnable examples that show how to use this project, one per task, built and checked with the code they show.'
type: index
-->

<div align="center">

# ▶️ EXAMPLES

<a name="top"></a>

**How to use this project, shown in code that runs.**

_Small enough to read. Complete enough to run._

</div>

---

## 💡 What This Folder Is For

Reserved, and holding nothing but this log until the project has someone to
show how to use it: a library's callers, a command-line tool's operators, an
API's clients. When it does, each example goes here, one file or folder per
task, small enough to read in one sitting and complete enough to run as it
stands.

An example is code, so it runs with the project's own commands. Make sure the
commands the `ci` job in
[`.github/workflows/checks.yml`](../.github/workflows/checks.yml) runs also
build the examples, so one that stops working fails a pull request before it
fails a reader. Some toolchains already look here by name: Cargo, for one,
finds every example in `examples/` without being told.

What is not an example lives elsewhere: a test that proves behaviour in
[`tests/`](../tests/README.md), a step-by-step guide in
[`docs/library/`](../docs/library/README.md), and a page that opens in a
browser in [`assets/html/`](../assets/html/README.md).

This directory is **yours from the first commit**. Nothing upstream will ever
write to it or delete from it.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                    | Purpose    |
| :----------------------- | :--------- |
| [`README.md`](README.md) | This file. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch,
from what each example says about itself: open each file with a comment saying
what it shows, and give each folder a README of its own.

---

<div align="center">

**An example that does not run teaches the wrong thing.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
