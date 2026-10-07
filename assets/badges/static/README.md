<!--
title: '🏷️ STATIC BADGES'
description: 'Logs the fixed-message badges the badge kit draws into this folder: status, role, context, licence, and navigation.'
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

| File                     | Holds                                                                                               |
| :----------------------- | :-------------------------------------------------------------------------------------------------- |
| `<name>.svg`             | One per entry in `.github/badges.yml` without a gold label, named after the entry, drawn by the kit |
| [`README.md`](README.md) | This log                                                                                            |

**The badges are logged by their data file, not row by row here.** Each SVG is
drawn from one entry, and the kit deletes any SVG no entry names, so the data
file is always the exact list of what this folder holds. Add a row here only for
a file the kit did not draw.

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
