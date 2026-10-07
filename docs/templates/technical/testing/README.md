<!--
title: '🧪 TESTING TEMPLATES'
description: 'Logs the fill-in standards for unit tests and end-to-end tests, inside the canonical testing strategy.'
tags: [templates, testing, unit-tests, e2e]
category: docs
-->

<div align="center">

# 🧪 TESTING TEMPLATES

<a name="top"></a>

**How this project proves its code works, from one function to a whole journey.**

_Fast at the bottom. Faithful at the top._

</div>

---

## 💡 What This Folder Is For

The fill-in standards for the test suite: the runner, what counts as covered,
how tests are named and isolated, and which journeys the end-to-end layer must
protect. Each decision is marked by `[square brackets]` until your project makes
it.

The binding strategy is the canonical
[Testing Strategy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Testing-Strategy.md).
These documents record your project's own conventions inside it.

Copy a file out to `docs/technical/testing/` under the same name, then replace
every bracket. The seed here stays pristine. Performance budgets are a separate
area, in [`../benchmarks/`](../benchmarks/README.md).

---

## 📝 File Log

| File                                               | Decides                                                                                                                |
| :------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| [`E2E-Testing.md`](E2E-Testing.md)                 | The automation framework, the critical user journeys, the execution environment, diagnostics, and flakiness guardrails |
| [`Unit-Test-Standards.md`](Unit-Test-Standards.md) | The test runner, coverage targets, naming and layout, Arrange-Act-Assert, isolation and mocking, and speed             |
| [`README.md`](README.md)                           | This log. It is not a seed, and is not copied out                                                                      |

Add a row here in the same change that adds a file.

---

## 🔗 See also

- [Technical templates](../README.md) - the level above, and every other area
- [Template catalogue](../../README.md) - every seed, and when to reach for it

---

<div align="center">

**A suite worth trusting is a suite someone designed.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
