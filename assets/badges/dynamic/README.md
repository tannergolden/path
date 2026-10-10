<!--
title: '🔄 DYNAMIC BADGES'
description: 'Live badges: values the Markdown Kit measures or a workflow sets, the only ones under the gold label.'
tags: [badges, health, assets, automation]
category: docs
-->

<div align="center">

# 🔄 DYNAMIC BADGES

<a name="top"></a>

**Health badges whose colour says something true about the repository right now.**

_Gold on the label. Traffic lights on the message._

</div>

---

## 💡 What This Folder Is For

The kit writes every badge with a `measure:` here: what it measures itself on
every run, like a workflow's last run, the last commit or the latest release,
and what another workflow measures and writes with `markdown-kit set`, like a
coverage figure or a test count.

These are the only badges that may wear the **gold** label (`C0A062`), and under
it the message colour is not decoration. It is a state: **green** healthy,
**yellow** degraded, **red** failing, and **slate** for nothing measured yet.
Each run redraws them, and commits only when something they show has changed.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log exclude=*.svg -->

| Entry                    | Purpose    |
| :----------------------- | :--------- |
| [`README.md`](README.md) | This file. |

<!-- AUTO-INDEX:END -->

**The badges themselves are listed by the settings, not here.** Each SVG is
drawn from one entry with a `measure:` and named after it, and the kit deletes
any SVG no entry names. 🗂️ Machined Indexes lists everything else.

---

## 🔗 See also

- [Badges](../README.md) - both badge folders, and how to reference a badge
- [Static badges](../static/README.md) - the badges that say what their author wrote

---

<div align="center">

**A badge that reports health must be able to report ill health.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../../../LICENSE).

</div>
