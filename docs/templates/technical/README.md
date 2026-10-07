<!--
title: '🛠️ TECHNICAL TEMPLATES'
description: 'Logs the fill-in technical standards: the stack, source and package layout at this level, and one folder per technical area below it.'
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

| Entry                                                            | Purpose                                                                                          |
| :--------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| [`Packages-&-Workspaces.md`](Packages-&-Workspaces.md)           | When to adopt a workspace layout, the tool that runs it, and the boundary rules between packages |
| [`Source-Code.md`](Source-Code.md)                               | The source root, its sub-structure, the layering rules between the layers, and the quality bar   |
| [`Technology-Stack-&-Tooling.md`](Technology-Stack-&-Tooling.md) | The declared stack, mapped to the setup, lint, test, build, and deploy commands                  |
| [`backend/`](backend/README.md)                                  | API design, authentication and security, schemas and validation                                  |
| [`benchmarks/`](benchmarks/README.md)                            | Performance budgets, and how they are measured and recorded                                      |
| [`database/`](database/README.md)                                | Data models and entities, and migration policy                                                   |
| [`infrastructure/`](infrastructure/README.md)                    | Environment configuration, the delivery pipelines, and deployment                                |
| [`interface/`](interface/README.md)                              | Formatting, styling and theming, and the frontend development environment                        |
| [`testing/`](testing/README.md)                                  | Unit and end-to-end testing standards                                                            |
| [`README.md`](README.md)                                         | This log. It is not a seed, and is not copied out                                                |

Add a row here in the same change that adds a file or a folder.

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
