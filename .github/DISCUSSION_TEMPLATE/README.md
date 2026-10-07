<!--
title: '💬 DISCUSSION FORMS'
description: 'The discussion category forms, each bound by its file name to the category it shapes.'
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

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                              | Purpose                                                                                                                                          |
| :----------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| [`accessibility.yaml`](accessibility.yaml)                         | Accessibility feedback - contrast, keyboard navigation, focus order, screen readers.                                                             |
| [`announcements.yaml`](announcements.yaml)                         | Official updates such as releases, deprecations, and roadmap notes.                                                                              |
| [`community.yaml`](community.yaml)                                 | General discussion, introductions, meetups, and topics that don&#x2019;t fit other categories.                                                   |
| [`ideas.yaml`](ideas.yaml)                                         | Brainstorm features or improvements before opening a formal Feature Request.                                                                     |
| [`internationalization-i18n.yaml`](internationalization-i18n.yaml) | Translation and localization topics, language-specific feedback, and locale issues.                                                              |
| [`polls.yaml`](polls.yaml)                                         | Run time-boxed surveys to gather community sentiment and make lightweight decisions (priorities, roadmap themes, release timing, naming).        |
| [`q-a.yaml`](q-a.yaml)                                             | Ask &#x201C;how do I&#x2026;?&#x201D; questions and get help from maintainers and the community.                                                 |
| [`README.md`](README.md)                                           | This file.                                                                                                                                       |
| [`roadmap.yaml`](roadmap.yaml)                                     | High-level plans and milestones. Link to Issues and Pull Requests for tracking.                                                                  |
| [`showcase.yaml`](showcase.yaml)                                   | Share demos, prototypes, case studies, success stories, and lessons learned.                                                                     |
| [`tooling-setup.yaml`](tooling-setup.yaml)                         | Developer environment topics - IDEs, Node.js versions, package managers, linters, CI runners, containers/devcontainers, and local configuration. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from the prose each form
opens with.

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
