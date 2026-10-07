<!--
title: '🧭 ARCHITECTURE DECISIONS'
description: 'The architecture decision register, and the records it lists.'
tags: [adr, architecture, decisions, index]
category: docs
-->

<div align="center">

# 🧭 ARCHITECTURE DECISIONS

<a name="top"></a>

**The home of the decision register, and the rule for adding a record to it.**

_One decision per record. One row per decision._

</div>

---

## 💡 What This Folder Is For

An architecture decision record (ADR) captures one significant decision: the
context it was made in, the options weighed, and the consequences accepted.
This folder holds the **register** that lists every one of them.

The register is a living record, not a fill-in form. It arrives with no
decisions in it and gains one row each time a record is written. Records go to
`docs/adrs/`, the path the register and the ADR template both name, one file
per decision.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                                  | Purpose                                                                      |
| :--------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| [`Architecture-Decision-Records.md`](Architecture-Decision-Records.md) | How architecture decisions are recorded, plus the index of accepted records. |
| [`README.md`](README.md)                                               | This file.                                                                   |

<!-- AUTO-INDEX:END -->

**A record added to this folder needs no row typed by hand.** It appears in this
log and in the register's Decision Index on the next push, both drawn by 🗂️
Machined Indexes, the register's from the record's own frontmatter.

---

## 🌿 Adding A Decision

- [ ] Copy the [ADR template](../templates/ADR.md) to
      `docs/adrs/ADR-NNNN-Short-Slug.md`, taking the next number.
- [ ] Set `status`, `date`, and `evidence` in its frontmatter, and write every
      section.
- [ ] Add its row to the top of the register's Decision Index.
- [ ] Propose it in a pull request. Once merged, it is **Accepted**.

A later decision supersedes an earlier one rather than rewriting it: mark the
old record **Superseded** and link the new one.

---

<div align="center">

**Write the decision down while the reasons are still fresh.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
