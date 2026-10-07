<!--
title: '🗄️ DATABASE TEMPLATES'
description: 'Fill-in standards for data models and entities, and for writing, running, and rolling back schema migrations.'
tags: [templates, database, data-models, migrations]
category: docs
-->

<div align="center">

# 🗄️ DATABASE TEMPLATES

<a name="top"></a>

**How the data is shaped, and how that shape changes without losing any of it.**

_Model it once. Migrate it forward._

</div>

---

## 💡 What This Folder Is For

The fill-in standards for persistence: which store holds the data, what the
core entities are and how they relate, and the rules every change to the schema
follows. Each decision is marked by `[square brackets]` until your project makes
it.

Copy a file out to `docs/technical/database/` under the same name, then replace
every bracket. The seed here stays pristine.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                    | Purpose                                                              |
| :------------------------------------------------------- | :------------------------------------------------------------------- |
| [`Data-Models-&-Entities.md`](Data-Models-&-Entities.md) | Standards for modeling entities and their relationships.             |
| [`Migration-Policies.md`](Migration-Policies.md)         | Policies for writing, reviewing, and rolling back schema migrations. |
| [`README.md`](README.md)                                 | This file.                                                           |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from each template's own
frontmatter.

---

## 🔗 See also

- [Technical templates](../README.md) - the level above, and every other area
- [Template catalogue](../../README.md) - every seed, and when to reach for it

---

<div align="center">

**Every schema change written so it can be undone.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
