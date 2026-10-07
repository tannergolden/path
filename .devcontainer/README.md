<!--
title: '🐳 DEVELOPMENT CONTAINER'
description: 'The language-neutral development container this repository ships, and how to give it the toolchain your project needs.'
tags: [devcontainer, development-environment, configuration, onboarding]
category: docs
-->

<div align="center">

# 🐳 DEVELOPMENT CONTAINER

<a name="top"></a>

**A container that can clone, edit, and commit in any language, with no toolchain yet.**

_Neutral until you name the language._

</div>

---

## 💡 What This Folder Is For

Open the repository in a dev container - <kbd>Reopen in Container</kbd> in VS
Code, or a Codespace - and this folder decides what you get: an Ubuntu base
image, git, the common shell utilities, and a handful of editor extensions that
are useful whatever you write.

**Nothing language-specific is installed, on purpose.** This scaffold does not
know what you are about to build, and a toolchain nobody needs costs every
contributor a slow rebuild.

`.gitattributes` marks this folder `export-ignore`, so `git archive` leaves it
out of a source tarball. It is for developing the project, not for shipping it.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                    | Purpose                                                |
| :--------------------------------------- | :----------------------------------------------------- |
| [`devcontainer.json`](devcontainer.json) | Development container - deliberately language-neutral. |
| [`README.md`](README.md)                 | This file.                                             |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from what each file says
about itself.

---

## ⚙️ Giving It A Toolchain

- [ ] Uncomment the feature for your language under `features` in
      `devcontainer.json`. The full catalogue is at
      [containers.dev/features](https://containers.dev/features).
- [ ] Set `postCreateCommand` to your bootstrap step, such as `npm ci`,
      `pip install -e .` or `go mod download`, so a fresh container is ready to
      build.
- [ ] Add your language's editor extension to `customizations.vscode.extensions`.
- [ ] Rebuild the container.

> [!NOTE]
> **There is no `settings` block, deliberately.** VS Code reads
> [`.vscode/settings.json`](../.vscode/settings.json) inside the container like
> anywhere else, so a copy here would be a second source of truth, and the copy
> that drifts is always the one nobody remembers.

`devcontainer.json` is JSON with comments, which is what dev containers read.
The repository validator parses it the same way, so a comment is never reported
as an error.

---

<div align="center">

**Equip it for this project, and for nothing else.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../LICENSE).

</div>
