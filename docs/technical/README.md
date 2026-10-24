<!--
title: '🛠️ TECHNICAL'
description: 'How this project is built: its architecture, stack and source, one document for each part that needs one, and the designs, plans and research behind them.'
type: index
-->

<div align="center">

# 🛠️ TECHNICAL

<a name="top"></a>

**How this project is built.**

_Written down where the code cannot say it._

</div>

---

## 💡 What This Folder Is For

How this project is built: its architecture and how its parts fit, the stack it
runs on and where its source lives, and one document for each part that needs
one.

- **The architecture**: the system as it stands, its actors, building blocks,
  interfaces and trust boundaries, from the
  [Architecture Overview](../templates/technical/Architecture-Overview.md) seed.
- **The stack and the source**: what the project is built with, and where each
  part of it lives.
- **One folder per area**: `backend/`, `database/`, `infrastructure/`,
  `interface/` and `testing/`, as the fill-in standards lay them out.
- **Designs, plans and research**: `designs/`, `plans/` and `research/`, from
  the Technical Design, Implementation Plan and Research Log templates.

The fill-in standards in [`templates/technical/`](../templates/technical/README.md)
copy out to the same path here, without `templates/`:
`docs/templates/technical/backend/API-Design-Standards.md` becomes
`docs/technical/backend/API-Design-Standards.md`.

Its documents are **yours from the first commit**: nothing upstream ever
writes, moves or removes one. Only this README is ever updated from the
template, when you run 🔄 Template Sync, and its log is redrawn from the files
the folder holds.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                    | Purpose    |
| :----------------------- | :--------- |
| [`README.md`](README.md) | This file. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from each document's own
frontmatter.

---

## 🔗 See also

- [Documentation index](../README.md) - every document this project keeps
- [Template catalogue](../templates/README.md) - every seed, and where each one is copied to

---

<div align="center">

**Write down what the code cannot say.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../../LICENSE).

</div>
