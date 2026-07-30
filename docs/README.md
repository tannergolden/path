<!--
title: '📚 DOCUMENTATION'
description: 'Where this project keeps its own documents, and where the engineering standards it follows actually live.'
tags: [documentation, index, standards, templates]
category: docs
-->


<div align="center">

# 📚 DOCUMENTATION

<a name="top"></a>

**Two kinds of document, kept deliberately apart.**

_Standards are followed. Templates are filled in._

</div>

---

## 🧭 The Split

| Kind          | Where it lives                                                                                        | What you do with it        |
| :------------ | :---------------------------------------------------------------------------------------------------- | :------------------------- |
| **Standards** | [`tannergolden/standards`](https://github.com/tannergolden/standards/blob/Development/docs/README.md) | Follow by link, never copy |
| **Templates** | [`docs/templates/`](templates/README.md)                                                              | Copy out, fill in, own     |

A standard describes how every repository works: branching, reviews, releases,
secrets, hygiene. It is shared, it changes centrally, and copying it here would
only produce a stale second copy.

A template is a blank your project fills in: its architecture, its data model,
its deployment protocol. Nobody else can write those for you, which is exactly
why they ship as seed content rather than as law.

---

## 🌱 Using A Template

Copy it out of `docs/templates/` to the matching path **without** `templates/`,
then edit it until it describes your project:

```txt
docs/templates/technical/backend/API-Design-Standards.md
        ↓
docs/technical/backend/API-Design-Standards.md
```

**Anything in `[square brackets]` is yours to replace** - a bare `[REPLACE_ME]`,
a choice list like `[REST | GraphQL | gRPC]`, or a prompt like `[why]`. One
rule, because the seeds use all three forms. A file still carrying brackets
has not been adopted yet.

Nothing syncs these and nothing overwrites them. From the moment this repository
was generated they are ordinary files in your tree.

---

## 📁 This Folder As You Grow

`docs/` is where your instantiated documents go - the tree you build by copying
seeds out, not the tree they sit in. A conventional shape, none of it mandatory:

```txt
docs/
├── technical/           # architecture, backend, database, interface, testing
├── adrs/                # architecture decision records
└── operations/          # runbooks, on-call, incident response
```

Nothing belongs in it until you put something there, and `templates/` is not
copied across - the seeds stay where they are and you take what you want.

---

## 🔗 See also

- [Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md) - every canonical guide
- [Template catalogue](templates/README.md) - what each seed document is for
- [Repository README](../README.md) - setup, and how to configure CI

---

<div align="center">

**Follow the standards. Fill in the templates.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
