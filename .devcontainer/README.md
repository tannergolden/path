<!--
title: '🐳 DEVELOPMENT CONTAINER'
description: 'The language-neutral development container this repository ships, and how to give it the toolchain your project needs.'
type: index
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

**Nothing for your project's language is installed, on purpose.** This
scaffold does not know what you are about to build, and a toolchain nobody
needs costs every contributor a slow rebuild.

**Python is the one exception, and it is not a language choice.** The checks
this repository runs on its own configuration are Python: the validator, the
stub checker, the commit-message hook and their tests. So the container
installs Python and the scripts' one requirement, PyYAML, and switches on the
[git hooks](../.github/scripts/hooks/README.md) when it is created. A
container that cannot run those checks cannot tell you whether CI will pass.
It also installs gitleaks from Ubuntu's archive, so the `pre-commit` hook
scans what you stage for secrets. That release trails gitleaks itself, and CI
scans every pull request with the current one.

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

🗂️ Machined Indexes redraws this log after every push to the default branch,
from what each file says about itself.

---

## ⚙️ Giving It A Toolchain

- [ ] Uncomment the feature for your language under `features` in
      `devcontainer.json`. The full catalogue is at
      [containers.dev/features](https://containers.dev/features).
- [ ] Append your bootstrap step to `postCreateCommand`, such as
      `&& npm ci`, `&& pip install -e .` or `&& go mod download`, so a fresh
      container is ready to build. Keep what is already there: it installs
      what the repository's own checks need and switches on the hooks.
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

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
