<!--
title: '📜 IMPLEMENTATION PLAN TEMPLATE'
description: 'Reusable template for planning an implementation in small, reviewable slices.'
tags: [template, planning, implementation, delivery]
category: docs
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 📜 IMPLEMENTATION PLAN TEMPLATE

<a name="top"></a>

**Bridges a design and its code - the concrete changes, their order, and how each will be verified.**

_Structured strategy. Reduced risk. Clear implementation._

</div>

---

> [!NOTE]
> **How to use**: copy this file to `docs/technical/plans/<short-slug>.md` (keep this template pristine) and replace the bracketed placeholders. It bridges the [Technical Design](/docs/templates/Technical-Design.md) and the code - small enough to review, complete enough to execute.

---

## 🎯 Goal

A concise description of what this implementation aims to achieve and the problem it solves.

## 🗺️ Scope

- **In scope**: [What this plan delivers]
- **Out of scope**: [Deferred or excluded work]

## 🏗️ Proposed Changes

### [Component/Service Name]

- [ ] Describe change 1
- [ ] Describe change 2

### [Another Component/Service Name]

- [ ] Describe change 1

## 📅 Milestones

1. [Milestone - deliverable and rough sequencing]
2. [Milestone - deliverable and rough sequencing]

## ⚠️ Risks & Mitigations

| Risk   | Likelihood              | Mitigation            |
| :----- | :---------------------- | :-------------------- |
| [Risk] | [High \| Medium \| Low] | [How it is contained] |

## 🧪 Verification Plan

### Automated Tests

```bash
# Command to run the relevant suite
make test
```

### Manual Verification

1. Step 1 of manual check
2. Step 2 of manual check

## ⏪ Rollback

- [How to revert if the change misbehaves: revert PR, flag off, restore config]

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Planned with rigor. Delivered in slices.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
