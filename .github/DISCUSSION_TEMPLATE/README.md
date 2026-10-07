<!--
title: '💬 DISCUSSION FORMS'
description: 'Logs the discussion category forms, the category each one is bound to by its file name, and which of those categories must be created first.'
tags: [discussions, discussion-forms, community, triage]
category: docs
-->

<div align="center">

# 💬 DISCUSSION FORMS

<a name="top"></a>

**The forms that shape a new discussion, each bound to the category it is named after.**

_The file name is the binding._

</div>

---

## 💡 What This Folder Is For

Questions, ideas, and announcements belong in Discussions rather than the issue
tracker. When someone starts a discussion, GitHub fills its body from the form
whose file name matches the category's **slug** - `q-a.yaml` for Q&A,
`ideas.yaml` for Ideas - so each category asks for what it needs. Every form
also applies `type: discussion` and `status: needs triage`.

Discussions must be switched on first, under <kbd>Settings</kbd> →
<kbd>General</kbd> → <kbd>Features</kbd>.

---

## 📝 File Log

| File                                                               | Category       | For                                                                                           |
| :----------------------------------------------------------------- | :------------- | :-------------------------------------------------------------------------------------------- |
| [`accessibility.yaml`](accessibility.yaml)                         | Create it      | Contrast, keyboard navigation, focus order, and screen readers                                |
| [`announcements.yaml`](announcements.yaml)                         | GitHub default | Official updates: releases, deprecations, and roadmap notes. Maintainers post here            |
| [`community.yaml`](community.yaml)                                 | Create it      | Introductions, meetups, and topics no other category fits                                     |
| [`ideas.yaml`](ideas.yaml)                                         | GitHub default | Early ideas, worked through before they become a formal Feature Request                       |
| [`internationalization-i18n.yaml`](internationalization-i18n.yaml) | Create it      | Translation, localization, and locale problems                                                |
| [`polls.yaml`](polls.yaml)                                         | GitHub default | Time-boxed polls for lightweight decisions such as priorities and naming                      |
| [`q-a.yaml`](q-a.yaml)                                             | GitHub default | "How do I...?" questions, with the best answer marked once solved                             |
| [`roadmap.yaml`](roadmap.yaml)                                     | Create it      | High-level plans and milestones, linked to the issues and pull requests that track them       |
| [`showcase.yaml`](showcase.yaml)                                   | Create it      | Demos, prototypes, case studies, and lessons learned                                          |
| [`tooling-setup.yaml`](tooling-setup.yaml)                         | Create it      | Editors, runtimes, package managers, linters, CI runners, and dev containers. Adds `area: dx` |
| [`README.md`](README.md)                                           | -              | This log. GitHub reads only the YAML forms here                                               |

Add a row here in the same change that adds a form.

> [!IMPORTANT]
> **A form applies only to a category whose slug matches its file name.** Four
> of these match a category every repository starts with. The other six do
> nothing until you create the category, named so that its slug comes out the
> same: _Tooling & Setup_ for `tooling-setup`, for example. A rename that
> changes the slug orphans its form without a word. GitHub's other two starting
> categories, General and Show and tell, have no form here and open blank.

---

<div align="center">

**One category, one form, one name binding them.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
