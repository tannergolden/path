<!--
title: '🛤️ GOLDEN PATH'
description: 'A language-agnostic scaffold. Structure, community health files, and workflow triggers, with every standard followed by link rather than copied.'
tags: [template, scaffold, ci-cd, engineering-standards]
category: docs
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 🛤️ GOLDEN PATH

<a name="top"></a>

**The paved road to a new repository.**

_Scaffold here. Standards by link. No engine._

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

There is also **no sync engine**. Nothing here phones home, nothing overwrites
your files later, and editing anything after generating has no upstream
consequence. The standards stay current because they are linked, not because
something reaches in and rewrites your tree.

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

Two things it deliberately leaves alone: references to
`tannergolden/standards`, which are the shared workflows every repository calls
and are correct for everyone, and your email address, which GitHub keeps
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
   security features); `apply-rulesets` writes branch protection. Both preview
   by default and change nothing until you turn `dry-run` off. Do settings
   first: they are checkboxes, while a wrong ruleset blocks every merge. See the token note below before you do.
5. **Enable private vulnerability reporting** under Settings → Security. The
   issue chooser gains a "Report a vulnerability" entry automatically, which is
   why no security contact link is hard-coded.
6. **Uncomment the rules you want in `.github/CODEOWNERS`**, replacing
   `@your-org/your-team` with a real owner. A rule naming an owner without write
   access is a GitHub error, which is why every rule ships commented out.
7. **Enable ecosystems in `.github/dependabot.yml`** as you add manifests. Only
   `github-actions` is on, because it is the only one guaranteed to apply.
8. **Replace this README.** Everything above describes the template, not your
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

| Path                         | Purpose                                                                    |
| :--------------------------- | :------------------------------------------------------------------------- |
| `.github/workflows/`         | Twelve trigger workflows. The logic lives in the standards repository      |
| `.github/`                   | Community health files, CODEOWNERS, Dependabot, release notes config       |
| `.github/scripts/`           | The repository validator the `ci` job runs until you point it at your own  |
| `docs/templates/`            | Fill-in project documents, copied out and edited as your project's own law |
| `src/`, `tests/`             | Empty structure, ready for your first file                                 |
| `assets/`                    | Logos, images, and diagrams this project owns. Empty, with a layout        |
| `packages/`, `benchmarks/`   | Reserved, empty                                                            |
| `.devcontainer/`, `.vscode/` | A working development container and editor defaults                        |

The root carries only what a tool discovers there by mechanism: `.editorconfig`,
`.gitattributes`, `.gitignore`, `LICENSE`, and this file.

---

## 🌿 How The Workflows Work

Your repository holds **triggers**. The logic lives in
[`tannergolden/standards`](https://github.com/tannergolden/standards) and is
pulled in by `uses:`. GitHub only runs a workflow that lives in the repository
being pushed to, which is why these twelve small files exist here at all. They
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

**Do not rename the job ids** `ci` and `secrets` (in `checks.yml`) or `pr`
(in `governance.yml`). A called workflow reports its checks as
`<job id> / <job name>`, so branch protection depends on them - the file a
job lives in does not matter, but its id does.

Every workflow ships installed, and **almost all of them are inert here on
purpose**: nearly every job carries an `is_template` guard, so it is silent
in this template and comes alive in every repository generated from it. Only
two jobs run in the template itself - `prune-runs.yml`, because a template
accumulates run history like any other repository, and `verify-stubs.yml`,
because a stub with a wrong ceiling should be caught here rather than
downstream. Delete any file that does not fit your project - each one is
yours, and nothing reinstalls it.

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
> sweep, and the new-major alarm in `lifecycle.yml` with it. GitHub emails you when it
> happens, and one commit or a manual dispatch turns them back on.
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

## 📚 The Standards

Everything about how to branch, review, release, and secure a repository lives
in the [Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md).
Follow it **by link**. A standard copied into your repository is a standard that
starts going stale the moment you paste it.

The one exception is [`docs/templates/`](docs/templates/README.md), which is
meant to be copied: those are fill-in documents that become _your_ project's
decisions. A fill-in document's destination mirrors its path minus `templates/`.

---

<div align="center">

**Structure, not opinions. Standards by link, not by copy.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by [@tannergolden](https://github.com/tannergolden). Distributed under the MIT License.

</div>
