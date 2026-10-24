<!--
title: '🚀 GETTING STARTED'
description: 'How to build this project from source and set up a machine to change it, with the same install, build, test and lint commands CI runs. Fill it in once the project builds, and read it before a first contribution.'
type: template
-->

<div align="center">

# 🚀 GETTING STARTED

<a name="top"></a>

**From a clean machine to a passing build, with the commands CI runs.**

_If CI can run it, so can you._

</div>

---

> [!NOTE]
> **How to use**: copy this file to `docs/introduction/Getting-Started.md`, the same path minus `templates/`, and replace every `[bracket]`. The seed here stays pristine. Each command must be the one `.github/workflows/checks.yml` gives CI, so a contributor and CI never disagree about what passing means: change both in the same pull request.

---

## 🎯 Purpose & Intent

One page that takes a newcomer from nothing to a working copy they can change and test. Filled in, it is the build-from-source instructions of the [OpenSSF Baseline](https://baseline.openssf.org/) (OSPS-DO-07.01), and the quick development setup of the [OpenSSF Best Practices badge](https://www.bestpractices.dev/) (`installation_development_quick`).

- **Exact**: every version pinned, every command the one CI runs.
- **Short**: a newcomer reaches a passing test run in `[N]` minutes.
- **Tested**: someone follows it on a clean machine `[every release | every quarter]`, and fixes what no longer works.

---

## 📋 1. Prerequisites

| Tool                           | Version                               | Needed for                         | Install                                           |
| :----------------------------- | :------------------------------------ | :--------------------------------- | :------------------------------------------------ |
| **Git**                        | `[2.x or later]`                      | Cloning and committing             | `[Package manager \| git-scm.com]`                |
| **[Language runtime]**         | `[Exact version, as pinned in: file]` | Building and running               | `[REPLACE_ME]`                                    |
| **[Package manager]**          | `[REPLACE_ME]`                        | Installing dependencies            | `[REPLACE_ME]`                                    |
| **[Container runtime]**        | `[REPLACE_ME]`                        | The dev container, if you use it   | `[Docker \| Podman \| None: use a Codespace]`     |
| **[Database, service or CLI]** | `[REPLACE_ME]`                        | `[REPLACE_ME]`                     | `[REPLACE_ME]`                                    |
| **gitleaks** (optional)        | Any recent release                    | The secret scan in the commit hook | `[Package manager \| A release from its project]` |

- **Operating systems**: `[Linux | macOS | Windows with WSL 2]`, tested on `[REPLACE_ME]`
- **Hardware**: `[Memory, disk and CPU architecture, where they matter]`

The same tools, and the commands below, are recorded for the whole project in [Technology Stack & Tooling](../technical/Technology-Stack-&-Tooling.md).

---

## 📥 2. Get The Code

```bash
git clone https://github.com/OWNER/REPOSITORY.git
cd [REPOSITORY]
```

**Or open it in the dev container.** The repository ships `.devcontainer/`: in VS Code, choose <kbd>Reopen in Container</kbd>, or open a Codespace on GitHub. It starts from a language-neutral image with git, and Python for the repository's own scripts, and its `postCreateCommand` already installs those scripts' requirements and switches on the hooks in step 3. This project adds `[the toolchain features it needs]` in `.devcontainer/devcontainer.json`, and `[the install command]` to that `postCreateCommand`, so a new container is ready to build.

---

## 🪝 3. Enable The Local Hooks

Once per clone, point git at the hooks the repository ships. The dev container does this for you.

```bash
git config core.hooksPath .github/scripts/hooks
```

They check each commit message for a Conventional Commit header and a `Signed-off-by:` trailer, and scan staged changes for secrets when gitleaks is installed. CI runs the same checks on every pull request, so a skipped hook only moves the failure later. Sign off each commit with `git commit -s`.

---

## 🏗️ 4. Install, Build, Test & Lint

Run these from the repository root, in this order. Each must be the same command as the input of the same name in `.github/workflows/checks.yml`. Where `checks.yml` gives no command, CI runs the `Makefile` target of the same name instead (`make setup`, `make build`, `make test`, `make lint`), and so do you.

| Step        | Command        | In `checks.yml` | A pass looks like                                  |
| :---------- | :------------- | :-------------- | :------------------------------------------------- |
| **Install** | `[REPLACE_ME]` | `setup-command` | `[Dependencies installed; the lockfile unchanged]` |
| **Build**   | `[REPLACE_ME]` | `build-command` | `[Output written to: dist \| build \| target]`     |
| **Test**    | `[REPLACE_ME]` | `test-command`  | `[Every test passes; exit code 0]`                 |
| **Lint**    | `[REPLACE_ME]` | `lint-command`  | `[No findings; exit code 0]`                       |

> [!NOTE]
> Until the project has commands of its own, `checks.yml` runs the template's checks on the repository's own configuration and scripts. Replace them there and here in the same pull request.

---

## ▶️ 5. Run It Locally

```bash
[REPLACE_ME - the command that starts the project]
```

- **Configuration**: copy `.env.example` to `.env.local` and set `[the variables it needs]`. Git ignores every `.env` file except the example, so real values never reach a commit.
- **Where to look**: `[http://localhost:PORT | The usage text it prints | REPLACE_ME]`
- **Sample data**: `[How to load fixtures or seed a local database, or "none needed"]`
- **Stop and reset**: `[REPLACE_ME]`

---

## 🩺 6. Common Problems

| Symptom                                              | Cause                                                         | Fix                                                                |
| :--------------------------------------------------- | :------------------------------------------------------------ | :----------------------------------------------------------------- |
| `[command not found: tool]`                          | `[The toolchain is missing, or not on PATH]`                  | `[Install the version in Prerequisites, or use the dev container]` |
| The `commit-msg` hook rejects a commit               | The message is not `type(scope): subject`, or has no sign-off | Reword it, and commit with `git commit -s`                         |
| The `pre-commit` hook says gitleaks is not installed | Staged changes were not scanned for secrets                   | Install gitleaks; CI scans every push either way                   |
| `[Tests pass locally and fail in CI]`                | `[A different runtime version, or an uncommitted lockfile]`   | `[Match the version in Prerequisites; commit the lockfile]`        |
| `[REPLACE_ME]`                                       | `[REPLACE_ME]`                                                | `[REPLACE_ME]`                                                     |

Still stuck? Ask in `[the Q&A discussions | the chat channel]`, with the command you ran, its full output and your operating system. `.github/SUPPORT.md` says where help is offered.

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Clone it, build it, test it, the way CI does.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in this repository's LICENSE.

</div>
