<!--
title: '📝 ARCHITECTURE DECISION RECORDS'
description: 'How architecture decisions are recorded, plus the index of accepted records.'
tags: [adr, architecture, decisions, index]
category: docs
index: true # pins this page to the top of its sidebar folder
-->

<!-- A per-repository living record, not canonical law. This arrives with the scaffold and is yours from the first commit: nothing syncs it and nothing overwrites it. The decision table starts empty and grows as you add ADRs from docs/templates/ADR.md. -->
<div align="center">

# 📝 ARCHITECTURE DECISION RECORDS

<a name="top"></a>

**How architecture decisions are recorded, plus the index of accepted records.**

_Traceable decisions. Immutable rationale. Engineering historical record._

</div>

---

## 🎯 Our Decision Philosophy

We believe that the "Why" is as important as the "What". Our goal is to maintain a transparent and auditable record of our technical evolution, ensuring that future contributors (human and AI) understand the constraints and trade-offs that shaped the system.

- **Traceability**: Every major architectural pivot is documented and numbered.
- **Context**: Decisions are recorded with the historical context in which they were made.
- **Consequences**: We explicitly document both the benefits and the technical debt incurred.

---

## 🟢 The Decision Index

Copy the [ADR template](../templates/ADR.md) to `docs/adrs/ADR-NNNN-Short-Slug.md`, set its frontmatter (`status`, `date`, `evidence`), and its row appears below on the next push, newest decision first.

> [!NOTE]
> **The table is generated, never typed.** 🗂️ Machined Indexes redraws it
> after every push from each record's own frontmatter, newest decision first,
> so a record cannot land without its row. Keep `status`, `date` and
> `evidence` current in the record itself.

Read a row in four moves: **Decision** links the record (its number and title); **Status** is Proposed, Accepted, Superseded, or Deprecated; **Date** is when it was decided; **Evidence** is the research report(s) that informed it, or `-`.

<!-- AUTO-INDEX:BEGIN dir=. style=records fields=status,date,evidence headers=Decision,Status,Date,Evidence sort=date:desc -->

| Decision   | Status | Date | Evidence |
| :--------- | :----- | :--- | :------- |
| _none yet_ | -      | -    | -        |

<!-- AUTO-INDEX:END -->

---

## 🛠️ ADR Lifecycle

> [!TIP]
> Architecture decisions should be proposed via PR. Once merged, the ADR is considered **Accepted**. If a decision is superseded by a later ADR, the status should be updated to **Deprecated** or **Superseded**.

### 🔗 See also

> [!TIP]
> This project's own documents are indexed in the [&#x1F4DA; Documentation index](../README.md); the canonical engineering standards live in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).

---

<div align="center">

**Decided for integrity. Documented for scale.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
