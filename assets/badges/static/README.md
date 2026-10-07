<!--
title: '🏷️ STATIC BADGES'
description: 'Fixed-message badges the badge kit draws: status, role, context, licence, and navigation.'
tags: [badges, identity, assets, automation]
category: docs
-->

<div align="center">

# 🏷️ STATIC BADGES

<a name="top"></a>

**Fixed badges that name what a document is, rather than report how something is doing.**

_Identity, drawn once._

</div>

---

## 💡 What This Folder Is For

The badge kit writes every badge whose label is **not** gold here: the identity
row a header carries (status, role, context, licence) and any navigation badge
that links somewhere. Their message never changes on its own, so their colours
are free, apart from the meanings the standards fix: a role is pink, a context
purple, a licence yellow.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log exclude=*.svg -->

| Entry                    | Purpose    |
| :----------------------- | :--------- |
| [`README.md`](README.md) | This file. |

<!-- AUTO-INDEX:END -->

**The badges themselves are logged by their data file, not here.** Each SVG is
drawn from one entry in `.github/badges.yml` without a gold label and named
after it, and the kit deletes any SVG no entry names, so the data file is always
the exact list. 🗂️ Machined Indexes redraws this log after every push and lists
everything else.

---

## 🔗 See also

- [Badges](../README.md) - both badge folders, and how to reference a badge
- [Dynamic badges](../dynamic/README.md) - the gold labels, and the colours they may use

---

<div align="center">

**A badge earns its place by saying what the title cannot.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
