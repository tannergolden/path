<!--
title: '🏅 BADGES'
description: 'Badge artwork the badge kit draws from one data file, in a static and a dynamic folder.'
tags: [badges, assets, documentation, automation]
category: docs
-->

<div align="center">

# 🏅 BADGES

<a name="top"></a>

**Badge artwork committed to the repository, drawn by a kit rather than fetched.**

_Drawn once. Served from here._

</div>

---

## 💡 What This Folder Is For

A badge served from a third-party host is a request on every page view, and a
dependency on someone else's uptime for this project's pages to render. The
standards draw badges instead: a badge kit reads one data file,
`.github/badges.yml`, draws an SVG for each entry, and commits it here.

The kit sorts what it draws by label colour. A **gold** label marks a live,
dynamic-health badge and lands in `dynamic/`; every other badge is static and
lands in `static/`. Nothing is drawn until the kit is wired in with a data file
and a workflow stub, so both folders hold only their README for now.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                           | Purpose                                                                                   |
| :------------------------------ | :---------------------------------------------------------------------------------------- |
| [`dynamic/`](dynamic/README.md) | Gold-label health badges the badge kit draws, whose colour reports a live status.         |
| [`static/`](static/README.md)   | Fixed-message badges the badge kit draws: status, role, context, licence, and navigation. |
| [`README.md`](README.md)        | This file.                                                                                |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push.

---

## 🔗 Referencing A Badge

- **From the root `README.md`**, a relative path resolves everywhere it is read.
- **From every other document**, use the absolute `raw.githubusercontent.com`
  URL pinned to the default branch. GitHub leaves a relative image path
  unresolved in the pull-request rich diff and the security-policy tab.
- **Always write alt text**, for a badge as for any image.

The full rules, and the kit itself, are in the standards'
[Badge Visual Standards](https://github.com/tannergolden/standards/blob/Development/docs/technical/interface/Document-Styling-&-Formatting.md#-badge-visual-standards).

> [!NOTE]
> **The kit owns the SVGs, not the folders.** It deletes an `.svg` that no entry
> in its data file names any more, and leaves every other file alone, these
> READMEs included. Change the data file and let it redraw: a hand-edited SVG is
> overwritten on the next run.

---

<div align="center">

**Draw the badge once, and let the page load nothing it does not own.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
