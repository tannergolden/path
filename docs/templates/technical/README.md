<!--
title: '🛠️ TECHNICAL TEMPLATES'
description: 'Fill-in technical standards: the stack, source and package layout, and one folder per technical area.'
tags: [templates, technical, standards, index]
category: docs
-->

<div align="center">

# 🛠️ TECHNICAL TEMPLATES

<a name="top"></a>

**The fill-in standards that record how this project is built, one area to a folder.**

_Every bracket is a decision still waiting for you._

</div>

---

## 💡 What This Folder Is For

Everything here is a **fill-in standard**: a document whose decisions are marked
by `[square brackets]` - a bare `[REPLACE_ME]`, a choice list like
`[REST | GraphQL | gRPC]`, or a prompt like `[why]` - until your project makes
them. The three files at this level span the whole codebase. Each folder below
holds the standards for one technical area.

A copy's destination mirrors its path minus `templates/`: `Source-Code.md` here
becomes `docs/technical/Source-Code.md`, and a file in `backend/` lands in
`docs/technical/backend/`. The seed stays pristine and the copy is yours.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                            | Purpose                                                                                                              |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| [`backend/`](backend/README.md)                                  | Fill-in standards for backend services: API design, authentication and security, schemas and validation.             |
| [`benchmarks/`](benchmarks/README.md)                            | Fill-in standard for performance budgets, the methodology behind the numbers, and how each run is recorded.          |
| [`database/`](database/README.md)                                | Fill-in standards for data models and entities, and for writing, running, and rolling back schema migrations.        |
| [`infrastructure/`](infrastructure/README.md)                    | Fill-in standards for environment configuration, the delivery pipelines, and deploying and rolling back releases.    |
| [`interface/`](interface/README.md)                              | Fill-in standards for the user interface: formatting, styling and theming, and the frontend development environment. |
| [`testing/`](testing/README.md)                                  | Fill-in standards for unit tests and end-to-end tests, inside the canonical testing strategy.                        |
| [`Packages-&-Workspaces.md`](Packages-&-Workspaces.md)           | Guidelines for monorepo management and package isolation.                                                            |
| [`README.md`](README.md)                                         | This file.                                                                                                           |
| [`Source-Code.md`](Source-Code.md)                               | Architecture and standards for the application source code.                                                          |
| [`Technology-Stack-&-Tooling.md`](Technology-Stack-&-Tooling.md) | Declares the technology stack and maps it to the universal make interface.                                           |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from each template's own
frontmatter.

---

## 🔗 See also

- [Template catalogue](../README.md) - every seed, and when to reach for it
- [Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md) - the canonical guides these standards sit inside

---

<div align="center">

**Decide it once, write it down, and build to what you wrote.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
