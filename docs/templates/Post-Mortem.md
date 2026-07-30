<!--
title: '📉 POST-MORTEM TEMPLATE'
description: 'Blameless post-mortem template for capturing incidents and their lessons.'
tags: [template, post-mortem, incidents, operations]
category: docs
-->

<div align="center">

# 📉 POST-MORTEM TEMPLATE

<a name="top"></a>

**Records an incident or project outcome blamelessly - impact, timeline, root cause, and the actions that prevent a repeat.**

_Continuous learning. Radical transparency. Future focus._

</div>

---

> [!CAUTION]
> **How to use**: copy this file to `docs/operations/post-mortems/YYYY-MM-DD-<short-slug>.md` and keep this template pristine. Stay **blameless**: name processes and safeguards, never people - the goal is prevention, not fault.

---

## 🗓️ Overview

| Attribute             | Value                                 |
| :-------------------- | :------------------------------------ |
| **Date**              | [YYYY-MM-DD]                          |
| **Severity / Impact** | [Critical \| High \| Medium \| Low]   |
| **Duration**          | [Detection → resolution, e.g. 2h 15m] |
| **Affected**          | [Users/systems impacted and how]      |

## 📝 Summary

A brief overview of the project outcome or incident.

## ⏱️ Timeline (for incidents)

- `[HH:MM]` - First effect / triggering change
- `[HH:MM]` - Detected (how: alert, user report, dashboard)
- `[HH:MM]` - Mitigated (what stopped the bleeding)
- `[HH:MM]` - Resolved (fully recovered)

## 📈 What Went Well

- Success 1
- Success 2

## 📉 What Could Be Improved

- Challenge 1
- Challenge 2

## 🛠️ Root Cause Analysis (for incidents)

- Why did it happen? (ask "why" until you reach a process, not a person)
- Why wasn't it caught earlier? (tests, review, monitoring)
- How was it detected?

## 📝 Lessons Learned

- Key takeaway 1
- Key takeaway 2

## ✅ Action Items

Every item needs an owner and a tracking issue - untracked actions don't happen.

- [ ] [Prevention task] - owner: [@handle], issue: #
- [ ] [Detection/monitoring improvement] - owner: [@handle], issue: #
- [ ] [Documentation/runbook update] - owner: [@handle], issue: #

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Learning from failure. Scaling through knowledge.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
