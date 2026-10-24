<!--
title: '📚 DOCUMENTATION'
description: 'Where this project keeps its own documents, and where the engineering standards it follows actually live.'
type: index
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

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                     | Purpose                                                                                                                                                     |
| :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`adrs/`](adrs/README.md)                 | Architecture decision records, one file per decision, each logged with its status, date and evidence.                                                       |
| [`distribution/`](distribution/README.md) | From a branch to a release: how a change moves through this project and how a release reaches its users, wherever this project adds to the shared workflow. |
| [`introduction/`](introduction/README.md) | Where to start: what this project is and how its parts fit together, the principles it holds to, how to get ready to work on it, and where it is going.     |
| [`library/`](library/README.md)           | What to learn, and where: guides, background and further reading for anyone new to this project's domain or its tools.                                      |
| [`operations/`](operations/README.md)     | Keeping this project healthy and safe once it runs: runbooks, incident response, post-mortems, security, and the risks it still carries.                    |
| [`references/`](references/README.md)     | Things to look up: the glossary, catalogues, settings and formats, the pages this project consults rather than reads through.                               |
| [`technical/`](technical/README.md)       | How this project is built: its architecture, stack and source, one document for each part that needs one, and the designs, plans and research behind them.  |
| [`templates/`](templates/README.md)       | Index of the reusable document templates and when to use each one.                                                                                          |
| [`README.md`](README.md)                  | This file.                                                                                                                                                  |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push. Every folder below this
one carries a `README.md` that logs the files inside it, so the tree reads one
level at a time.

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

Whenever you run 🔄 Template Sync, it brings the seeds themselves up to date: each
improvement arrives as a pull request that overwrites a seed you had not changed
with the template's version, and merges one you had with your changes.
It never touches a document you copied out - from the moment you make it, that
copy is an ordinary file in your tree. Put a `#` in front of a seed's line in `.github/template-sync`
to keep that seed exactly as it is.

---

## 📁 The Seven Folders

`docs/` is where your own documents go: the pages you write and the seeds you
copy out, not the tree the seeds sit in. It arrives in the same seven folders
as the standards' own documentation, so every repository on the standards
reads the same way:

```bash
docs/
├── introduction/        # where to start: overview, principles, setup, roadmap
├── distribution/        # from a branch to a release: releasing, delivery
├── technical/           # how it is built: architecture, source, designs, plans
├── operations/          # keeping it healthy and safe: runbooks, post-mortems
├── references/          # things to look up: glossary, catalogues, formats
├── library/             # what to learn: guides, background, further reading
├── adrs/                # architecture decision records
└── templates/           # the seeds, copied out into the folders above
```

Each folder arrives empty but for a `README.md` that says what belongs in it
and logs its files. Put each document you write in the folder its kind names,
and add folders below them as you grow: give each one a `README.md` that logs
its files, the way every seeded folder does, and update it in the same change
that adds a file. `templates/` is not copied across: the seeds stay where they
are and you take what you want.

**Use these folders unless your project needs its own.** They fit any project,
which is why the standards use the same seven. If yours keeps its documents
another way - a notes vault whose folders are its documents, say - keep that
way, and add `!/docs/**` under **Your rules** in `.github/template-sync`. Every
README in these folders is kept current, so 🔄 Template Sync would otherwise
overwrite any of them you put to a different use the next time you run it.

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
