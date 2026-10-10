<!--
title: '🎨 ASSETS'
description: 'Where this project keeps what presents it: three folders nearly every project needs, a name ready for every other kind, and the rules every file follows.'
tags: [assets, branding, images, documentation]
category: docs
-->

<div align="center">

# 🎨 ASSETS

<a name="top"></a>

**What this project shows the world, and one set of rules for all of it.**

_Three folders to start. A name ready for the rest._

</div>

---

**Every repository has this folder, whatever the project.** Every project has
something to show: a logo, a screenshot, a diagram. And every repository that
draws its README with the [Markdown
Kit](https://github.com/tannergolden/markdown) needs a home for each file the
kit generates. So `assets/` is here from the first commit, holding only what
nearly every project needs, and a file never has to wonder where it goes.

---

## 📁 What Goes Where

<!-- AUTO-INDEX:BEGIN dir=. style=log exclude=banners,badges,trophies,elements -->

| Entry                                   | Purpose                                                                                                                            |
| :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| [`branding/`](branding/README.md)       | The marks, colours and type that identify this project: logo, mark, wordmark, icon, favicon, palette, and the social preview card. |
| [`diagrams/`](diagrams/README.md)       | Architecture, flow, sequence and data drawings that Mermaid in the text cannot express.                                            |
| [`screenshots/`](screenshots/README.md) | Captures of the product and the terminal, still or moving, in day and night pairs, for the README and the docs.                    |
| [`README.md`](README.md)                | This file.                                                                                                                         |

<!-- AUTO-INDEX:END -->

Three folders ship, because nearly every project fills them: `branding/` for who
it is, `screenshots/` for what it looks like, and `diagrams/` for how it works.
Each holds only its README until its first file arrives.

🗂️ Machined Indexes redraws this table after every push, and every folder here
carries a `README.md` that logs the files inside it in the same way.

---

## ➕ When You Need Another

Nothing else ships, so nobody scrolls past folders their project will never use.
When the first file of another kind arrives, make its folder under the name
below, beside the three, and give it a `README.md` that logs it the way theirs
do.

| Folder           | For                                                                                  |
| :--------------- | :----------------------------------------------------------------------------------- |
| `illustrations/` | Drawn artwork: hero art, empty states, spot illustrations, a mascot                  |
| `photos/`        | Photographs of hardware, setups, people and events, resized and stripped of metadata |
| `icons/`         | An icon set the pages use, beyond the project's own icon in `branding/`              |
| `video/`         | Demos and walkthroughs, through Git LFS or a release asset rather than plain git     |
| `audio/`         | Sound the project ships or demonstrates, through Git LFS like video                  |
| `fonts/`         | Typefaces the artwork is set in, each beside its licence                             |
| `mockups/`       | Wireframes and design comps, from before a feature was built                         |
| `slides/`        | Talks and decks, the source beside a PDF export                                      |
| `print/`         | Stickers, posters and swag, at print resolution, with the bleed marked               |
| `html/`          | Self-contained pages that open in a browser: previews, demos, embeds                 |

---

## 🧩 Drawn By The Markdown Kit

A page drawn with the [Markdown Kit](https://github.com/tannergolden/markdown)
gets these too. The kit makes each folder the first time it draws into it, so a
repository that never uses the kit never sees them, and a README log leaves them
out.

| Folder            | Holds                                                                                      |
| :---------------- | :----------------------------------------------------------------------------------------- |
| `banners/`        | The header, the footer and the row of links under it                                       |
| `badges/static/`  | Every badge whose value the settings write, and the shields.io badges localized            |
| `badges/dynamic/` | Every live badge, measured by the kit or set by a workflow: the only ones in gold          |
| `trophies/`       | The trophy case: the level and next-up cards, the trophies and the achievements            |
| `elements/`       | The body's drawings: the schematic, instruments, milestones, roster, certificate, placards |

> [!NOTE]
> **The kit owns the SVGs, not the folder.** It redraws them on every run and
> takes away any it no longer draws, and leaves every other file here alone,
> this README included. Change `.github/markdown.yaml` and let it redraw: a
> hand-edited SVG is overwritten on the next run.

---

## 📏 The Rules Every Folder Follows

1. **File by kind, never by page.** A file goes in the folder for what it is,
   whichever document shows it: a diagram is a diagram whether the README or a
   design document embeds it.
2. **Name in kebab-case.** Lowercase words joined by hyphens, with a variant as
   a suffix: `-dark` for the night theme, `@2x` for double density, `-512` for a
   size in pixels. A source and its export share a name:
   `ingest-pipeline.drawio` beside `ingest-pipeline.svg`.
3. **Keep the source.** Commit the editable original beside every export, or use
   a format that is both, like `.drawio.svg`, so the next change starts from the
   source rather than a copy of it.
4. **Draw for both themes.** Anything that sits on the page's background gets a
   `-dark` twin, shown with a `<picture>`.
5. **Choose the format by kind.** SVG for anything drawn, PNG for a screenshot,
   JPEG or WebP for a photograph, GIF for motion that plays inline.
6. **Mind the size.** Under 1 MB for an image and 5 MB for a GIF. Anything
   larger, and every video and audio master, goes through Git LFS or a release
   asset, decided before the first commit.
7. **Log every file.** Each folder's README logs what is in it. Write what each
   file is and the page that shows it in its row, and the row survives every
   regeneration. A file the project did not make names its source and its
   licence there.

A light and a dark image, as a page shows them:

```html
<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="assets/screenshots/dashboard-dark.png"
  />
  <img
    alt="The dashboard, with three healthy services"
    src="assets/screenshots/dashboard.png"
  />
</picture>
```

---

## 🔗 Referencing An Asset

Use a **repository-relative** path from the document doing the referencing. A
document at `docs/technical/Architecture.md` reaches a diagram here as
`../../assets/diagrams/ingest-pipeline.svg`, written as an image with alt text:

<!-- Shown as inline code rather than a live image: a link checker follows a
     real markdown image, and this example names a file that does not exist. -->

`![Architecture of the ingest pipeline](../../assets/diagrams/ingest-pipeline.svg)`

> [!IMPORTANT]
> **A profile README is the exception.** It renders off-repository, where a
> relative path resolves against the viewer's page and breaks. Those need an
> absolute `raw.githubusercontent.com` URL. Everywhere else, relative wins: it
> survives a fork, a rename, and a branch.

**Always write alt text.** It is what a screen reader announces and what shows
when an image fails to load, and it is the one accessibility requirement that
costs nothing to meet.

---

## 🚫 What Does Not Live Here

- **Assets the code loads.** An icon in an application bundle, a web page's
  stylesheet, a game's sprites: they live with the code that loads them. This
  folder holds what presents the project.
- **Build output.** Compiled or bundled images belong in the build directory and
  stay out of version control. The kit's drawings are the one exception,
  committed on purpose, because a README can show only what its repository
  serves.
- **Large binaries in plain git.** Git stores every version of a file forever. A
  file past a megabyte or two goes through Git LFS or an external host.
- **Anything you do not have the rights to redistribute.** A repository is a
  redistribution.

---

<div align="center">

**Sources here. Build output elsewhere. Alt text always.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../LICENSE).

</div>
