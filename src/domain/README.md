<!--
title: '🧠 DOMAIN LAYER'
description: 'Logs the domain layer: the entities, business rules, and pure logic that import nothing outside themselves.'
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

| File                     | Purpose  |
| :----------------------- | :------- |
| [`README.md`](README.md) | This log |

Add a row here in the same change that adds a file. Once this folder holds more
than a screenful, log its subfolders instead and give each a README of its own.

---

<div align="center">

**The rules of the business, free of everything else.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
