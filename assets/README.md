<!--
title: '🎨 ASSETS'
description: 'Where this project keeps its images, logos, and diagrams, and which visual assets deliberately live somewhere else.'
tags: [assets, branding, images, documentation]
category: docs
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🎨 ASSETS

<a name="top"></a>

**A designated home for everything visual this project owns.**

_Empty on purpose. Yours to fill._

</div>

---

## 📁 What Goes Where

| Folder      | Put here                                                        |
| :---------- | :-------------------------------------------------------------- |
| `branding/` | Logos, icons, colour palettes, typography specimens             |
| `images/`   | General project imagery, screenshots, product shots             |
| `docs/`     | Diagrams and figures embedded in documents under `docs/`        |

Three folders because three is what every project needs. Add your own -
`mockups/`, `diagrams/`, `video/` - as soon as you have something to put in
them. An empty folder invented ahead of a need is a folder nobody uses.

---

## 🔗 Referencing An Asset

Use a **repository-relative** path from the document doing the referencing. A
document at `docs/technical/Architecture.md` reaches a diagram here as
`../../assets/docs/ingest-pipeline.svg`, written as an image with alt text:

<!-- Shown as inline code rather than a live image: a link checker follows a
     real markdown image, and this example names a file that does not exist. -->

`![Architecture of the ingest pipeline](../../assets/docs/ingest-pipeline.svg)`

> [!IMPORTANT]
> **A profile README is the exception.** It renders off-repository, where a
> relative path resolves against the viewer's page and breaks. Those need an
> absolute `raw.githubusercontent.com` URL. Everywhere else, relative wins:
> it survives a fork, a rename, and a branch.

**Always write alt text.** It is what a screen reader announces and what shows
when an image fails to load, and it is the one accessibility requirement that
costs nothing to meet.

---

## 🚫 What Does Not Live Here

- **Build output.** Compiled or bundled images belong in your build directory
  and stay out of version control. This folder is for sources.
- **Large binaries.** Git stores every version of a file forever. Anything past
  a megabyte or two wants Git LFS or an external host, decided before the first
  commit rather than after the clone gets slow.
- **Anything you do not have the rights to redistribute.** A repository is a
  redistribution.

---

<div align="center">

**Sources here. Build output elsewhere. Alt text always.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the MIT License.

</div>
