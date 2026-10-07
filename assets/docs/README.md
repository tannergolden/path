<!--
title: '📊 DOCUMENT FIGURES'
description: 'The diagrams and figures embedded in the documents of this project.'
tags: [diagrams, figures, assets, documentation]
category: docs
-->

<div align="center">

# 📊 DOCUMENT FIGURES

<a name="top"></a>

**The diagrams and figures that the documents under `docs/` embed.**

_Mermaid in the text. Everything else here._

</div>

---

## 💡 What This Folder Is For

A diagram that can be written as code belongs in the document itself, as a
Mermaid block: it is versioned with the text, reviewed in the same diff, and
readable without rendering. This folder is for the figures that cannot be:
exported architecture drawings, annotated screenshots, charts.

A document reaches a figure here by a **relative path** from where the document
sits, with alt text. From `docs/technical/Architecture.md`, that is
`../../assets/docs/ingest-pipeline.svg`.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                    | Purpose    |
| :----------------------- | :--------- |
| [`README.md`](README.md) | This file. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push. A figure cannot describe
itself, so name the document that embeds it in its row, where regeneration keeps
it and a figure nothing uses any more is easy to find.

---

<div align="center">

**Diagrams as code first, and a figure only where code cannot draw it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
