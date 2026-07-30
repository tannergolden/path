<!--
title: '👤 USER STORY TEMPLATE'
description: 'Template for writing user stories with clear acceptance criteria.'
tags: [template, user-story, product, requirements]
category: docs
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 👤 USER STORY TEMPLATE

<a name="top"></a>

**Captures a user-facing requirement as a persona, a motivation, and verifiable acceptance criteria.**

_Empathy driven. Clear criteria. Better outcomes._

</div>

---

> [!TIP]
> **How to use**: copy this file to `docs/<area>/stories/<short-slug>.md` (or your tracker of choice), keep this template pristine, and write from the end-user's perspective - the value delivered, not the implementation.

---

## 👤 Persona

**As a** [type of user],
**I want** [to perform some action],
**So that** [I can achieve some goal/benefit].

## ✅ Acceptance Criteria

Verifiable outcomes - each one testable, none about implementation detail:

- [ ] Given [context], when [action], then [outcome].
- [ ] Given [context], when [action], then [outcome].
- [ ] Errors and empty states behave as specified.

## 🚫 Out of Scope

- [Explicitly excluded behavior - prevents silent scope creep]

## 🎨 Wireframes/Mockups

- [Link to Figma/Design]
- [User Interface conventions](technical/interface/Formatting-&-Standards.md) - the fill-in standard for this project's interface rules

## 🔗 Dependencies

- [Blocking stories, services, migrations, or approvals]

## 🛠️ Technical Notes

- Database schema changes needed
- New API endpoints required
- Third-party integrations

## 🏁 Definition of Done

- [ ] Acceptance criteria verified by automated tests where practical
- [ ] Documentation updated if behavior or setup changed
- [ ] Reviewed and squash-merged through the normal gates

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Designed for people. Built for purpose.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
