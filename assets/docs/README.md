<!--
title: '📊 DOCUMENT FIGURES'
description: 'Logs the diagrams and figures embedded in the documents of this project, and says how a document should reference one.'
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

| File                     | Purpose  |
| :----------------------- | :------- |
| [`README.md`](README.md) | This log |

Add a row here in the same change that adds a figure, naming the document that
embeds it, so a figure nothing uses any more is easy to find and delete.

---

<div align="center">

**Diagrams as code first, and a figure only where code cannot draw it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
