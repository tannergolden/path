<!--
title: '🎨 ASSETS'
description: 'Where this project keeps everything that presents it: a folder for every kind of asset, the rules every file follows, and what lives somewhere else.'
tags: [assets, branding, images, documentation]
category: docs
-->

<div align="center">

# 🎨 ASSETS

<a name="top"></a>

**A home for every kind of asset this project owns, and one set of rules for all of them.**

_Filed by kind. Named in kebab-case. Logged where it lives._

</div>

---

**Every repository has this folder, whatever the project.** Every project has
something to show: a logo, a screenshot, a diagram. And every repository that
draws its README with the [Markdown
Kit](https://github.com/tannergolden/markdown) needs a home for each file the
kit generates. So `assets/` is here from the first commit, with a folder for
every kind of asset, and a file never has to wonder where it goes.

---

## 📁 What Goes Where

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                       | Purpose                                                                                                                             |
| :------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------- |
| [`animations/`](animations/README.md)       | Looping demos that play inline: GIFs, and the terminal recordings they are made from.                                               |
| [`audio/`](audio/README.md)                 | Sound the project presents itself with: podcast clips, trailers, voice-overs and sound design.                                      |
| [`badges/`](badges/README.md)               | Badges the Markdown Kit draws: static ones in static/, live ones in dynamic/.                                                       |
| [`banners/`](banners/README.md)             | The header, footer and link buttons the Markdown Kit draws for the README.                                                          |
| [`branding/`](branding/README.md)           | The marks, colours and type that identify this project: logo, mark, wordmark, app icon, favicon, palette and type specimen.         |
| [`diagrams/`](diagrams/README.md)           | Architecture, flow, sequence and data drawings that Mermaid in the text cannot express.                                             |
| [`elements/`](elements/README.md)           | The drawings the Markdown Kit places in the README's body: schematics, instruments, milestones, rosters, certificates and placards. |
| [`fonts/`](fonts/README.md)                 | The typefaces the brand, diagrams and graphics are set in, each with its licence.                                                   |
| [`html/`](html/README.md)                   | Standalone HTML pages: previews, demos, prototypes and embeds that open in a browser.                                               |
| [`icons/`](icons/README.md)                 | Small symbols for the docs: feature icons, and third-party logos used under their owners' terms.                                    |
| [`illustrations/`](illustrations/README.md) | Drawn artwork: hero art, empty states, spot illustrations and mascots.                                                              |
| [`mockups/`](mockups/README.md)             | Wireframes, design comps and exported prototype screens: what the product will look like, before it does.                           |
| [`photos/`](photos/README.md)               | Photographs: hardware, setups, people and events.                                                                                   |
| [`print/`](print/README.md)                 | Material made to be printed or handed out: datasheets, one-pagers, posters and stickers.                                            |
| [`screenshots/`](screenshots/README.md)     | Captures of the product and the terminal, in day and night pairs, for the README and the docs.                                      |
| [`slides/`](slides/README.md)               | Decks and talk material about the project, exported to PDF.                                                                         |
| [`social/`](social/README.md)               | The images the project is shown by off-site: the repository's social preview, Open Graph cards and launch graphics.                 |
| [`trophies/`](trophies/README.md)           | The trophy case the Markdown Kit draws: the tiered trophies, the level and next-up cards, and the achievements.                     |
| [`video/`](video/README.md)                 | Demos, walkthroughs and talks too long or too large to play inline.                                                                 |
| [`README.md`](README.md)                    | This file.                                                                                                                          |

<!-- AUTO-INDEX:END -->

Fifteen folders are yours, one for every kind of asset a repository presents
itself with. Each holds only its README until its first file arrives, so the
next file always has an obvious home. The other four are the Markdown Kit's: it
draws `banners/`, `badges/`, `trophies/` and `elements/` on every run of the
page's stub, and keeps them current.

🗂️ Machined Indexes redraws this table after every push, and every folder here
carries a `README.md` that logs the files inside it in the same way.

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
