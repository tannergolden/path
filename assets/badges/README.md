<!--
title: '🏅 BADGES'
description: 'Badges the Markdown Kit draws: static ones in static/, live ones in dynamic/.'
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
[Markdown Kit](https://github.com/tannergolden/markdown) draws each badge listed
under `badges:` in `.github/markdown.yaml` instead, and commits it here.

It files each badge by what it is. A **live** badge names a `measure:`:
something the kit measures on every run, or `set`, a value another workflow
measures and writes with `markdown-kit set`. It lands in `dynamic/`, and only a
live badge may wear the gold label. Every other badge is **static**: it says
what its author wrote, and lands in `static/`, with the shields.io badges the
kit draws from the repository's Markdown in `static/localized/`.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                           | Purpose                                                                                                |
| :------------------------------ | :----------------------------------------------------------------------------------------------------- |
| [`dynamic/`](dynamic/README.md) | Live badges: values the Markdown Kit measures or a workflow sets, the only ones under the gold label.  |
| [`static/`](static/README.md)   | Badges that say what their author wrote: identity, navigation and posture, never under the gold label. |
| [`README.md`](README.md)        | This file.                                                                                             |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push.

---

## 🔗 Referencing A Badge

- **From the root `README.md`**, a relative path resolves everywhere it is read.
- **From every other document**, use the absolute `raw.githubusercontent.com`
  URL pinned to the default branch. GitHub leaves a relative image path
  unresolved in the pull-request rich diff and the security-policy tab.
- **Always write alt text**, for a badge as for any image.

The settings, and every rule the kit holds a badge to, are in its [settings
reference](https://github.com/tannergolden/markdown/blob/Development/docs/Settings.md).

> [!NOTE]
> **The kit owns the SVGs, not the folder.** It redraws them on every run and
> takes away any it no longer draws, and leaves every other file here alone,
> this README included. Change `.github/markdown.yaml` and let it redraw: a
> hand-edited SVG is overwritten on the next run.

---

<div align="center">

**Draw the badge once, and let the page load nothing it does not own.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../../LICENSE).

</div>
