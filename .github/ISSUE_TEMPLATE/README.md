<!--
title: '📥 ISSUE FORMS'
description: 'Logs the issue forms a reporter chooses from and the chooser configuration beside them, and explains why this README is never offered as a form.'
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

| File                                                     | Shows as                | For                                                                             |
| :------------------------------------------------------- | :---------------------- | :------------------------------------------------------------------------------ |
| [`Accessibility-Report.yaml`](Accessibility-Report.yaml) | ♿ Accessibility Report | Barriers to inclusive use: contrast, keyboard access, focus, screen readers     |
| [`Bug-Report.yaml`](Bug-Report.yaml)                     | 🐛 Bug Report           | A defect or regression, with what it takes to reproduce it                      |
| [`Documentation-Report.yaml`](Documentation-Report.yaml) | 📚 Documentation Report | Gaps, inaccuracies, outdated sections, or unclear passages in the documentation |
| [`Feature-Request.yaml`](Feature-Request.yaml)           | ✨ Feature Request      | New functionality, with acceptance criteria, rationale, and success metrics     |
| [`Feedback-Report.yaml`](Feedback-Report.yaml)           | 📝 Feedback Report      | Suggestions and usability insights that are not a defect                        |
| [`Performance-Report.yaml`](Performance-Report.yaml)     | 🚀 Performance Report   | Slow pages, latency, memory spikes, and other inefficiencies, with measurements |
| [`Vulnerability-Report.yaml`](Vulnerability-Report.yaml) | 🛡️ Vulnerability Report | A suspected vulnerability, on a **private** repository only                     |
| [`config.yml`](config.yml)                               | -                       | Switches blank issues off and adds the one contact link, to Discussions         |
| [`README.md`](README.md)                                 | -                       | This log. GitHub never offers it as a form                                      |

Add a row here in the same change that adds a form.

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
