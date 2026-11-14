<!--
title: '🔗 SYNCED FILES'
description: 'Which files here are kept current from other repositories, by which sync, and which parts of each are yours: read it before editing one, so an update comes from its sync and a change of your own survives the next one.'
type: reference
-->

<div align="center">

# 🔗 SYNCED FILES

<a name="top"></a>

**What arrives here from other repositories, and which parts of it are yours.**

_Update a synced file by running its sync. Change only the parts it leaves to you._

</div>

---

<!-- TEMPLATE-SYNC:BEGIN -->

## 💡 Why This Page Exists

Some files in this repository are written somewhere else and delivered here: by
the template it was generated from, by the hub that writes the rules for AI
agents, and by the standards its workflows call. Each arrives through a sync
that keeps it current, and a hand edit works against that sync. A file edited to
bring it up to date is drift the next sync has to merge, and may not be able to;
an edit inside a block a machine writes is gone the next time that machine runs.

Two habits keep this repository easy to keep current:

- **To update a synced file, run the sync that owns it**, and merge the pull
  request it opens. Never copy a newer version in by hand, or rewrite one from
  memory: the sync records where each file came from, and a copy it did not
  make reads as an edit of your own.
- **To make a change of your own, make it where the file leaves room for one**,
  and the next sync merges around it.

> [!NOTE]
> **This section is the template's.** 🔄 Template Sync keeps everything between
> this page's `TEMPLATE-SYNC` markers current. **This Repository's Own Syncs**,
> after it, is yours.

---

## 🔄 The Syncs

| Sync                 | From                                                                                                                                   | What it keeps current here                                                                                                                                                                                    | When it runs                                                                          |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------ |
| 🔄 Template Sync     | The template this repository was generated from: `tannergolden/path`, or a template built on it, as `.github/template-sync.lock` names | Every path on a line of its own, without a `#`, in the **Kept current** section of `.github/template-sync`                                                                                                    | Only when you run it, from the Actions tab: one pull request on `chore/template-sync` |
| 🔁 Intelligence Sync | `tannergolden/intelligence`, the hub                                                                                                   | The universal rules between the `INTELLIGENCE` markers in `AGENTS.md`. A first sync also creates `AGENTS.md` where there is none, folds a `CLAUDE.md` into it, and adds `docs/Prompts.md` where it is missing | Every Monday, and whenever you run it: one pull request on `chore/intelligence`       |
| 🗂️ Machined Indexes  | This repository's own files                                                                                                            | Every folder log between `AUTO-INDEX` markers                                                                                                                                                                 | After every push to the default branch: one pull request                              |
| The shared workflows | `tannergolden/standards`                                                                                                               | Nothing is copied. Each stub in `.github/workflows/` calls a standards workflow at `@v1`, so a fix reaches this repository when the standards move `v1`                                                       | With no sync at all. The stubs themselves are kept current by 🔄 Template Sync        |

⚖️ Apply Standards writes this repository's settings, rulesets and labels from
the standards: never a file, and only when you run it.

**A hidden `docs/` or `assets/` still syncs.** A repository that keeps the
template's `docs/` as `.docs/`, or its `assets/` as `.assets/`, has those files
synced where it keeps them, and no sync brings the visible folder back.
`.github/template-sync` still names them by the template's paths, such as
`/docs/README.md`, and wherever a page here names a `docs/` path, read it as
`.docs/`.

---

## 🧭 Whose Is Each Part

| What                                                                   | Whose                                                                     | Edit it?                                                                                                                                        | Kept current by      |
| :--------------------------------------------------------------------- | :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------- | :------------------- |
| Lines between `INTELLIGENCE` markers, in `AGENTS.md`                   | The hub's                                                                 | No. The next sync replaces the block, and the Machined Block Check flags the edit on its pull request first                                     | 🔁 Intelligence Sync |
| Lines between `TEMPLATE-SYNC` markers, in `AGENTS.md` and on this page | The template's                                                            | Not in place: an edit there is a conflict at the next sync, and yours stays until you settle it. Delete a section to drop it, and it stays out  | 🔄 Template Sync     |
| Lines between `AUTO-INDEX` markers, in each folder's `README.md`       | Drawn from the files beside them                                          | No. Add, rename or describe a file, and the log follows                                                                                         | 🗂️ Machined Indexes  |
| Any other file on a **Kept current** line                              | The template's, merged with yours                                         | Only for a change this repository needs. It merges at every sync, and where you and the template change the same lines, that file waits for you | 🔄 Template Sync     |
| A file on a `#/` line, under **Yours**                                 | Yours, seeded once when this repository was generated                     | Yes                                                                                                                                             | Nothing              |
| `.github/template-sync`                                                | Yours: each `#` you add or take away, and everything under **Your rules** | Yes, that is its job. Each sync redraws the rest from the template and keeps your choices                                                       | 🔄 Template Sync     |
| `.github/template-sync.lock`                                           | The sync's                                                                | No                                                                                                                                              | 🔄 Template Sync     |

---

## ✍️ Files With A Part Of Your Own

Some synced files are made to be added to. Write in the part each leaves to
you, and the sync merges around it:

| File                              | Yours                                                                                                                                                                                                                                                   | The template's or the hub's                                                                          |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------- |
| `AGENTS.md`                       | Every section after the universal rules: Commands, Definition of done, Conventions, Where things live, Gotchas, Ask first and Overrides. Change how a universal Default applies here with a line under **Overrides**; an Invariant cannot be overridden | The universal rules between `INTELLIGENCE` markers, and the sections between `TEMPLATE-SYNC` markers |
| `docs/Prompts.md`                 | Everything from **✍️ This Repository's Prompts** to the end                                                                                                                                                                                             | The Golden Path section above it                                                                     |
| `docs/Synced-Files.md`            | **This Repository's Own Syncs**, at the end                                                                                                                                                                                                             | Everything between its `TEMPLATE-SYNC` markers                                                       |
| `.github/workflows/checks.yml`    | The commands under `with:`: how this project lints, tests and builds                                                                                                                                                                                    | The rest of the stub                                                                                 |
| `.github/dependabot.yml`          | An entry for each ecosystem this project has a manifest for                                                                                                                                                                                             | The rest                                                                                             |
| `.devcontainer/devcontainer.json` | The features your toolchain needs                                                                                                                                                                                                                       | The rest                                                                                             |
| `.env.example`                    | The variable names this project reads, never their values                                                                                                                                                                                               | The rest                                                                                             |
| Each `README.md` under `docs/`    | The documents beside it, yours from the first commit                                                                                                                                                                                                    | The README itself                                                                                    |

**Keep your lines in a file the template also changes** with a note under
**Your rules** in `.github/template-sync`, such as
`# keep mine: /.github/workflows/checks.yml`: where you and the template change
the same lines, yours stand, and its other changes still arrive. **Stop syncing
a file** by putting a `#` in front of its line, or a whole folder with a rule
such as `!/docs/**`. [`.github/template-sync.md`](../.github/template-sync.md)
says how each works.

---

## ✅ Before You Edit A Synced File

1. **Find who owns it**: its line in `.github/template-sync`, and any markers
   around the lines you mean to change.
2. **If you only want it current, leave it alone.** Run the sync that owns it,
   and merge the pull request it opens.
3. **If this repository needs it different**, change only the part it leaves
   to you, or only the lines you must, and write down why where the next person
   will look: `AGENTS.md`'s **Conventions**, or an ADR.
4. **Never edit inside a machine's markers**, and never edit
   `.github/template-sync.lock`.

### 🤖 For AI Agents

- Never bring a synced file up to date by hand, from memory or by copying the
  template's version: tell your user which sync to run.
- Change a synced file only when your user asks for a change this repository
  needs, in the part the file leaves to it, and say in your report that the
  file is synced and how its next sync will treat the change.
- Never edit between `INTELLIGENCE`, `TEMPLATE-SYNC` or `AUTO-INDEX` markers or
  in `.github/template-sync.lock`, and change `.github/template-sync` only when
  your user asks.
- Running a sync opens a pull request, so run one only when your user asks for
  it.

<!-- TEMPLATE-SYNC:END -->

---

## ✍️ This Repository's Own Syncs

> [!TIP]
> **List anything this repository takes from somewhere else that the sections
> above do not cover**: a vendored library, a schema copied from an API, a file
> another repository's workflow writes. Name its source and how to bring it up
> to date. 🔄 Template Sync never writes outside its own section of this page.

---

<div align="center">

**Update by syncing. Change only what is yours.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
