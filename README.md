<!--
title: '🛤️ GOLDEN PATH'
description: 'A language-agnostic scaffold. Structure, community health files, and workflow triggers, with every standard followed by link rather than copied.'
tags: [template, scaffold, ci-cd, engineering-standards]
category: docs
-->


<div align="center">

# 🛤️ GOLDEN PATH

<a name="top"></a>

**The paved road to a new repository.**

_Scaffold here. Standards by link. Template fixes when you ask._

</div>

---

## 💡 What This Is

A **golden path**: the paved, supported route to a new repository. It is a
**boilerplate** - a working starting shape, already decided - not an empty
directory with instructions.

That distinction is the whole design. Two things have to be true before a
repository is any good: it has to follow sound engineering standards, and it has
to have a structure. This template supplies **both**, and supplies them
differently on purpose.

|                   | How it arrives                                                                      | Why                                                                      |
| :---------------- | :---------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| **The standards** | By link, from [`tannergolden/standards`](https://github.com/tannergolden/standards) | Shared, so a fix reaches every repository at once                        |
| **The structure** | Copied here, as real folders and files                                              | Yours from the first commit, because only you can decide what it becomes |

So you get `src/`, `tests/`, `packages/`, `benchmarks/`, `assets/`, and `docs/`
already laid out, community health files already written, and continuous
integration already wired - and none of it is enforced. A boilerplate makes the
common case free; it does not make the uncommon case impossible.

The name is the point. A golden path is not the only way to build something and
it is not compulsory. It is the way that already has the paving stones laid, so
taking it costs less than not taking it. Every file here is yours to change the
moment you have a reason to.

What it deliberately does **not** decide is the language: no build system, no
package manager, no toolchain. A structure is universal; a build is not.

**Nothing reaches in and rewrites your tree, and the scaffold can still keep
up - when you ask.** The standards stay current because they are linked. The
files copied here - the workflow stubs, the repository scripts, the seeded
documents - are brought up to date only when you run **🔄 Template Sync** from
the Actions tab: it proposes the template's later fixes as one pull request,
merged with whatever you changed. It never runs on its own, so a repository
whose owner never runs it never changes. Nothing is pushed to your branch,
nothing you deleted comes back, and editing anything after generating has no
upstream consequence. [`.github/template-sync`](.github/template-sync) names
every file it may touch: put a `#` in front of a line to keep that file yours.
The structure folders are on it switched off, so a sync never touches them
unless you take the `#` away.
[How it works](.github/template-sync.md).

---

## 🔀 Fork, Or "Use This Template"

Both buttons hand you every file in this repository. They differ in exactly one
thing: whether your copy keeps a **link back to this one**.

**Fork it** when you want this repository's history, and to pull later changes
back down through git. A fork remembers where it came from, so `Sync fork` and
`git pull upstream` both work.

**Click "Use this template"** when you want the current version as a starting
point. You get a clean repository with a single `Initial commit` and no parent,
and later fixes to the scaffold can still reach it - whenever you run
**🔄 Template Sync**, as a pull request, one file at a time, merged with your
changes. It is the route this template is built for, and the one
**🚀 The First Five Minutes** assumes further down.

|                              | Fork                                              | "Use this template"                     |
| :--------------------------- | :------------------------------------------------ | :-------------------------------------- |
| **Link back to here**        | Kept - `Sync fork` works                          | None                                    |
| **Later scaffold fixes**     | `Sync fork`: every change, or none                | 🔄 Template Sync: per file, as a PR     |
| **History**                  | Every commit this repository has                  | One `Initial commit`                    |
| **Actions**                  | **Disabled until you enable them**, per GitHub    | On from the start                       |
| **Issues**                   | Off by default                                    | On                                      |
| **A new pull request**       | Defaults to targeting **this** repository         | Targets yours                           |
| **Visibility**               | Public, and a fork's visibility cannot be changed | Yours to choose                         |
| **Your contributions graph** | Commits to a fork do not count                    | They count                              |

### What a fork actually buys you

Less than it looks, and it is worth knowing why before choosing it. **The
standards reach both routes identically.** Every `uses:` in these workflows
points at `tannergolden/standards@v1`, a moving major tag, so every fix in the
v1 line arrives the moment it is published whether you forked or generated -
which is what **Staying current takes no effort** describes further down.
Forking does not make you more current; that part is already free.

What a fork does sync is the **scaffold**: the fifteen stub workflows, the
directory layout, the seeded documents. A generated repository can take the
stub and seed fixes too - every stub but `cut-release.yml`, while the layout
stays yours - whenever you run 🔄 Template Sync, so what a fork adds is the
shared history - and with it, every change at once or none. In a fork, delete
`.github/workflows/template-sync.yml`: `Sync fork` already carries the same
changes, and two routes to them would only collide.

> [!IMPORTANT]
> **Initialisation and `Sync fork` want opposite things.** Once Actions are
> running, the `init` job claims the repository - it rewrites the identity to
> your account and **force-pushes the default branch**. That force-push is the
> moment your history stops being a fast-forward of this one's, so `Sync fork`
> begins offering to discard your commits rather than catch you up.
>
> Neither is misbehaving: a fork wants a shared history, and initialisation
> deliberately rewrites one. If you want the fork **and** the shared history,
> delete `.github/TEMPLATE_INIT` before enabling Actions. That skips
> initialisation entirely, and the file itself lists what you then set by hand.

> [!TIP]
> **There is a third route.** Generate with "Use this template", then add this
> repository as a second remote:
>
> ```bash
> git remote add template https://github.com/tannergolden/path
> git fetch template
> ```
>
> Cherry-pick whatever you want from it, whenever you want it, with none of the
> fork's costs - no disabled Actions, no force-push collision, and no pull
> request that opens against somebody else's repository by mistake. For the
> template's own fixes, prefer 🔄 Template Sync: a cherry-pick arrives in the
> template author's identity, unmerged with your edits.

> [!NOTE]
> **Neither route carries the template flag over.** Ten of the fifteen stubs
> are guarded by `!github.event.repository.is_template`, and 🏷️ Cut Release by
> its inverse - which is what keeps those ten silent here and Cut Release silent
> everywhere else. `prune-runs.yml`, `verify-stubs.yml` and `auto-index.yml` run
> on both sides, and 🔄 Template Sync reads the same flag to decide whether to
> check its list or to sync. A fork inherits that flag no more than a generated
> repository does, so your copy lands on the right side of every guard.

---

## ⚠️ CI Is Green, And Only Half Configured

The `ci` job in `checks.yml` runs the commands **you** give it, and it **fails when every stage
resolves to nothing** rather than reporting a green check that checked nothing.
That leaves a new scaffold in an awkward spot: there is no source code to lint
yet, but "no source code" is not the same as "nothing to validate".

So `lint-command` starts out pointing at
[`.github/scripts/validate-repository.py`](.github/scripts/validate-repository.py),
which checks the files that exist from the first commit - every YAML and JSON
file parses, every workflow `uses:` is pinned to a tag or a commit rather than a
branch, no CRLF or stray whitespace. A typo in any of those breaks something
quietly, so this is a real gate, not a placeholder that returns zero.

**It is still only half the story.** Nothing is testing or building your project,
because your project does not exist yet. Open `.github/workflows/checks.yml` and
replace that command once it does:

```yaml
jobs:
  ci:
    uses: tannergolden/standards/.github/workflows/ci.yml@v1
    with:
      lint-command: 'golangci-lint run'
      test-command: 'go test ./...'
      build-command: 'go build ./...'
```

Any language, any tool. A few starting points:

| Stack  | `lint-command`                      | `test-command`  | `build-command`         |
| :----- | :---------------------------------- | :-------------- | :---------------------- |
| Go     | `golangci-lint run`                 | `go test ./...` | `go build ./...`        |
| Rust   | `cargo clippy -- -D warnings`       | `cargo test`    | `cargo build --release` |
| Python | `ruff check .`                      | `pytest`        | `python -m build`       |
| Node   | `npm run lint`                      | `npm test`      | `npm run build`         |
| .NET   | `dotnet format --verify-no-changes` | `dotnet test`   | `dotnet build`          |

You do not have to fill in all of them - one real command is enough.

> [!TIP]
> Prefer a `Makefile`? Add one with `lint`, `test`, `build`, and `docs` targets,
> then delete the `with:` block entirely: the `ci` job falls back to `make <target>`
> whenever no explicit command is given.

---

## 🤖 No AI Infrastructure, On Purpose

This template ships **no agent instruction files and no agent configuration**.
That is a decision, not an omission.

Agent instructions are **always loaded**. Every byte is paid on every session, in
every repository, forever. They also carry conventions that belong to a project
rather than to a scaffold: how you write commits, what must never be touched by
hand, which commands actually build the thing. Shipping a default set makes that
choice on your behalf, invisibly, and the usual result is a file nobody wrote and
nobody trusts.

**Nothing here depends on them.** Initialisation, CI, the rulesets, the release
flow and every workflow behave identically with none of it present. Adding it is
additive, and so is taking it away.

When you do want it, there are two supported routes and no wrong answer:

| Route                                                       | You commit                  | Updates arrive by                            |
| :----------------------------------------------------------- | :-------------------------- | :------------------------------------------- |
| **By hand**                                                 | the instructions themselves | you editing them                             |
| **[`tannergolden/intelligence`](https://github.com/tannergolden/intelligence)** | one workflow stub | a release moving a tag, with no pull request |

Writing them by hand suits conventions that are specific to one project. The
publisher suits several repositories that share one set, for the same reason the
workflows here are called rather than copied: the law lives in one place, and a
fix reaches everything pinned to it. Its README carries the stub to copy and the
version to pin.

> [!IMPORTANT]
> **Whichever route you take, confirm the tools you actually use load what you
> wrote.** They do not agree on which filename to read, and some will not find a
> shared file at all unless a small per-tool file points them at it. Instructions
> nothing loads are worse than none, because they look finished.

> [!TIP]
> **Either route stays reversible.** What you write by hand is yours to delete.
> What the publisher delivers is listed with digests in a lockfile, so the
> inventory of what arrived is also the manifest for removing it.

---

## 🎉 What Happens On Its Own

**"Use this template" substitutes nothing.** GitHub copies every file verbatim,
so a generated repository would otherwise carry the template author's licence
holder, funding target, and documentation footers forever.

The `init` job in `lifecycle.yml` fixes that on its own, once. It rewrites the identity to
**your** account, rewrites the bare "Initial commit" into a proper Conventional
Commit describing the new repository, and then deletes `.github/TEMPLATE_INIT`,
which is what stops it ever running again.

Two things it deliberately leaves alone. The first is any reference to a
repository on the template's account - `tannergolden/standards`, whose shared
workflows every repository calls, the agent instruction publisher, and this
template itself - because each belongs to that account rather than yours, so it
is correct for everyone. The second is your email address, which GitHub keeps
private. Commits use the `noreply` form, which always routes to you and
publishes nothing.

> [!NOTE]
> GitHub does not reliably fire an event when a repository is created from a
> template. If nothing happens within a minute or two, dispatch **🎯 Standards
> Lifecycle** from the Actions tab - the `init` job inside it is what claims the
> repository. Running it twice is harmless: the marker file is what permits
> it, and it is only removed on success.

---

## 🚀 The First Five Minutes

> [!TIP]
> Every step below, plus signing and the token, is kept as one canonical
> checklist in the standards:
> [🙋 What You Do By Hand](https://github.com/tannergolden/standards/blob/Development/docs/introduction/What-You-Do-By-Hand.md).

1. **Check that init ran** - `.github/TEMPLATE_INIT` should be gone and the
   `LICENSE` should carry your name and the current year. If not, dispatch
   **🎯 Standards Lifecycle** from the Actions tab.
2. **Sign your commits off.** `git commit -s` adds the `Signed-off-by` trailer
   that the DCO check requires. Once branch protection is on, a commit without
   it blocks the merge. `git config alias.ci 'commit -s'` and forget about it.
3. **Configure the `ci` job in `checks.yml`**, as above, once you have
   something to build.
4. **Apply the settings, then the protection** - run **🎯 Apply Standards**
   from the Actions tab. `apply-settings` writes the repository settings
   (squash-only merges, head branches deleted on merge, auto-merge, the
   security features); `apply-rulesets` writes branch protection.
   **Both ship switched OFF, and `dry-run` ships on.** Turning `dry-run` off
   on its own applies only the labels, on a green run that looks like it did
   everything - so tick the job you want as well. Do settings first: they are
   checkboxes, while a wrong ruleset blocks every merge. See the token note
   below before you do.
5. **Enable private vulnerability reporting** under Settings → Security. The
   issue chooser gains a "Report a vulnerability" entry automatically, which is
   why no security contact link is hard-coded.
6. **Uncomment the rules you want in `.github/CODEOWNERS`**, replacing
   `@your-org/your-team` with a real owner. A rule naming an owner without write
   access is a GitHub error, which is why every rule ships commented out.
7. **Enable ecosystems in `.github/dependabot.yml`** as you add manifests. Only
   `github-actions` is on, because it is the only one guaranteed to apply.
8. **Add a `BOT_ACCESS_TOKEN` secret** so 🔄 Template Sync, whenever you run
   it, can update the workflow stubs too - the default token cannot write
   `.github/workflows/`, so without it those files wait in an issue instead.
   While you are there, put a `#` in front of anything in
   `.github/template-sync` you want to own outright.
9. **Replace this README.** Everything above describes the template, not your
   project. Nothing rewrites it for you, because only you know what this
   repository is for. The sections worth keeping are the workflow table and
   the token note; the rest is scaffolding that has done its job.

> [!IMPORTANT]
> **🎯 Apply Standards needs a token for two of its three jobs.** Applying the
> label taxonomy needs nothing. **Writing the settings and the rulesets** each
> need a token with administration write as `ADMIN_TOKEN`. Without it, those
> jobs stop with a sentence naming the missing token instead of a bare `403`.
>
> A fine-grained token scoped to your repositories generated from the
> templates, with **Administration: Read and write** and nothing else, is all
> it needs. Step-by-step:
> [Creating the ADMIN_TOKEN](https://github.com/tannergolden/standards/blob/Development/docs/operations/Branch-Protection.md#-creating-the-admin_token).
> You can skip it entirely by applying the settings and rulesets yourself,
> where your own rights are already enough.

---

## 📦 What's Inside

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                       | Purpose                                                                                                                                |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------- |
| [`.devcontainer/`](.devcontainer/README.md) | The language-neutral development container this repository ships, and how to give it the toolchain your project needs.                 |
| [`.github/`](.github/)                      | Community health files, forms, CODEOWNERS, Dependabot, scripts and workflows - logged below                                            |
| [`.vscode/`](.vscode/README.md)             | The VS Code settings and extension recommendations this repository shares, and why every other file in this folder stays out of git.   |
| [`assets/`](assets/README.md)               | Where this project keeps what presents it: four folders to start, a name ready for every other kind, and the rules every file follows. |
| [`benchmarks/`](benchmarks/README.md)       | The benchmark suites and recorded results that defend the performance budgets of this project.                                         |
| [`docs/`](docs/README.md)                   | Where this project keeps its own documents, and where the engineering standards it follows actually live.                              |
| [`packages/`](packages/README.md)           | Workspace packages, one folder each, for when a second consumer needs shared code.                                                     |
| [`src/`](src/README.md)                     | The application source, split into three layers whose dependencies point inward.                                                       |
| [`tests/`](tests/README.md)                 | The test suites, from isolated units to whole user journeys, and how CI comes to run them.                                             |
| [`.editorconfig`](.editorconfig)            | Editor defaults every editor honours: UTF-8, LF, a final newline, and indentation per language                                         |
| [`.env.example`](.env.example)              | Environment variable template for this project.                                                                                        |
| [`.gitattributes`](.gitattributes)          | Git attributes - line endings, diffs, and what counts as binary                                                                        |
| [`.gitignore`](.gitignore)                  | &#x1F5C4;&#xFE0F; Universal Ignore Patterns                                                                                            |
| [`.markdownlint.json`](.markdownlint.json)  | Repository-wide markdownlint rules. Discovered by mechanism, which is why this lives at the root.                                      |
| [`LICENSE`](LICENSE)                        | MIT License                                                                                                                            |
| [`README.md`](README.md)                    | This file.                                                                                                                             |

<!-- AUTO-INDEX:END -->

The root carries only what a tool discovers there by mechanism.

**Every folder carries a `README.md` that logs each file inside it**, with one
exception. GitHub shows a README in `.github/` in place of this page, so that
folder's own files are logged here instead. 🗂️ Machined Indexes redraws both
tables after every push:

<!-- AUTO-INDEX:BEGIN dir=./.github style=log -->

| Entry                                                           | Purpose                                                                                                                             |
| :-------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| [`DISCUSSION_TEMPLATE/`](.github/DISCUSSION_TEMPLATE/README.md) | The discussion category forms, each bound by its file name to the category it shapes.                                               |
| [`ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/README.md)           | The issue forms a reporter chooses from, and the chooser configuration that offers them.                                            |
| [`scripts/`](.github/scripts/README.md)                         | The checks this repository runs on its own configuration, and the tests that guard them.                                            |
| [`workflows/`](.github/workflows/README.md)                     | Every workflow in this repository: the name it shows in the Actions tab, what triggers it, and what it does.                        |
| [`CODE_OF_CONDUCT.md`](.github/CODE_OF_CONDUCT.md)              | The code of conduct governing participation in this project.                                                                        |
| [`CODEOWNERS`](.github/CODEOWNERS)                              | CODEOWNERS - Folder-based ownership rules                                                                                           |
| [`CONTRIBUTING.md`](.github/CONTRIBUTING.md)                    | How to contribute, covering branching, commits, code style, testing, and the pull-request process.                                  |
| [`dependabot.yml`](.github/dependabot.yml)                      | Dependabot - automated dependency updates                                                                                           |
| [`FUNDING.yml`](.github/FUNDING.yml)                            | &#x1F496; Funding Options                                                                                                           |
| [`GOVERNANCE.md`](.github/GOVERNANCE.md)                        | How this project is led, who decides what, how access continues, and the review and security standards every change meets.          |
| [`pull_request_template.md`](.github/pull_request_template.md)  | This template becomes the body of your pull request.                                                                                |
| [`release.yml`](.github/release.yml)                            | GitHub auto-generated release notes configuration.                                                                                  |
| [`SECURITY.md`](.github/SECURITY.md)                            | Supported versions and how to report vulnerabilities privately.                                                                     |
| [`SUPPORT.md`](.github/SUPPORT.md)                              | Where to get help with this repository - the right channel for every kind of question.                                              |
| [`template-sync`](.github/template-sync)                        | Every path tannergolden/path ships, and whether &#x1F504; Template Sync, when you run it, keeps it current in this repository.      |
| [`template-sync.md`](.github/template-sync.md)                  | How this repository takes its template's later fixes when you run &#x1F504; Template Sync, what you control, and what waits on you. |
| [`TEMPLATE_INIT`](.github/TEMPLATE_INIT)                        | This repository has not been initialised yet.                                                                                       |

<!-- AUTO-INDEX:END -->

---

## 🌿 How The Workflows Work

Your repository holds **triggers**. The logic lives in
[`tannergolden/standards`](https://github.com/tannergolden/standards) and is
pulled in by `uses:`. GitHub only runs a workflow that lives in the repository
being pushed to, which is why these fifteen small files exist here at all. They
are grouped by what they do - everything that verifies a change in one file,
everything that reacts to humans in another - so one push produces one run
with every check in it, not four runs to read separately.

| Workflow                   | Gives you                                                         |
| :------------------------- | :---------------------------------------------------------------- |
| `checks.yml`               | The gates: lint/test/build, secret scan, CodeQL, workflow lint    |
| `governance.yml`           | PR title and DCO checks, onboarding, triage, stale sweep, slash commands |
| `release.yml`              | Draft notes, publish assets, registries, prune superseded releases |
| `maintenance.yml`          | Prunes stale deployments; deletes draft releases on request        |
| `prune-runs.yml`           | Prunes workflow run history, with its logs and artifacts          |
| `lifecycle.yml`            | Claims this repository once; tells you when a new major exists    |
| `dependabot-automerge.yml` | Approves and queues Dependabot's patch and minor updates          |
| `ci-failure-alert.yml`     | Opens an issue when a watched workflow fails, closes it on green  |
| `apply-standards.yml`      | Dispatch-only. The label taxonomy and branch protection           |
| `auto-format.yml`          | Formats what a push touched                                       |
| `preview-deploy.yml`       | Deploys pushes to a preview target, once one is configured        |
| `verify-stubs.yml`         | Proves every job's permission ceiling matches its called workflow |
| `auto-index.yml`           | Redraws every folder log and index after a push, as a pull request |
| `template-sync.yml`        | Proposes the template's later fixes as one pull request, when run |
| `cut-release.yml`          | Template only. Publishes the releases generated repositories follow |

**Do not rename the job ids** `ci` and `secrets` (in `checks.yml`) or `pr`
(in `governance.yml`). A called workflow reports its checks as
`<job id> / <job name>`, so branch protection depends on them - the file a
job lives in does not matter, but its id does.

Every workflow ships installed, and **almost all of them are inert here on
purpose**: nearly every job carries an `is_template` guard, so it is silent
in this template and comes alive in every repository generated from it. Three
run in the template exactly as they will in yours - `prune-runs.yml`, because a
template accumulates run history like any other repository, `verify-stubs.yml`,
because a stub with a wrong ceiling should be caught here rather than
downstream, and `auto-index.yml`, because the template's own folder logs need
keeping too. Two more run here differently: `template-sync.yml` checks that the
template's list names every file it ships instead of syncing, and
`cut-release.yml` runs only here, publishing the releases your copy follows.
Delete any file that does not fit your project - each one is yours, and nothing
reinstalls it: 🔄 Template Sync switches a deleted file off rather than bringing
it back.

> [!IMPORTANT]
> **The guard covers the required checks too.** `ci`, `secrets` and `pr` -
> the three job ids branch protection names - are guarded like everything
> else, so they do not run while a repository is marked as a template. That
> is right for this one, which has no source code to check. But if you keep
> your own repository flagged as a template and apply the rulesets from step
> 4, every pull request will wait forever on three checks that never report.
> Un-flag it, or leave those checks out of the ruleset.

### Staying current takes no effort

`@v1` is a **moving major tag**. Every fix and feature in the v1 line reaches
this repository the moment it is published - no pull request, no update
command, nothing to maintain. Breaking changes never arrive that way, because a
new major is a different tag.

That leaves exactly one gap, and the `standards` job in `lifecycle.yml` fills
it: when `v2` is published it opens **one issue** telling you, and changes
nothing. Adopting a
major is a decision, not a chore.

The files copied here - the stubs themselves among them - cannot follow a tag.
They keep up a different way, and only when you ask: see
**🔄 Template Sync: Fixes When You Ask** below.

Almost nothing here pins a third-party action, either. Every `uses:` in the
stubs points at `tannergolden/standards`, so the SHA pins behind them are
maintained once, there, rather than in every repository built from this one.
The exception is `verify-stubs.yml`, which runs steps of its own and pins
`actions/checkout` to a commit three times. Those three are why
`.github/dependabot.yml` ships with `github-actions` enabled: it keeps them
current, and it is the one ecosystem that is correct for every repository
from the moment it is generated.

> [!NOTE]
> **If this repository goes quiet for 60 days, GitHub disables its scheduled
> workflows.** That is a platform rule for public repositories, not something a
> workflow can opt out of, and it takes the weekly checks sweep, the governance
> sweep, and the new-major alarm in `lifecycle.yml` with it. GitHub emails you
> when it happens, and one commit or a manual dispatch turns them back on.
>
> The safety net is that **Dependabot is not subject to that rule**. It keeps
> reading `.github/dependabot.yml`, and because a moving major tag only changes
> when the major changes, a `v2` still arrives as a pull request even with
> every cron asleep. So a dormant repository still finds out; it just finds out
> through Dependabot instead of through an issue.

If you would rather pin exact versions (`@v1.4.2`) for an auditable record of
what ran when, do that instead - Dependabot updates reusable-workflow
references natively, and the `dependabot-automerge` stub will merge them on
green CI.

---

## 🔄 Template Sync: Fixes When You Ask

This template keeps improving after you generate from it - a stub gains a
guard, the repository validator learns a check, a seeded document gets
clearer. **🔄 Template Sync** is how those fixes reach your copy, and it runs
only when you run it.

**Nothing happens on its own.** There is no schedule. When you want the
template's latest release, run **🔄 Template Sync** from the Actions tab: it
compares this repository with that release and proposes whatever changed as
**one pull request** on `chore/template-sync`, which you review and merge like
any other. If you never run it, nothing in this repository ever changes.

| It always...                     | Because                                                                                                        |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| Merges rather than overwrites    | Each file is merged with whatever you changed in it, by the same three-way merge git uses                      |
| Writes in your identity          | The template is rewritten exactly as initialisation rewrote it, so footers and contact links stay yours        |
| Leaves a conflict untouched      | A file you and the template changed in the same place stays as you have it; the pull request shows the change |
| Respects a deletion              | A file you delete is switched off, under its old name or a new one, until you take the `#` off its line again  |
| Leaves your structure alone      | `src/`, `tests/`, `packages/`, `benchmarks/`, `assets/`, this README and the licence start switched off        |

Three files describe it, and only one of them is yours to edit:

| File                                                   | What it is                                                                                         |
| :----------------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| [`.github/template-sync`](.github/template-sync)       | Every path the template ships, in `.gitignore` syntax. Put a `#` in front of a line to keep that file as yours |
| `.github/template-sync.lock`                           | Where each file was last synced from. Written by the sync alone; never edit it                     |
| [`.github/template-sync.md`](.github/template-sync.md) | The full explanation: every outcome, every option, and what to do when something waits on you      |

> [!IMPORTANT]
> **Workflow files need a `BOT_ACCESS_TOKEN`.** GitHub's default token cannot
> write anything under `.github/workflows/`, so without the secret those files
> wait - named in the pull request and in one issue, never dropped - while
> everything else arrives. With it, they arrive like any other file, and CI
> runs on the pull request.

**You follow a major, and a new one is your decision.** This template publishes
versions with 🏷️ Cut Release, moving `v1` to each new one, and a sync takes
whatever `v1` points at. A breaking change ships as `v2`, which nothing follows
until you change `ref:` in `.github/workflows/template-sync.yml`. To remove the
option altogether, delete that file.

The engine lives in [`tannergolden/standards`](https://github.com/tannergolden/standards/blob/Development/docs/distribution/automation/Template-Sync.md),
called rather than copied, like every other workflow here.

---

## 📚 The Standards

Everything about how to branch, review, release, and secure a repository lives
in the [Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
Follow it **by link**. A standard copied into your repository is a standard that
starts going stale the moment you paste it.

The one exception is [`docs/templates/`](docs/templates/README.md), which is
meant to be copied: those are fill-in documents that become _your_ project's
decisions. A fill-in **standard** instantiates at its own path minus
`templates/`; the **work-product forms** - an ADR, a post-mortem, a user
story - go where a numbered or dated record belongs instead. The
[catalogue](docs/templates/README.md) gives each destination.

---

<div align="center">

**Structure, not opinions. Standards by link, not by copy.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the MIT License.

</div>
