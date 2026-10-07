<!--
title: '🎭 END-TO-END TESTS'
description: 'Logs the end-to-end tests: whole user journeys driven against a running system, gating promotion to Preview and Release.'
tags: [testing, e2e, test-suites, quality]
category: docs
-->

<div align="center">

# 🎭 END-TO-END TESTS

<a name="top"></a>

**Whole user journeys, driven against a running system the way a user would.**

_Few journeys, none of them allowed to break._

</div>

---

## 💡 What This Folder Is For

An end-to-end test drives the running system from the outside, through a real
browser or client, across a whole journey: sign up, check out, publish. These
are the slowest and most expensive tests in the project, so they cover the few
journeys that must never break rather than every branch of the code.

The canonical
[Testing Strategy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Testing-Strategy.md)
has the smoke set gate promotion to `Preview` and `Release`. The template ships
no application, so wiring this layer to yours is a Day-0 task.

The framework, the critical journeys, the environment, diagnostics, and the
guardrails against flakiness belong in the fill-in
[E2E Testing](../../docs/templates/technical/testing/E2E-Testing.md) standard.

---

## 📝 File Log

| File                     | Purpose  |
| :----------------------- | :------- |
| [`README.md`](README.md) | This log |

Add a row here in the same change that adds a file. Once this folder holds more
than a screenful, log its subfolders instead and give each a README of its own.

---

<div align="center">

**If a user would notice it breaking, a journey here should notice first.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
