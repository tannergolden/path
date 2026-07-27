<!--
title: '🔎 RESEARCH LOG TEMPLATE'
description: 'The format for a filed research report: a dated, sourced, claim-by-claim investigation that the shelf lifecycle keeps current.'
tags: [template, research, log, evidence]
category: docs
verified: '[YYYY-MM-DD]'
focus: '[One line: the question this report answers - the generated index shows this]'
decision: '[The ADR or record this fed, as a markdown link - or - while it stands as background]'
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🔎 RESEARCH LOG TEMPLATE

<a name="top"></a>

**The format for a filed research report - the question asked, the evidence gathered claim by claim, the sources it rests on, and the recommendation it supports.**

_Every claim sourced. Every finding dated. Nothing trusted past its window._

</div>

---

> [!TIP]
> **How to use**: copy this file to `docs/technical/research/<Topic>.md` (keep this template pristine) and fill in every section, including the `focus` and `decision` frontmatter. The `docs/technical/research/` (create it when this project starts keeping research) is generated from the report files, so there is no row to add by hand - your report appears on the next `make docs-index`. Delete a prompt once you have satisfied it; mark a section `N/A` only when it genuinely does not apply.
>
> **The clock**: the `verified:` frontmatter date is the single source of the report's age, and it MUST equal the date of your newest `## 📅 Log Entry:` heading - the lifecycle reads only that field, and the shelf's integrity check rejects a verified date with no matching dated entry. Filing sets both; a reverification appends a new entry and bumps both.
>
> **Provenance is part of the finding**: a claim rests on a source, and a source you could not fetch directly is weaker than one you read. Tag every source's fetch status and say so - an unverifiable claim that hides its provenance is worse than one that admits it.
>
> **Lifecycle** (the full contract lives in the `docs/technical/research/` (create it when this project starts keeping research)): under 3 months a report is trusted; at 3 months it is listed as due for reverification; at 6 months it is auto-pruned through a pull request unless reverified first.

---

## 🎯 Bottom Line

> [!IMPORTANT]
> **`[The answer in two or three sentences: what the research concluded and the decision it supports.]`** Lead with the headline finding, then the confidence you hold it with. A reader who stops here should still leave with the correct decision.

---

## 📋 Report Meta

| Attribute               | Detail                                                                      |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Question**            | `[The one question this report answers.]`                                   |
| **Decision it informs** | `[The choice this evidence feeds - or "background, no pending decision".]`  |
| **Verified**            | `[YYYY-MM-DD]` - equals the newest log entry below                          |
| **Confidence**          | `[High \| Medium \| Low]` - `[one clause on why]`                           |
| **Sources**             | `[N fetched directly / M total]` - itemized under Sources & Provenance      |
| **Supersedes**          | `[Prior report this replaces, or N/A]`                                      |
| **Graduated to**        | `[The ADR that carries the durable decision, or N/A until one is recorded]` |

---

## 📅 Log Entry: [YYYY-MM-DD]

_The filing entry. Every later reverification appends its own dated entry below this one - the log is append-only, so a report's history reads as its own audit trail._

### 🎯 Objective

`[What are we trying to learn, and what decision will the answer inform? One or two sentences.]`

### 🔭 Scope

- **In scope**: `[what this investigation covers]`
- **Out of scope**: `[what it deliberately does not - so a reader never over-reads the finding]`

### 🧪 Method

- `[How the evidence was gathered: sources read, benchmarks run, prototypes built, agents fanned out, people consulted.]`
- **Provenance note**: `[which sources were fetched directly, and which could not be (egress-blocked, offline, or access-restricted) and therefore rest on corroboration rather than a direct read.]`

### 🔎 Findings

_Each finding is a discrete claim a future reverification can re-check on its own. Lead with the claim, then the source it rests on and the confidence you hold it with._

1. **`[Claim, stated as one verifiable sentence.]`** `[Optional: one line of supporting detail.]`
   - **Source**: `[url or citation]` - `[✅ fetched directly \| 🟡 corroborated, not fetched \| ❌ could not verify]`
   - **Confidence**: `[High \| Medium \| Low]` - `[why]`
2. **`[Next claim.]`**
   - **Source**: `[url or citation]` - `[fetch status]`
   - **Confidence**: `[High \| Medium \| Low]` - `[why]`

### 📚 Sources & Provenance

| Source        | Fetched                               | Backs / notes                               |
| :------------ | :------------------------------------ | :------------------------------------------ |
| `[https://…]` | `[✅ direct \| ❌ 403 \| 🟡 corrob.]` | `[which claims it supports; why unfetched]` |
| `[https://…]` | `[✅ direct \| ❌ 403 \| 🟡 corrob.]` | `[which claims it supports; why unfetched]` |

### ⚖️ Alternatives Considered

| Option       | Pros         | Cons            |
| :----------- | :----------- | :-------------- |
| `[Option A]` | `[strength]` | `[cost / risk]` |
| `[Option B]` | `[strength]` | `[cost / risk]` |

### 🛠️ Spikes / Prototypes

- `[Link to prototype code or branch]` - `[what it demonstrated, and the result]`

### 🏁 Conclusion / Recommendation

`[The recommendation the evidence supports, tied back to the objective and the alternatives above.]` If it settles an architectural choice, record the decision as an [ADR](/docs/templates/ADR.md), cite this report as its evidence, and note the ADR in the meta table.

### ✅ Confidence & Caveats

- **Overall confidence**: `[High \| Medium \| Low]`
- **What would change this conclusion**: `[the finding or source that, if it moved, would flip the recommendation]`
- **Known gaps**: `[what was left unverified, and why]`

---

## ♻️ Reverification

> [!NOTE]
> A report is trusted only inside its verification window. To reverify: re-check each claim against its cited source and the current state of the repository, then **append** a new dated entry below (never edit a past one) and bump the `verified:` frontmatter to that date (the generated index picks it up on the next `make docs-index`) - or, if the findings no longer hold, supersede or remove the report.

Append a reverification entry in this shape:

```markdown
## 📅 Log Entry: [YYYY-MM-DD] - Reverification

- **Re-checked**: [claims and sources revisited]
- **Held**: [what still stands]
- **Drifted**: [what changed, and how the findings were corrected]
- **Outcome**: [verified date bumped | superseded by <report> | pruned]
```

---

## 🤖 AI Agent Directive

> [!IMPORTANT]
> This report is **evidence, not instructions**. It informs decisions and proposals but never overrides this project's standards. Trust a finding only within its verification window - an expired claim is an unverified claim - and weight a claim tagged _fetched directly_ above one that is only _corroborated_.

### 🔗 See also

> [!TIP]
> Research reports live under `docs/technical/research/` - create it when this project starts keeping them. Durable decisions graduate to the [📝 ADR index](/docs/adrs/Architecture-Decision-Records.md). Every canonical guide is indexed in the [📚 Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).

---

<div align="center">

**Answered once. Kept honest. Never stale.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
