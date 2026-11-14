<!--
title: '🔎 RESEARCH'
description: 'Every research report filed in this project: one per question, written from the Research Log template, sourced claim by claim, and trusted for three months from the date it was last verified.'
type: index
-->

<div align="center">

# 🔎 RESEARCH

<a name="top"></a>

**The evidence behind this project's decisions, filed where the next question can find it.**

_Every claim sourced. Every report dated._

</div>

---

## 💡 What This Folder Is For

Every research request ends here. When someone asks an agent to research, look
into, compare or find out about anything, the work is done only when its report
is filed in this folder, as `AGENTS.md` says. Each report answers one question
in the shape of the [Research Log](../../templates/Research-Log.md) template:
the bottom line, the findings claim by claim with the source each rests on and
how it was fetched, and the decision it fed.

- **One file per question**, named for its topic, such as `Message-Queues.md`.
  A second look at the same question goes into the same file as a new dated log
  entry, never into a second report.
- **Trusted for three months** from its `verified` date. After that a report is
  stale: before anything relies on it, reverify its claims and move the date, or
  replace it with a new research pass. 🔎 Research Freshness opens an issue
  every Monday listing each report past its window, or with no date at all.
- **Durable conclusions graduate.** A finding that must outlive the window
  becomes a decision in [`adrs/`](../../adrs/README.md), and the report's
  **Graduated to** row links it.

Its reports are **yours from the first commit**: nothing upstream ever writes,
moves or removes one. Only this README is ever updated from the template, when
you run 🔄 Template Sync, and its log is redrawn from the files the folder holds.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log fields=verified -->

| Entry                    | Verified | Purpose    |
| :----------------------- | :------- | :--------- |
| [`README.md`](README.md) | -        | This file. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push to the default branch,
from each report's own frontmatter.

---

## 🔗 See also

- [Research Log template](../../templates/Research-Log.md) - the shape every report takes
- [Technical documentation](../README.md) - the designs, plans and parts this research feeds

---

<div align="center">

**Answered once. Kept honest. Never stale.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
