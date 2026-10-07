<!--
title: '🧩 UNIT TESTS'
description: 'Logs the unit tests: fast, isolated checks of one piece of logic each, run on every push.'
tags: [testing, unit-tests, test-suites, quality]
category: docs
-->

<div align="center">

# 🧩 UNIT TESTS

<a name="top"></a>

**Fast, isolated tests of one piece of logic each, run on every push.**

_In-process, and no I/O._

</div>

---

## 💡 What This Folder Is For

A unit test proves that one function or module behaves as designed, in process,
with anything that would do I/O replaced by a test double. Unit tests are the
bulk of the suite because they are cheap enough to run on every push, and the
domain layer, which does no I/O, is where most of them point.

Co-locating them next to the source they test is fine too, if your language
prefers it. This folder is the home for the ones that are not.

The runner, coverage targets, naming, test layout, and mocking rules belong in
the fill-in [Unit Test Standards](../../docs/templates/technical/testing/Unit-Test-Standards.md).

---

## 📝 File Log

| File                     | Purpose  |
| :----------------------- | :------- |
| [`README.md`](README.md) | This log |

Add a row here in the same change that adds a file. Once this folder holds more
than a screenful, log its subfolders instead and give each a README of its own.

---

<div align="center">

**One behaviour per test, proven in milliseconds.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
