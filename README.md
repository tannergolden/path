<!--
title: '🛤️ GOLDEN PATH'
description: 'A language-agnostic scaffold. Structure, community health files, and workflow triggers, with every standard followed by link rather than copied.'
type: index
-->

<!-- markdown:header:start -->
<!-- markdownlint-disable MD041 -->

<div align="center">

<a name="top"></a>

<picture>
  <source media="(max-width: 585px) and (prefers-color-scheme: dark)" srcset="assets/banners/header-narrow-dark.svg">
  <source media="(max-width: 585px)" srcset="assets/banners/header-narrow-day.svg">
  <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/banners/header-still-dark.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/banners/header-still-day.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/banners/header-dark.svg">
  <img alt="path: Golden path repository template: language-agnostic boilerplate with folder structure, community health files, dev container and GitHub Actions CI wired to…. Scaffold here. Standards by link. Template fixes when you ask. Project: tannergolden/path. Release: v1.4.1. Stars: 0. Forks: 0. Open issues: 0. License: MIT." src="assets/banners/header-day.svg">
</picture>

</div>
<!-- markdown:header:end -->

---

## 💡 What It Is

A **golden path**: the paved, supported route to a new repository. Generate
from it and you start with a structure already decided (`src/`, `tests/`,
`packages/`, `benchmarks/`, `examples/`, `assets/` and `docs/`), community
health files already written, and continuous integration already wired.

The structure is **copied**, so it is yours from the first commit. The
standards arrive **by link**, from
[`tannergolden/standards`](https://github.com/tannergolden/standards), so a fix
there reaches every repository at once. It decides no language: no build
system, no package manager, no toolchain.

- **Status**: Active, and the template new repositories on this account start
  from.

---

## 🚀 Quick Start

1. **Click "Use this template"**, and choose the visibility with care: a
   repository made public later publishes its whole history
   ([going public](https://github.com/tannergolden/standards/blob/Development/docs/introduction/What-You-Do-By-Hand.md#going-public)).
2. **Let initialisation run.** The `init` job rewrites the identity to yours,
   turns the first commit into a Conventional Commit and deletes what only the
   template needs. If `.github/TEMPLATE_INIT` is still there after a minute or
   two, dispatch **🎯 Standards Lifecycle** from the Actions tab.
3. **Do the steps only a person can do**, signing and the admin token among
   them:
   [🙋 What You Do By Hand](https://github.com/tannergolden/standards/blob/Development/docs/introduction/What-You-Do-By-Hand.md).
4. **Fit your project in** with the
   [Fit My Project Into This Scaffold](docs/Prompts.md#fit-my-project-into-this-scaffold)
   prompt, and give the `ci` job your commands, as below.
5. **Replace this README** with
   [`docs/templates/Project-README.md`](docs/templates/Project-README.md),
   leaving out its masthead and footer: the kit draws those.

Generate rather than fork: a fork starts with Actions disabled, and
initialisation's force-push breaks its `Sync fork`.

---

## 📖 Using It

### ⚠️ CI Is Green, And Only Half Configured

The `ci` job in `checks.yml` runs the commands you give it, and fails when
none resolves rather than reporting a check that checked nothing. It starts on
[`.github/scripts/validate-repository.py`](.github/scripts/validate-repository.py),
which checks the files a new repository already has. Point it at your project
once there is code:

```yaml
jobs:
  ci:
    uses: tannergolden/standards/.github/workflows/ci.yml@v1
    with:
      lint-command: 'golangci-lint run'
      test-command: 'go test ./...'
      build-command: 'go build ./...'
```

One real command is enough. With a `Makefile` that has `lint`, `test` and
`build` targets, drop the `with:` block: the job falls back to `make <target>`.

### 🧭 This Layout, Or Your Own

Use this layout, and fit your project into it. Keep a layout of your own only
when the tree means something: dotfiles that mirror where they install, a
notes vault, or a tool that finds files by where they are. Either way the
checks, the community health files and the development container still apply.

### 🔄 Staying Current

- **The standards** are pinned at `@v1`, a moving major tag, so every fix in
  the v1 line arrives on its own. A new major opens one issue and changes
  nothing.
- **This template's fixes** arrive only when you run **🔄 Template Sync**, as
  one pull request: it overwrites the files you left alone and merges the ones
  you changed. A `#` in front of a line in
  [`.github/template-sync`](.github/template-sync) keeps that file yours, and a
  `BOT_ACCESS_TOKEN` lets it update workflow files
  ([how it works](.github/template-sync.md)).
- **The agent rules** in [`AGENTS.md`](AGENTS.md) arrive from
  [`tannergolden/intelligence`](https://github.com/tannergolden/intelligence)
  through 🔁 Intelligence Sync, one pull request per release.

[`.github/workflows/README.md`](.github/workflows/README.md) logs every
workflow, what starts it and the secrets it reads.

### 🎨 This Page Is Drawn

The [Markdown Kit](https://github.com/tannergolden/markdown) draws this
README's header, cards, trophy case and footer every night, from
`.github/workflows/markdown.yml` and `.github/markdown.yaml`. A generated
repository keeps both, and its theme is its own to change
([how](.github/markdown.md)). The cards are the four repositories every
generated repository runs on:

<div align="center">

<!-- markdown:element:path:start -->
<a href="https://github.com/tannergolden/path">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/elements/path-dark.svg">
  <img alt="tannergolden/path. Golden path repository template: language-agnostic boilerplate with folder structure, community health files, dev container and GitHub Actions CI wired to reusable workflows." src="assets/elements/path-day.svg">
</picture>
</a>
<!-- markdown:element:path:end -->
<!-- markdown:element:standards:start -->
<a href="https://github.com/tannergolden/standards">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/elements/standards-dark.svg">
  <img alt="tannergolden/standards. Engineering standards plus reusable GitHub Actions workflows and composite actions that enforce them for any language: CI/CD, security scanning, branch protection, releases." src="assets/elements/standards-day.svg">
</picture>
</a>
<!-- markdown:element:standards:end -->

<!-- markdown:element:intelligence:start -->
<a href="https://github.com/tannergolden/intelligence">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/elements/intelligence-dark.svg">
  <img alt="tannergolden/intelligence. Universal rules for AI coding agents like Claude Code, Codex, Copilot and Cursor: written once, tested by evals, synced to every repository as AGENTS.md and to every machine." src="assets/elements/intelligence-day.svg">
</picture>
</a>
<!-- markdown:element:intelligence:end -->
<!-- markdown:element:markdown:start -->
<a href="https://github.com/tannergolden/markdown">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/elements/markdown-dark.svg">
  <img alt="tannergolden/markdown. README generator for GitHub profiles and repos: scheduled GitHub Actions draw headers, badges, trophies and footers as committed SVGs. No third-party servers." src="assets/elements/markdown-day.svg">
</picture>
</a>
<!-- markdown:element:markdown:end -->

</div>

### 🧰 Maintaining This Template

- **Every change gets a line in [`CHANGELOG.md`](CHANGELOG.md)**, under
  **Unreleased**, in the same pull request: it is what an owner reads before a
  sync.
- **A new file needs a line in `.github/template-sync`**, in the section that
  says what a generated repository does with it
  ([For Template Authors](https://github.com/tannergolden/standards/blob/Development/docs/distribution/automation/Template-Sync.md#-for-template-authors)).
- **Only the first half of [`docs/Prompts.md`](docs/Prompts.md) is the
  template's.** The rest is each owner's, and the validator holds it to a hash.
- **A merge reaches existing repositories only through a release.** Dispatch
  🏷️ Cut Release from the default branch with the next `vX.Y.Z` and
  `move-major` on. A breaking change ships as `v2`, which no repository follows
  until its owner moves `ref:`.

---

## 📦 What's Inside

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                              | Purpose                                                                                                                                |
| :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| [`.devcontainer/`](.devcontainer/README.md)        | The language-neutral development container this repository ships, and how to give it the toolchain your project needs.                 |
| [`.github/`](.github/)                             | Community health files, forms, CODEOWNERS, Dependabot, actions, scripts and workflows - logged below                                   |
| [`assets/`](assets/README.md)                      | Where this project keeps what presents it: four folders to start, a name ready for every other kind, and the rules every file follows. |
| [`benchmarks/`](benchmarks/README.md)              | The benchmark suites and recorded results that defend the performance budgets of this project.                                         |
| [`docs/`](docs/README.md)                          | Where this project keeps its own documents, and where the engineering standards it follows actually live.                              |
| [`examples/`](examples/README.md)                  | Runnable examples that show how to use this project, one per task, built and checked with the code they show.                          |
| [`packages/`](packages/README.md)                  | Workspace packages, one folder each, for when a second consumer needs shared code.                                                     |
| [`src/`](src/README.md)                            | The application source, split into three layers whose dependencies point inward.                                                       |
| [`tests/`](tests/README.md)                        | The test suites, from isolated units to whole user journeys, and how CI comes to run them.                                             |
| [`.editorconfig`](.editorconfig)                   | Editor defaults every editor honours: UTF-8, LF, a final newline, and indentation per language                                         |
| [`.env.example`](.env.example)                     | Environment variable template for this project.                                                                                        |
| [`.git-blame-ignore-revs`](.git-blame-ignore-revs) | Commits that changed only formatting, which `git blame` should look through.                                                           |
| [`.gitattributes`](.gitattributes)                 | Git attributes - line endings, diffs, and what counts as binary                                                                        |
| [`.gitignore`](.gitignore)                         | &#x1F5C4;&#xFE0F; Universal Ignore Patterns                                                                                            |
| [`.markdownlint.json`](.markdownlint.json)         | Repository-wide markdownlint rules. Discovered by mechanism, which is why this lives at the root.                                      |
| [`AGENTS.md`](AGENTS.md)                           | How AI coding agents work in this repository: the universal rules first, then its own.                                                 |
| [`CHANGELOG.md`](CHANGELOG.md)                     | What changed in each release of this template, newest first, so an owner can see what a Template Sync will bring before running it.    |
| [`LICENSE`](LICENSE)                               | MIT License                                                                                                                            |
| [`README.md`](README.md)                           | This file.                                                                                                                             |

<!-- AUTO-INDEX:END -->

Every folder carries a `README.md` that logs each file inside it. GitHub shows
a README in `.github/` in place of this page, so that folder's own files are
logged here instead. 🗂️ Machined Indexes redraws both tables after every push:

<!-- AUTO-INDEX:BEGIN dir=./.github style=log -->

| Entry                                                           | Purpose                                                                                                                                              |
| :-------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`actions/`](.github/actions/README.md)                         | The composite actions this repository keeps for its own workflows, and for any other repository that calls them.                                     |
| [`DISCUSSION_TEMPLATE/`](.github/DISCUSSION_TEMPLATE/README.md) | The discussion category forms, each bound by its file name to the category it shapes.                                                                |
| [`ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/README.md)           | The issue forms a reporter chooses from, and the chooser configuration that offers them.                                                             |
| [`scripts/`](.github/scripts/README.md)                         | The checks this repository runs on its own configuration, and the tests that guard them.                                                             |
| [`workflows/`](.github/workflows/README.md)                     | Every workflow in this repository: the name it shows in the Actions tab, what triggers it, and what it does.                                         |
| [`ACCESSIBILITY.md`](.github/ACCESSIBILITY.md)                  | The accessibility this project aims for, how to report a barrier, and what happens after you do.                                                     |
| [`CODE_OF_CONDUCT.md`](.github/CODE_OF_CONDUCT.md)              | The code of conduct governing participation in this project, how to report a violation, and how harm is addressed and repaired.                      |
| [`CODEOWNERS`](.github/CODEOWNERS)                              | Folder-based ownership rules                                                                                                                         |
| [`commit-template.txt`](.github/commit-template.txt)            | &lt;type&gt;(&lt;scope&gt;): &lt;emoji&gt; &lt;subject starting lowercase, no em dash&gt;                                                            |
| [`CONTRIBUTING.md`](.github/CONTRIBUTING.md)                    | How to contribute, covering branching, commits, code style, testing, and the pull-request process.                                                   |
| [`dependabot.yml`](.github/dependabot.yml)                      | Dependabot - automated dependency updates                                                                                                            |
| [`FUNDING.yml`](.github/FUNDING.yml)                            | &#x1F496; Funding Options                                                                                                                            |
| [`GOVERNANCE.md`](.github/GOVERNANCE.md)                        | How this project is led, who decides what, how access continues, and the review and security standards every change meets.                           |
| [`markdown.lock.json`](.github/markdown.lock.json)              | -                                                                                                                                                    |
| [`markdown.md`](.github/markdown.md)                            | How the Markdown Kit draws this README, and how to change its theme, holidays, words, placards and trophies. Read it before editing its settings.    |
| [`markdown.yaml`](.github/markdown.yaml)                        | How &#x1F4DD; Markdown draws this README: its theme, the words on its header and footer, its placards and its trophy case.                           |
| [`pull_request_template.md`](.github/pull_request_template.md)  | This template becomes the body of your pull request.                                                                                                 |
| [`release.yml`](.github/release.yml)                            | GitHub auto-generated release notes configuration.                                                                                                   |
| [`SECURITY.md`](.github/SECURITY.md)                            | How to report a vulnerability privately, what happens after you do, which versions receive security fixes, and the protections this repository runs. |
| [`SUPPORT.md`](.github/SUPPORT.md)                              | Where to get help with this repository - the right channel for every kind of question.                                                               |
| [`template-sync`](.github/template-sync)                        | Every path tannergolden/path ships, and whether &#x1F504; Template Sync, when you run it, keeps it current in this repository.                       |
| [`template-sync.md`](.github/template-sync.md)                  | How this repository takes its template's later fixes when you run &#x1F504; Template Sync, what you control, and what waits on you.                  |
| [`TEMPLATE_INIT`](.github/TEMPLATE_INIT)                        | This repository has not been initialised yet.                                                                                                        |
| [`VULNERABILITY_REPORT.yml`](.github/VULNERABILITY_REPORT.yml)  | Report a suspected vulnerability privately, so the maintainers can fix it before it is made public.                                                  |

<!-- AUTO-INDEX:END -->

---

## 🤝 Getting Involved

- **Questions**: [`SUPPORT.md`](/.github/SUPPORT.md) says where to ask.
- **A bug or an idea**: open an issue from one of the forms.
- **A change**: [`CONTRIBUTING.md`](/.github/CONTRIBUTING.md) explains how,
  every change follows the
  [standards](https://github.com/tannergolden/standards/blob/Development/docs/README.md)
  by link, and every contribution follows the
  [code of conduct](/.github/CODE_OF_CONDUCT.md).
- **Who decides**: [`GOVERNANCE.md`](/.github/GOVERNANCE.md) names the
  maintainers.

---

## 🛡️ Security

Report a vulnerability privately, never in an issue:
[`SECURITY.md`](/.github/SECURITY.md) says how, and how fast a fix follows.

---

## ⚖️ Licence

The Golden Path is released under the terms in [LICENSE](/LICENSE).

---

<!-- markdown:trophies:start -->
<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/level.svg"><img src="assets/trophies/level-day.svg" alt="tannergolden/path: level 20, 6,758 XP, case 27% complete, released 32 days ago"></picture>
  <picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/next-up.svg"><img src="assets/trophies/next-up-day.svg" alt="Next up: Active Days to Bronze 60%, Regulars 40%, By the Book II 39%"></picture>
</p>

<p align="center">
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-stars"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/stars.svg"><img src="assets/trophies/stars-day.svg" alt="Stars trophy: Unranked, 0, 0% to Bronze"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-forks"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/forks.svg"><img src="assets/trophies/forks-day.svg" alt="Forks trophy: Unranked, 0, 0% to Bronze"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-contributors"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/contributors.svg"><img src="assets/trophies/contributors-day.svg" alt="Contributors trophy: Bronze, 2, 0% to Silver, top 43%"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-commits"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/commits.svg"><img src="assets/trophies/commits-day.svg" alt="Commits trophy: Bronze, 196, 24% to Silver, top 3.1%, up 1 this week"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-releases"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/releases.svg"><img src="assets/trophies/releases-day.svg" alt="Releases trophy: Bronze, 1, 0% to Silver, top 10%"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-merged"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/merged.svg"><img src="assets/trophies/merged-day.svg" alt="Merged PRs trophy: Unranked, 0, 0% to Bronze"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-resolved"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/resolved.svg"><img src="assets/trophies/resolved-day.svg" alt="Issues Resolved trophy: Unranked, 0, 0% to Bronze"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-active"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/active.svg"><img src="assets/trophies/active-day.svg" alt="Active Days trophy: Unranked, 18 days, 60% to Bronze"></picture></a>
</p>

<details>
<summary><b>Achievements</b> · 28 of 100 earned · next: Active Days to Bronze, 60%</summary>

<p align="center"><b>Launch</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-first-release"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-release.svg"><img src="assets/trophies/achievements/first-release-day.svg" alt="First Release: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-filed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/filed.svg"><img src="assets/trophies/achievements/filed-day.svg" alt="Filed: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-first-tag"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-tag.svg"><img src="assets/trophies/achievements/first-tag-day.svg" alt="First Tag: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-named"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/named.svg"><img src="assets/trophies/achievements/named-day.svg" alt="Named: earned, Common"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-first-fork"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-fork.svg"><img src="assets/trophies/achievements/first-fork-day.svg" alt="First Fork: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-first-merge"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-merge.svg"><img src="assets/trophies/achievements/first-merge-day.svg" alt="First Merge: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-first-star"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-star.svg"><img src="assets/trophies/achievements/first-star-day.svg" alt="First Star: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-first-watcher"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/first-watcher.svg"><img src="assets/trophies/achievements/first-watcher-day.svg" alt="First Watcher: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-front-door"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/front-door.svg"><img src="assets/trophies/achievements/front-door-day.svg" alt="Front Door: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-outside-help"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/outside-help.svg"><img src="assets/trophies/achievements/outside-help-day.svg" alt="Outside Help: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-poster"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/poster.svg"><img src="assets/trophies/achievements/poster-day.svg" alt="Poster: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-stranger-report"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/stranger-report.svg"><img src="assets/trophies/achievements/stranger-report-day.svg" alt="Stranger Report: 0% (0 of 1)"></picture></a>
</p>

<p align="center"><b>Health</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-gatekeeper"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/gatekeeper.svg"><img src="assets/trophies/achievements/gatekeeper-day.svg" alt="Gatekeeper: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-locksmith"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/locksmith.svg"><img src="assets/trophies/achievements/locksmith-day.svg" alt="Locksmith: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-paperwork"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/paperwork.svg"><img src="assets/trophies/achievements/paperwork-day.svg" alt="Paperwork: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-support-line"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/support-line.svg"><img src="assets/trophies/achievements/support-line-day.svg" alt="Support Line: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-auto-pilot"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/auto-pilot.svg"><img src="assets/trophies/achievements/auto-pilot-day.svg" alt="Auto-pilot: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-changelog"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/changelog.svg"><img src="assets/trophies/achievements/changelog-day.svg" alt="Changelog: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-form-filler"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/form-filler.svg"><img src="assets/trophies/achievements/form-filler-day.svg" alt="Form Filler: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-house-rules"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/house-rules.svg"><img src="assets/trophies/achievements/house-rules-day.svg" alt="House Rules: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-welcome-mat"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/welcome-mat.svg"><img src="assets/trophies/achievements/welcome-mat-day.svg" alt="Welcome Mat: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-well-formed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/well-formed.svg"><img src="assets/trophies/achievements/well-formed-day.svg" alt="Well-Formed: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-clean-bill"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/clean-bill.svg"><img src="assets/trophies/achievements/clean-bill-day.svg" alt="Clean Bill: earned, Common"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-documented"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/documented.svg"><img src="assets/trophies/achievements/documented-day.svg" alt="Documented: earned, Common"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-licensed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/licensed.svg"><img src="assets/trophies/achievements/licensed-day.svg" alt="Licensed: earned, Common"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-label-maker"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/label-maker.svg"><img src="assets/trophies/achievements/label-maker-day.svg" alt="Label Maker: 36% (9 of 25)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-open-hand"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/open-hand.svg"><img src="assets/trophies/achievements/open-hand-day.svg" alt="Open Hand: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-protected"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/protected.svg"><img src="assets/trophies/achievements/protected-day.svg" alt="Protected: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-roadmap"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/roadmap.svg"><img src="assets/trophies/achievements/roadmap-day.svg" alt="Roadmap: 0% (0 of 5)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-town-hall"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/town-hall.svg"><img src="assets/trophies/achievements/town-hall-day.svg" alt="Town Hall: 0% (0 of 1)"></picture></a>
</p>

<p align="center"><b>Craft</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-follows-the-standards"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/follows-the-standards.svg"><img src="assets/trophies/achievements/follows-the-standards-day.svg" alt="Follows the Standards: earned, Legendary"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-golden-path"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/golden-path.svg"><img src="assets/trophies/achievements/golden-path-day.svg" alt="Golden Path: earned, Legendary"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-ready-room"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/ready-room.svg"><img src="assets/trophies/achievements/ready-room-day.svg" alt="Ready Room: earned, Epic"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-by-the-book"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/by-the-book.svg"><img src="assets/trophies/achievements/by-the-book-day.svg" alt="By the Book I: earned, Rare, 39% to By the Book II"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-signed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/signed.svg"><img src="assets/trophies/achievements/signed-day.svg" alt="Signed I: earned, Rare, 10% to Signed II"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-small-steps"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/small-steps.svg"><img src="assets/trophies/achievements/small-steps-day.svg" alt="Small Steps: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-test-suite"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/test-suite.svg"><img src="assets/trophies/achievements/test-suite-day.svg" alt="Test Suite: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-wired"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/wired.svg"><img src="assets/trophies/achievements/wired-day.svg" alt="Wired: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-squeaky"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/squeaky.svg"><img src="assets/trophies/achievements/squeaky-day.svg" alt="Squeaky: earned, Common"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-green-machine"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/green-machine.svg"><img src="assets/trophies/achievements/green-machine-day.svg" alt="Green Machine: 17% (17 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-release-notes"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/release-notes.svg"><img src="assets/trophies/achievements/release-notes-day.svg" alt="Release Notes: 10% (1 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-semver"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/semver.svg"><img src="assets/trophies/achievements/semver-day.svg" alt="Semver: 10% (1 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-containerized"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/containerized.svg"><img src="assets/trophies/achievements/containerized-day.svg" alt="Containerized: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-gitmoji"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/gitmoji.svg"><img src="assets/trophies/achievements/gitmoji-day.svg" alt="Gitmoji: 0% (0 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-packager"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/packager.svg"><img src="assets/trophies/achievements/packager-day.svg" alt="Packager: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-prerelease"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/prerelease.svg"><img src="assets/trophies/achievements/prerelease-day.svg" alt="Prerelease: 0% (0 of 1)"></picture></a>
</p>

<p align="center"><b>Community</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-regulars"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/regulars.svg"><img src="assets/trophies/achievements/regulars-day.svg" alt="Regulars: 40% (2 of 5)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-crew"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/crew.svg"><img src="assets/trophies/achievements/crew-day.svg" alt="Crew: 20% (1 of 5)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-ten-strong"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/ten-strong.svg"><img src="assets/trophies/achievements/ten-strong-day.svg" alt="Ten Strong: 20% (2 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-answered"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/answered.svg"><img src="assets/trophies/achievements/answered-day.svg" alt="Answered: 0% (0 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-fast-reply"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/fast-reply.svg"><img src="assets/trophies/achievements/fast-reply-day.svg" alt="Fast Reply: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-good-first-issues"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/good-first-issues.svg"><img src="assets/trophies/achievements/good-first-issues-day.svg" alt="Good First Issues: 0% (0 of 5)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-help-wanted"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/help-wanted.svg"><img src="assets/trophies/achievements/help-wanted-day.svg" alt="Help Wanted: 0% (0 of 5)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-long-thread"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/long-thread.svg"><img src="assets/trophies/achievements/long-thread-day.svg" alt="Long Thread: 0% (0 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-mentor"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/mentor.svg"><img src="assets/trophies/achievements/mentor-day.svg" alt="Mentor: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-org-backed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/org-backed.svg"><img src="assets/trophies/achievements/org-backed-day.svg" alt="Org Backed: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-outside-merges"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/outside-merges.svg"><img src="assets/trophies/achievements/outside-merges-day.svg" alt="Outside Merges: 0% (0 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-popular-opinion"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/popular-opinion.svg"><img src="assets/trophies/achievements/popular-opinion-day.svg" alt="Popular Opinion: 0% (0 of 50)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-reviewed"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/reviewed.svg"><img src="assets/trophies/achievements/reviewed-day.svg" alt="Reviewed: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-talkative"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/talkative.svg"><img src="assets/trophies/achievements/talkative-day.svg" alt="Talkative: 0% (0 of 1,000)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-triage"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/triage.svg"><img src="assets/trophies/achievements/triage-day.svg" alt="Triage: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-well-maintained"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/well-maintained.svg"><img src="assets/trophies/achievements/well-maintained-day.svg" alt="Well Maintained: 0% (0 of 25)"></picture></a>
</p>

<p align="center"><b>Reach</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-big-name"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/big-name.svg"><img src="assets/trophies/achievements/big-name-day.svg" alt="Big Name: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-cloned"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/cloned.svg"><img src="assets/trophies/achievements/cloned-day.svg" alt="Cloned: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-downloaded"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/downloaded.svg"><img src="assets/trophies/achievements/downloaded-day.svg" alt="Downloaded: 0% (0 of 1,000)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-fork-magnet"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/fork-magnet.svg"><img src="assets/trophies/achievements/fork-magnet-day.svg" alt="Fork Magnet: 0% (0 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-forked-far"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/forked-far.svg"><img src="assets/trophies/achievements/forked-far-day.svg" alt="Forked Far: 0% (0 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-living-forks"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/living-forks.svg"><img src="assets/trophies/achievements/living-forks-day.svg" alt="Living Forks: 0% (0 of 10)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-referred"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/referred.svg"><img src="assets/trophies/achievements/referred-day.svg" alt="Referred: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-registry"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/registry.svg"><img src="assets/trophies/achievements/registry-day.svg" alt="Registry: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-star-of-the-week"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/star-of-the-week.svg"><img src="assets/trophies/achievements/star-of-the-week-day.svg" alt="Star of the Week: 0% (0 of 50)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-stargazer-streak"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/stargazer-streak.svg"><img src="assets/trophies/achievements/stargazer-streak-day.svg" alt="Stargazer Streak: 0% (0 of 12)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-trending"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/trending.svg"><img src="assets/trophies/achievements/trending-day.svg" alt="Trending: 0% (0 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-used-by"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/used-by.svg"><img src="assets/trophies/achievements/used-by-day.svg" alt="Used By: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-visited"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/visited.svg"><img src="assets/trophies/achievements/visited-day.svg" alt="Visited: not measured yet"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-watched"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/watched.svg"><img src="assets/trophies/achievements/watched-day.svg" alt="Watched: 0% (0 of 25)"></picture></a>
</p>

<p align="center"><b>Rhythm</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-night-shift"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/night-shift.svg"><img src="assets/trophies/achievements/night-shift-day.svg" alt="Night Shift: earned, Rare"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-alive"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/alive.svg"><img src="assets/trophies/achievements/alive-day.svg" alt="Alive: earned, Uncommon"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-long-game"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/long-game.svg"><img src="assets/trophies/achievements/long-game-day.svg" alt="Long Game: 33% (1 of 3)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-weekend-project"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/weekend-project.svg"><img src="assets/trophies/achievements/weekend-project-day.svg" alt="Weekend Project: 19% (5 of 26)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-streak"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/streak.svg"><img src="assets/trophies/achievements/streak-day.svg" alt="Streak: 13% (4 of 30)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-monthly-release"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/monthly-release.svg"><img src="assets/trophies/achievements/monthly-release-day.svg" alt="Monthly Release: 8% (1 of 12)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-weekly-beat"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/weekly-beat.svg"><img src="assets/trophies/achievements/weekly-beat-day.svg" alt="Weekly Beat: 7% (4 of 52)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-big-week"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/big-week.svg"><img src="assets/trophies/achievements/big-week-day.svg" alt="Big Week: 6% (6 of 100)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-marathon-day"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/marathon-day.svg"><img src="assets/trophies/achievements/marathon-day-day.svg" alt="Marathon Day: 2% (1 of 50)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-comeback"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/comeback.svg"><img src="assets/trophies/achievements/comeback-day.svg" alt="Comeback: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-friday-deploy"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/friday-deploy.svg"><img src="assets/trophies/achievements/friday-deploy-day.svg" alt="Friday Deploy: 0% (0 of 1)"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-same-day-fix"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/same-day-fix.svg"><img src="assets/trophies/achievements/same-day-fix-day.svg" alt="Same-Day Fix: 0% (0 of 10)"></picture></a>
</p>

<p align="center"><b>Secret</b></p>
<p align="center">
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-birthday"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/birthday.svg"><img src="assets/trophies/achievements/birthday-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-constellation"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/constellation.svg"><img src="assets/trophies/achievements/constellation-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-friday-the-13th"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/friday-the-13th.svg"><img src="assets/trophies/achievements/friday-the-13th-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-full-house"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/full-house.svg"><img src="assets/trophies/achievements/full-house-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-ghost"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/ghost.svg"><img src="assets/trophies/achievements/ghost-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-green-wall"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/green-wall.svg"><img src="assets/trophies/achievements/green-wall-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-leap-day"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/leap-day.svg"><img src="assets/trophies/achievements/leap-day-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-midnight-oil"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/midnight-oil.svg"><img src="assets/trophies/achievements/midnight-oil-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-new-year"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/new-year.svg"><img src="assets/trophies/achievements/new-year-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-palindrome"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/palindrome.svg"><img src="assets/trophies/achievements/palindrome-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-round-number"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/round-number.svg"><img src="assets/trophies/achievements/round-number-day.svg" alt="Secret achievement"></picture></a>
  <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository-the-answer"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/trophies/achievements/the-answer.svg"><img src="assets/trophies/achievements/the-answer-day.svg" alt="Secret achievement"></picture></a>
</p>

</details>

<p align="center"><sub>Refreshed daily by <a href="https://github.com/tannergolden/markdown">tannergolden/markdown</a> · Every trophy and achievement, what it is for and how to earn it: <a href="https://github.com/tannergolden/markdown/blob/HEAD/docs/references/Catalogue.md#repository">the catalogue</a>. Click any card for its entry.</sub></p>
<!-- markdown:trophies:end -->

<!-- markdown:footer:start -->
<div align="center">

<a href="#top">
<picture>
  <source media="(max-width: 585px) and (prefers-color-scheme: dark)" srcset="assets/banners/footer-narrow-dark.svg">
  <source media="(max-width: 585px)" srcset="assets/banners/footer-narrow-day.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/banners/footer-dark.svg">
  <img alt="Structure, not opinions. Standards by link, not by copy. Back to Top. Built with love by @tannergolden. Last updated November 19, 2026." src="assets/banners/footer-day.svg">
</picture>
</a>

<a href="https://github.com/tannergolden/path/issues"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/banners/link-issues-dark.svg"><img alt="Issues" src="assets/banners/link-issues-day.svg"></picture></a>
<a href="https://github.com/tannergolden/path/pulls"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/banners/link-pull-requests-dark.svg"><img alt="Pull Requests" src="assets/banners/link-pull-requests-day.svg"></picture></a>
<a href="https://github.com/tannergolden/path/releases"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/banners/link-releases-dark.svg"><img alt="Releases" src="assets/banners/link-releases-day.svg"></picture></a>
<a href="https://github.com/tannergolden/path/actions"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/banners/link-actions-dark.svg"><img alt="Actions" src="assets/banners/link-actions-day.svg"></picture></a>

</div>
<!-- markdown:footer:end -->
