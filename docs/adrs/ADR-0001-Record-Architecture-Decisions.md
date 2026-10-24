<!--
title: '📄 ADR-0001: RECORD ARCHITECTURE DECISIONS'
description: 'The decision to record every significant architecture decision as a numbered record in this folder, and the first example of one.'
type: record
status: 'Accepted'
date: '2026-10-24'
evidence: 'N/A'
-->

<div align="center">

# 📄 ADR-0001: RECORD ARCHITECTURE DECISIONS

<a name="top"></a>

**Every decision that shapes this project is written down, once, where the code lives.**

_The first decision is to keep the others._

</div>

---

## 📋 Meta Information

| Attribute     | Specification                                                          |
| :------------ | :--------------------------------------------------------------------- |
| **Deciders**  | The maintainers listed in [GOVERNANCE.md](../../.github/GOVERNANCE.md) |
| **Consulted** | Everyone who reviews the pull requests that implement a decision       |
| **Informed**  | Every contributor, through this folder and its log                     |

> [!NOTE]
> This record arrives with the repository, because the template made the
> decision first. Keep it as the project's own first decision, or supersede it
> if the project chooses to record decisions some other way.

---

## 🎯 Context & Problem Statement

A project's significant decisions - its architecture, its stack, the patterns
it commits to and the ones it rejects - shape every change that follows. When
they are not written down, the reasoning lives only in the heads of the people
who were there, and a later contributor, human or AI, sees what was built but
not why, or what was ruled out. They then repeat the debate, or undo the
decision without knowing what it protected.

---

## 🚦 Decision Drivers

- **Driver 1**: A contributor must be able to find why something is the way it
  is without asking the person who chose it.
- **Driver 2**: A decision must be recorded where it is reviewed, versioned and
  found: in the repository, beside the code it governs.
- **Driver 3**: Recording one must take minutes, or nobody will.

---

## 🏗️ Considered Options

1. **Option A**: Architecture decision records, one numbered file per decision
   in `docs/adrs/`, from the [ADR template](../templates/ADR.md).
2. **Option B**: Decisions recorded in issues, pull requests or a wiki.
3. **Option C**: No formal record; the code and its commit messages are the
   record.

---

## ✅ Decision Outcome

**Chosen Option**: Option A, architecture decision records in `docs/adrs/`.

### Rationale for Selection

A record in the repository is reviewed in the pull request that implements it,
versioned with the code it explains, and found by anyone who reads the tree,
which meets drivers 1 and 2. The template keeps it short and the log in this
folder's README is drawn from each record's frontmatter, so writing one is a
copy and a few paragraphs, which meets driver 3. Issues and a wiki scatter the
reasoning outside the code's history, and commit messages say what changed
rather than which alternatives were rejected.

---

## 📈 Consequence Matrix

| Category         | Impact / Consequence                                                                         |
| :--------------- | :------------------------------------------------------------------------------------------- |
| **Positive (+)** | The reasoning behind the project survives the people who made it.                            |
| **Negative (-)** | Each significant decision costs a record, and a record nobody updates can mislead.           |
| **Neutral (~)**  | A decision is never rewritten: a later one supersedes it, and both stay in the folder's log. |

---

## ⚖️ Trade-off Comparative

### Option A: Architecture decision records

- ✅ Reviewed, versioned and found with the code.
- ❌ Asks for discipline: a significant change without its record is incomplete.

### Option B: Issues, pull requests or a wiki

- ✅ No new file to write.
- ❌ The reasoning lives apart from the code: a wiki keeps a history of its own,
  and no pull request reviews a change to it.

### Option C: No formal record

- ✅ Nothing to write beyond the code and its commit messages.
- ❌ A commit message says what changed, not which alternatives were rejected,
  so the reasoning leaves with the people who held it.

---

## 🔗 Traceability & Links

- [ADR template](../templates/ADR.md) - the form every later record is copied from
- [Decision log](README.md) - every record in this folder, with its status and date

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Decide once. Write it down. Point to it forever.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../../LICENSE).

</div>
