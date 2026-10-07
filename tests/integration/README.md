<!--
title: '🔗 INTEGRATION TESTS'
description: 'Integration tests: checks that cross a real boundary such as a database, the filesystem, or an HTTP service.'
tags: [testing, integration-tests, test-suites, quality]
category: docs
-->

<div align="center">

# 🔗 INTEGRATION TESTS

<a name="top"></a>

**Tests that cross a real boundary, proving the adapters against the real thing.**

_One real boundary per test._

</div>

---

## 💡 What This Folder Is For

An integration test exercises the code where it meets something outside the
process: a database, the filesystem, an HTTP service. These are the tests that
prove the adapters in `src/infra/` work, which no amount of mocking in a unit
test can.

They run on every push, like the unit tests, against local emulators or
containers rather than a shared environment, so a run on a laptop and a run in
CI meet the same dependencies. Keep each test to one boundary, so a failure
names the thing that broke.

The canonical
[Testing Strategy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Testing-Strategy.md)
sets where this layer sits and when it runs.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                    | Purpose    |
| :----------------------- | :--------- |
| [`README.md`](README.md) | This file. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from what each file says
about itself. A subfolder appears as one row, so give it a README of its own and
its row links to that.

---

<div align="center">

**Mock the world in a unit test. Meet it here.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
