<!--
title: '🔄 TEMPLATE SYNC'
description: 'How this repository takes its template''s later fixes when you run 🔄 Template Sync, what you control, and what waits on you.'
tags: [template, sync, automation, workflows]
category: docs
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🔄 TEMPLATE SYNC

<a name="top"></a>

**This repository can take its template's later fixes, whenever you ask, as a pull request you merge.**

_On request. Per file. Merged with your changes. Nothing you did not choose._

</div>

---

## 💡 What It Does

This repository was generated from a template. Generating hands over a copy and then forgets it, so
every fix the template got afterwards would otherwise stay there: a workflow stub, a repository
script, a seeded document. **🔄 Template Sync** carries those fixes here - when you ask it to.

**It never runs on its own.** Run **🔄 Template Sync** from the Actions tab and it fetches the
template's latest release, then merges each file the template changed with whatever you changed in
that file. The result arrives as **one pull request** on `chore/template-sync`, labeled
`automated`, which later runs update in place. Nothing is ever pushed to your branch, and nothing
you did not choose is synced. If you never run it, this repository never changes.

| File                                  | What it is                                                    | Yours to edit?        |
| :------------------------------------ | :------------------------------------------------------------ | :-------------------- |
| `.github/workflows/template-sync.yml` | The button: it runs only when you run it                      | Yes                   |
| `.github/template-sync`               | The list: every path the template ships, and whether it syncs | Yes - that is its job |
| `.github/template-sync.lock`          | Where each file was last synced from                          | Never                 |
| `.github/template-sync.md`            | This page                                                     | A sync updates it     |

The engine itself lives in [`tannergolden/standards`](https://github.com/tannergolden/standards) and
is called, never copied, so a fix to how syncing works reaches this repository on its next run.

---

## 📋 Choosing What Syncs

`.github/template-sync` names every path the template ships, in `.gitignore` syntax:

```gitignore
# --- Kept current ---------------------------------------------------------
/.github/workflows/checks.yml
/.github/scripts/validate-repository.py

# --- Yours: seeded once, never synced ------------------------------------
#/README.md
#/LICENSE

# --- Your rules ----------------------------------------------------------
```

**A line naming a path keeps it current. `#/path` - a hash with no space - leaves it to you.**

| You want                                      | Do this                                                       |
| :-------------------------------------------- | :------------------------------------------------------------ |
| To keep a file as your own from now on        | Put a `#` in front of its line                                |
| The template to keep it current again         | Take the `#` away                                             |
| To stop a whole folder                        | Add a rule under **Your rules**, such as `!/.devcontainer/**` |
| A file the template left to you, kept current | Take the `#` away from its line                               |
| To stop syncing altogether                    | Delete `.github/workflows/template-sync.yml`                  |

Changes to the list take effect on the next sync you run. A few things worth knowing:

- **Your rules come last and win**, exactly as later lines do in a `.gitignore`. Start every
  pattern with `/`, or it matches that name in every folder.
- **Every sync redraws the list** from the template's latest one and keeps every choice you made.
  Anything you wrote that the template did not moves under **Your rules**, and stays.
- **A deleted line reads as switched off**, and comes back with a `#` in front of it, so the list
  always shows everything the template ships.
- **A file the template adds arrives as a new line** in the same pull request as the file.
- **Deleting the list does not switch syncing off.** The next run restores it with the template's
  defaults and syncs nothing else that time. Delete the stub to remove the option altogether.

---

## 🔀 What The Pull Request Tells You

| In the pull request                            | Means                                                                   |
| :--------------------------------------------- | :---------------------------------------------------------------------- |
| ✅ Updated to the template's version           | You had not changed the file, so it takes the template's version        |
| 🔀 Merged with your changes                    | You both changed it, in different places; both changes are kept         |
| 🆕 Added                                       | The template added it, written in your identity                         |
| 🚚 Moved by the template                       | The template moved it; your changes moved with it                       |
| 🗑️ Removed, as the template removed it         | You had not changed it, so it goes too                                  |
| 📌 Kept as yours after the template removed it | You had changed it, so it stays - yours from now on                     |
| 🙈 Switched off, because you deleted it        | It stays deleted, and its line in the list gains a `#`                  |
| ♻️ Switched back on and restored               | You took the `#` away from a file you had deleted, so it is back        |
| ✋ Held off, as you chose                      | The template reshaped its list; your choice is written back by name     |
| ⚠️ Needs you                                   | A conflict - see below                                                  |
| ⏸️ Waiting on a token                          | A workflow file - see below                                             |
| ⛔ Skipped as unsafe                           | A path that would reach outside this repository, so it is never written |

Files the template added or changed arrive **in your identity**: the footers name you, the licence
holder is you, and links to the shared repositories the template relies on stay as they are.

---

## ⚠️ When Something Waits On You

**A conflict** means you and the template changed the same lines. Your file is left exactly as it
was - no conflict markers, nothing half-merged - and the pull request shows the template's change.
Make the lines it changed match the template's, and the next sync stops asking; or put a `#` in
front of the file in the list to keep your version for good. Make that change on your default
branch, never on `chore/template-sync`: each sync rewrites that branch from your default branch, and
what was committed to it goes with it.

**A workflow file** under `.github/workflows/` cannot be written with the default token. It waits,
named, until a `BOT_ACCESS_TOKEN` secret exists - see below.

While anything waits, one issue stays open - **🔄 Template sync is waiting on you** - listing every
waiting file and why. Each sync you run redraws it, and the first one that finds nothing left
closes it.

> [!TIP]
> **Merging a sync pull request with a conflict still in it is safe.** Each file remembers where it
> was last synced from, and a file that did not merge keeps its old place, so the template's change
> is offered again on every run you make until it lands. Merge the rest; nothing is lost.

---

## 🔑 The Token

| Without a `BOT_ACCESS_TOKEN`                                       | With one                         |
| :----------------------------------------------------------------- | :------------------------------- |
| Files under `.github/workflows/` wait, named in the issue          | They arrive like any other file  |
| The pull request cannot start required checks; re-run them by hand | CI runs on it                    |
| A private template cannot be fetched at all                        | It can, if the token can read it |

`BOT_ACCESS_TOKEN` is the same secret every automation pull request here uses: a token with the
`repo` and `workflow` scopes, or a fine-grained one with **Contents**, **Pull requests**, **Issues**
and **Workflows** write on this repository - and **Contents** read on the template, when the
template is private. A token with the `repo` scope but not `workflow` counts as none for workflow
files: they wait, and everything else arrives.

---

## 🏷️ Template Versions

The template publishes releases as `v1.0.0`, `v1.1.0`, and so on, and moves `v1` to the latest one.
This repository follows `v1`. A new major - `v2` - is a breaking change to the scaffold, so it is
never followed on its own: change `ref:` in `.github/workflows/template-sync.yml` when you decide to.

---

## 🛡️ What It Never Does

- **Run without you.** There is no schedule: it starts only when you run it.
- **Write a conflict marker**, or touch a file it could not merge cleanly.
- **Re-create a file you deleted**, under its old name or a new one - unless you take the `#` off
  its line again.
- **Go backwards.** A repository generated between a change to the template and the release after it
  already holds that change, so it is left alone until the template releases past it.
- **Touch a file the template does not ship**, or one your list leaves to you.
- **Push to your branch.** It proposes; you merge - unless you set `automerge: true` in the stub,
  which merges a sync with nothing waiting once its checks pass.
- **Re-run initialisation**, write outside this repository, or write through a symlink.

---

## 🧰 In The Template Itself

The same stub runs differently in the template: there it **checks** that `.github/template-sync`
names every file the template ships, and fails a pull request that adds a file without a line for
it. Template releases are cut with **🏷️ Cut Release**, which only runs in the template; a merge to
the template reaches a generated repository only once a release moves `v1`.

---

## 🩺 When Something Looks Wrong

| You see                           | What to do                                                                                                                                            |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| "has not published `v1` yet"      | Nothing: the template has no release yet                                                                                                              |
| "has not been initialised yet"    | Let initialisation finish, or dispatch **🎯 Standards Lifecycle**                                                                                     |
| Workflow files keep waiting       | Add a `BOT_ACCESS_TOKEN` with the workflow scope                                                                                                      |
| "Failed to push branch"           | A fine-grained token needs **Workflows** write; or branch protection blocks `chore/template-sync`                                                     |
| "Could not open the pull request" | Turn on **Allow GitHub Actions to create and approve pull requests**, or add a `BOT_ACCESS_TOKEN`                                                     |
| "Could not fetch" the template    | The token cannot read it: a private template needs read access, and an expired `BOT_ACCESS_TOKEN` fails even for a public one. Renew it, or delete it |
| "already holds a newer version"   | Nothing: this repository is ahead of the template's last release                                                                                      |
| The same conflict on every run    | It is waiting on you: make its lines match the template's, or put a `#` before it                                                                     |
| The lock is refused               | It was edited by hand: restore it from history                                                                                                        |

The full standard - how each file is decided, how it is tested, what template authors must do - is
[🔄 Template Sync](https://github.com/tannergolden/standards/blob/Development/docs/distribution/automation/Template-Sync.md)
in the standards.

---

<div align="center">

**One copy at the start. Every fix after it, when you want it. Nothing you did not choose.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../LICENSE).

</div>
