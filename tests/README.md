<!--
title: '🧪 TESTS'
description: 'Logs the three test suites this project keeps, from isolated units to whole user journeys, and how CI comes to run them.'
tags: [testing, test-suites, ci, scaffold]
category: docs
-->

<div align="center">

# 🧪 TESTS

<a name="top"></a>

**The test suites, one folder for each layer of the pyramid.**

_Many fast tests. Few slow ones._

</div>

---

## 💡 What This Folder Is For

This scaffold ships without tests on purpose. Wire your framework of choice
into the `test-command` that
[`.github/workflows/checks.yml`](../.github/workflows/checks.yml) runs on every
pull request. Today that command runs the tests for `.github/scripts/`, so keep
them in it when you add your own.

The binding standard is the canonical
[Testing Strategy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Testing-Strategy.md);
the fill-in standards under `docs/templates/technical/testing/` are seeded for
your own conventions inside it.

This directory is **yours from the first commit**. Nothing here syncs, and
nothing upstream will ever write to it or delete from it - there is no sync
engine to protect it from.

---

## 📝 File Log

| Entry                                   | Put (and look for)                                                           |
| :-------------------------------------- | :--------------------------------------------------------------------------- |
| [`unit/`](unit/README.md)               | Fast, isolated tests of pure logic. Co-locating them with source is fine too |
| [`integration/`](integration/README.md) | Tests that cross a real boundary: database, filesystem, HTTP                 |
| [`e2e/`](e2e/README.md)                 | Full user-journey tests against a running system                             |
| [`README.md`](README.md)                | This log                                                                     |

Add a row here in the same change that adds a file or a folder at this level.
Each suite logs its own files.

---

<div align="center">

**Catch it at the lowest level that can catch it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
