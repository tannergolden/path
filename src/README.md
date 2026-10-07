<!--
title: '💻 APPLICATION SOURCE'
description: 'Logs the three layers the application source is split into, and the rule that keeps their dependencies pointing inward.'
tags: [source, architecture, layers, scaffold]
category: docs
-->

<div align="center">

# 💻 APPLICATION SOURCE

<a name="top"></a>

**Where the application starts: a layout imposed, and the stack left to you.**

_Dependencies point inward._

</div>

---

## 💡 What This Folder Is For

This scaffold ships without code on purpose: the template imposes a layout, not
a stack. The three layers below keep what the project **is** apart from how it is
delivered and what it talks to, so the core logic never depends on a framework
or a database.

This directory is **yours from the first commit**. Nothing here syncs, and
nothing upstream will ever write to it or delete from it - there is no sync
engine to protect it from.

---

## 📝 File Log

| Entry                         | Put (and look for)                                                        |
| :---------------------------- | :------------------------------------------------------------------------ |
| [`app/`](app/README.md)       | The application layer: entry points, use cases, orchestration             |
| [`domain/`](domain/README.md) | The domain layer: entities, business rules, pure logic with no I/O        |
| [`infra/`](infra/README.md)   | The infrastructure layer: persistence, transport, adapters to the outside |
| [`README.md`](README.md)      | This log                                                                  |

Add a row here in the same change that adds a file or a folder at this level.
Each layer logs its own files.

---

## 🧱 The One Rule Between Them

Dependencies point inward. `domain` imports nothing outside itself, `app`
orchestrates the domain and receives `infra` through injection, and `infra`
implements interfaces the other two declare. Only a composition root imports
`infra` directly.

The full rules, and the stack this is written in, belong in the fill-in
[Source Code](../docs/templates/technical/Source-Code.md) and
[Technology Stack & Tooling](../docs/templates/technical/Technology-Stack-&-Tooling.md)
standards, seeded under `docs/templates/technical/` for you to instantiate with
your decisions.

---

<div align="center">

**The domain at the centre, and everything else pointing at it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
