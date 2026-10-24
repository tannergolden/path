<!--
title: '🚀 APPLICATION LAYER'
description: 'The application layer: entry points and use cases that orchestrate the domain and receive infrastructure through injection.'
type: index
-->

<div align="center">

# 🚀 APPLICATION LAYER

<a name="top"></a>

**Entry points and use cases: the code that turns a request into domain work.**

_Orchestrate here. Decide in the domain._

</div>

---

## 💡 What This Folder Is For

The application layer is where the project starts and where each use case is
carried out: a command, a request handler, a scheduled job. It calls into
[`../domain/`](../domain/README.md) for every rule, and receives what it needs
from [`../infra/`](../infra/README.md) through injection, so swapping a database
or a transport never means rewriting a use case.

It may import `domain`. It never imports `infra` directly, except in the
composition root that wires the two together at startup.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                    | Purpose    |
| :----------------------- | :--------- |
| [`README.md`](README.md) | This file. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch,
from what each file says about itself. A subfolder appears as one row, so give
it a README of its own and its row links to that.

---

<div align="center">

**Thin use cases over a thick domain.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
