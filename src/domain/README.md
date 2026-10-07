<!--
title: '🧠 DOMAIN LAYER'
description: 'The domain layer: entities, business rules, and pure logic that import nothing outside themselves.'
tags: [source, domain-layer, business-rules, architecture]
category: docs
-->

<div align="center">

# 🧠 DOMAIN LAYER

<a name="top"></a>

**The entities and business rules that make this project what it is, with no I/O.**

_Import nothing. Depend on nothing._

</div>

---

## 💡 What This Folder Is For

The domain layer holds what would still be true if the project changed its
framework, its database, and its transport tomorrow: its entities, its business
rules, and the pure logic that applies them. No I/O happens here - no network,
no disk, no database - which also makes it the easiest code in the project to
test.

It imports nothing outside itself except the standard library. When it needs
the outside world, it declares an interface, and
[`../infra/`](../infra/README.md) implements it.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                    | Purpose    |
| :----------------------- | :--------- |
| [`README.md`](README.md) | This file. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from what each file says
about itself. A subfolder appears as one row, so give it a README of its own and
its row links to that.

---

<div align="center">

**The rules of the business, free of everything else.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
