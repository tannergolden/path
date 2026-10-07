<!--
title: '🗄️ DATABASE TEMPLATES'
description: 'Logs the fill-in standards for data models and entities, and for writing, running, and rolling back schema migrations.'
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

| File                                                     | Decides                                                                                                    |
| :------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| [`Data-Models-&-Entities.md`](Data-Models-&-Entities.md) | The persistence stack, the core entities, their relationships, indexing, and where data sits in the system |
| [`Migration-Policies.md`](Migration-Policies.md)         | How migrations are managed and run, the breaking-change protocol, seed data, and backup and recovery       |
| [`README.md`](README.md)                                 | This log. It is not a seed, and is not copied out                                                          |

Add a row here in the same change that adds a file.

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
