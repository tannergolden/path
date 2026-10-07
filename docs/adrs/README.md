<!--
title: '🧭 ARCHITECTURE DECISIONS'
description: 'Architecture decision records, one file per decision, each logged with its status, date and evidence.'
tags: [adr, architecture, decisions, index]
category: docs
-->

<div align="center">

# 🧭 ARCHITECTURE DECISIONS

<a name="top"></a>

**Every significant decision this project has made, and why, one record each.**

_One decision per record. One row per decision._

</div>

---

## 💡 What This Folder Is For

An architecture decision record (ADR) captures one significant decision: the
context it was made in, the options weighed, and the consequences accepted.
Every record lives in this folder, one file per decision, and the log below is
their index.

The folder is a living record, not a fill-in form, and it is **yours from the
first commit**: nothing syncs it and nothing overwrites it. It arrives with no
decisions in it and gains a row each time a record is written.

---

## 🎯 Why Decisions Are Recorded

The _why_ matters as much as the _what_. An auditable record of how the system
evolved lets every later contributor, human or AI, see the constraints and
trade-offs that shaped it before changing it.

- **Traceability**: every major architectural pivot is documented and numbered.
- **Context**: each decision is recorded with the situation it was made in.
- **Consequences**: the benefits and the technical debt are both written down.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log fields=status,date,evidence -->

| Entry                    | Status | Date | Evidence | Purpose    |
| :----------------------- | :----- | :--- | :------- | :--------- |
| [`README.md`](README.md) | -      | -    | -        | This file. |

<!-- AUTO-INDEX:END -->

**This log is the decision index, and nobody types its rows.** 🗂️ Machined
Indexes redraws it after every push from each record's own frontmatter.
**Status** is Proposed, Accepted, Superseded, or Deprecated; **Date** is when
the decision was made; **Evidence** links the research report(s) that informed
it, or reads N/A.

---

## 🌿 Adding A Decision

- [ ] Copy the [ADR template](../templates/ADR.md) into this folder as
      `ADR-NNNN-Short-Slug.md`, taking the next number.
- [ ] Set `status`, `date`, and `evidence` in its frontmatter, and write every
      section.
- [ ] Propose it in a pull request. Once merged, it is **Accepted**.

A later decision supersedes an earlier one rather than rewriting it: mark the
old record **Superseded** and link the new one.

---

## 🔗 See also

- [Documentation index](../README.md) - every document this project keeps
- [Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md) - the canonical engineering standards

---

<div align="center">

**Write the decision down while the reasons are still fresh.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
