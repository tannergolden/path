<!--
title: '🔌 INFRASTRUCTURE LAYER'
description: 'Logs the infrastructure layer: the adapters that implement the domain interfaces against databases, networks, and outside services.'
tags: [source, infrastructure-layer, adapters, architecture]
category: docs
-->

<div align="center">

# 🔌 INFRASTRUCTURE LAYER

<a name="top"></a>

**The adapters that connect the project to databases, networks, and outside services.**

_Implement the interface. Hide the vendor._

</div>

---

## 💡 What This Folder Is For

Persistence, transport, and every adapter to something outside the process live
here: the repository that talks to the database, the client that calls an
external API, the publisher that writes to a queue. Each implements an interface
that [`../domain/`](../domain/README.md) or [`../app/`](../app/README.md)
declares, so the rest of the code depends on the interface and never on the
vendor.

Nothing imports this layer directly except the composition root that wires it
in, which is what lets one adapter be replaced without touching a use case.

---

## 📝 File Log

| File                     | Purpose  |
| :----------------------- | :------- |
| [`README.md`](README.md) | This log |

Add a row here in the same change that adds a file. Once this folder holds more
than a screenful, log its subfolders instead and give each a README of its own.

---

<div align="center">

**Every outside dependency behind an interface the project owns.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
