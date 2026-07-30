<!--
title: '📄 ADR TEMPLATE'
description: 'The standard template for recording an architecture decision.'
tags: [adr, template, architecture, decisions]
category: docs
status: '[Proposed | Accepted | Superseded | Deprecated]'
date: '[YYYY-MM-DD]'
evidence: '[Commit-pinned permalink to the research report(s) that informed this, as a markdown link - or N/A]'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 📄 ADR TEMPLATE

<a name="top"></a>

**The standard template for recording an architecture decision.**

_Formalized rationale. Transparent intent. Auditable evolution._

</div>

---

> [!TIP]
> **How to use**: copy this file to `docs/adrs/ADR-NNNN-Short-Slug.md` using the next sequential number (Capitalized-Kebab, keep this template itself pristine) and fill in every section. Set `status`, `date`, and `evidence` in the frontmatter above - the [ADR index](../adrs/Architecture-Decision-Records.md) is generated from them, so there is no row to add by hand. Link the new record from the pull request that implements the decision. One decision per record; supersede rather than rewrite.

---

## 📋 Meta Information

> [!NOTE]
> **Status**, **Date**, and **Evidence** live in the frontmatter above - they feed the generated [ADR index](../adrs/Architecture-Decision-Records.md), so they are recorded once. This table records who was involved.

| Attribute     | Specification                               |
| :------------ | :------------------------------------------ |
| **Deciders**  | `[List of key stakeholders and architects]` |
| **Consulted** | `[SMEs and external reviewers]`             |
| **Informed**  | `[Affected engineering teams]`              |

---

## 🎯 Context & Problem Statement

> [!NOTE]
> Describe the technical context and the specific problem or requirement that necessitated this architectural decision. What constraints were we operating under?

---

## 🚦 Decision Drivers

- **Driver 1**: `[e.g., Scalability requirements for Peak Load]`
- **Driver 2**: `[e.g., Team familiarity with specific technology stacks]`
- **Driver 3**: `[e.g., Time-to-market constraints]`

---

## 🏗️ Considered Options

1. **Option A**: `[Description of the first architectural path]`
2. **Option B**: `[Description of the second architectural path]`
3. **Option C**: `[Description of the third architectural path]`

---

## ✅ Decision Outcome

**Chosen Option**: `[Option Name]`

### Rationale for Selection

`[Detailed explanation of why this option was selected over the alternatives, referencing the drivers above.]`

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                          |
| :--------------- | :------------------------------------------------------------ |
| **Positive (+)** | `[e.g., Improved latency, reduced operational overhead]`      |
| **Negative (-)** | `[e.g., Increased setup complexity, specific vendor lock-in]` |
| **Neutral (~)**  | `[e.g., No change to existing CI/CD pipelines]`               |

---

## ⚖️ Trade-off Comparative

### Option A: `[Name]`

- ✅ `[Pro]`
- ❌ `[Con]`

### Option B: `[Name]`

- ✅ `[Pro]`
- ❌ `[Con]`

---

## 🔗 Traceability & Links

- `[Link to relevant Issue or PR]`
- `[Link to technical documentation or RFC]`
- `[Link to parent or related ADRs]`

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**One decision. One record. Zero ambiguity.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
