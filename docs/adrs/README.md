<!--
title: '🧭 ARCHITECTURE DECISIONS'
description: 'Logs the folder holding the architecture decision register, and says where each record goes and how it is added.'
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

| File                                                                   | Purpose                                                                                                |
| :--------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| [`Architecture-Decision-Records.md`](Architecture-Decision-Records.md) | The register: how decisions are recorded, and the Decision Index that lists every record, newest first |
| [`README.md`](README.md)                                               | This log                                                                                               |

**The records themselves are logged in the register, not here.** Its Decision
Index already gives each one a row with its status, date, and evidence, and a
second list beside it would only drift from the first.

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
