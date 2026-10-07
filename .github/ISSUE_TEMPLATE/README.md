<!--
title: '📥 ISSUE FORMS'
description: 'The issue forms a reporter chooses from, and the chooser configuration that offers them.'
tags: [issues, issue-forms, triage, community]
category: docs
-->

<div align="center">

# 📥 ISSUE FORMS

<a name="top"></a>

**The forms a reporter picks from when opening an issue, and the chooser that offers them.**

_Every report arrives already triaged._

</div>

---

## 💡 What This Folder Is For

When someone opens an issue, GitHub shows the forms in this folder instead of a
blank text box. Each asks for what its kind of report needs, so a maintainer
can act on it without a round of questions first, and each applies a `type:`
label and `status: needs triage` so it lands in the triage queue.

Blank issues are switched off, which leaves these forms and one link to
Discussions as the only ways in.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log fields=name -->

| Entry                                                    | Name                                   | Purpose                                                                                                                                    |
| :------------------------------------------------------- | :------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| [`Accessibility-Report.yaml`](Accessibility-Report.yaml) | &#x267F; Accessibility Report          | &#x26D1;&#xFE0F; Report accessibility issues to improve compliance and inclusive User Experience (UX).                                     |
| [`Bug-Report.yaml`](Bug-Report.yaml)                     | &#x1F41B; Bug Report                   | &#x1F41E; Report a defect, regression, or unexpected behavior so we can reproduce and fix it quickly.                                      |
| [`config.yml`](config.yml)                               | -                                      | Steer reporters into the right template, and keep vulnerability reports PRIVATE.                                                           |
| [`Documentation-Report.yaml`](Documentation-Report.yaml) | &#x1F4DA; Documentation Report         | &#x1F4D6; Report documentation gaps, inaccuracies, outdated sections, or clarity issues so we can correct and improve them.                |
| [`Feature-Request.yaml`](Feature-Request.yaml)           | &#x2728; Feature Request               | &#x1FA84; Propose new functionality or enhancements with clear acceptance criteria, rationale, and success metrics.                        |
| [`Feedback-Report.yaml`](Feedback-Report.yaml)           | &#x1F4DD; Feedback Report              | &#x1F4A1; Share feedback, suggestions, or usability insights to help us improve the project.                                               |
| [`Performance-Report.yaml`](Performance-Report.yaml)     | &#x1F680; Performance Report           | &#x26A1;&#xFE0F; Report slow pages, high latency, memory spikes, or inefficiencies so we can measure, reproduce, and optimize performance. |
| [`README.md`](README.md)                                 | -                                      | This file.                                                                                                                                 |
| [`Vulnerability-Report.yaml`](Vulnerability-Report.yaml) | &#x1F6E1;&#xFE0F; Vulnerability Report | PRIVATE repos only: report suspected vulnerabilities here. For PUBLIC repos, do not open an issue - use SECURITY.md for private reporting. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from each form's own
`name:` and `description:`.

> [!IMPORTANT]
> **Never give this README YAML front matter.** GitHub lists a Markdown file in
> this folder as an issue template only when it opens with front matter naming
> it. This one opens with an HTML comment instead, which is why the chooser
> never shows it.

---

## 🛡️ Vulnerabilities Stay Private

The Vulnerability Report form is for **private** repositories only. On a public
repository a vulnerability never goes in an issue, where anyone can read it: it
goes through private vulnerability reporting, as [`SECURITY.md`](../SECURITY.md)
explains. GitHub adds **Report a vulnerability** to the chooser by itself once
that is enabled, which is why `config.yml` carries no security link of its own.

---

## ⚙️ The Discussions Link

The contact link in `config.yml` carries a placeholder, `OWNER/REPOSITORY`,
because GitHub substitutes nothing in a contact link. Initialisation rewrites
it for this repository. It still leads nowhere until Discussions is switched on,
under <kbd>Settings</kbd> → <kbd>General</kbd> → <kbd>Features</kbd>.

Any file in this folder also switches off every default form an account's
`.github` repository would otherwise supply. It is all or nothing, so a
repository that keeps one form of its own keeps the whole set here.

---

<div align="center">

**The right questions, asked before the issue is opened.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
