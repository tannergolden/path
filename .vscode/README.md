<!--
title: '⚙️ EDITOR SETTINGS'
description: 'The VS Code settings and extension recommendations this repository shares, and why every other file in this folder stays out of git.'
tags: [vscode, editor, configuration, onboarding]
category: docs
-->

<div align="center">

# ⚙️ EDITOR SETTINGS

<a name="top"></a>

**The VS Code defaults every contributor shares, and the line git draws around them.**

_Shared on purpose. Personal by default._

</div>

---

## 💡 What This Folder Is For

VS Code reads this folder when it opens the repository, inside the
[development container](../.devcontainer/README.md) as much as outside it.
What is committed here is what the whole team should get: format on save, a
final newline, and a short list of extensions that help whatever language you
write.

**Which formatter runs on save is a per-language choice**, so nothing here sets
one. Your language's extension supplies it.

---

## 📝 File Log

| File                                 | Purpose                                                                                                                                                  |
| :----------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`extensions.json`](extensions.json) | The extensions VS Code offers to install: EditorConfig, GitLens, Error Lens, Code Spell Checker, Markdown All in One, markdownlint, and Even Better TOML |
| [`settings.json`](settings.json)     | Format and fix on save, a final newline, trimmed whitespace, telemetry set off, version-control clutter hidden, and the spell checker's project words    |
| [`README.md`](README.md)             | This log                                                                                                                                                 |

Add a row here in the same change that adds a file, and read the next section
before you do.

---

## 🌿 What Git Keeps Here

> [!IMPORTANT]
> **Everything in this folder is ignored except what `.gitignore` names.** It
> keeps `extensions.json`, `settings.json`, `launch.json`, `tasks.json`, and
> this README. Any other file is silently left out by `git add`, with no warning
> and no error, which is how a personal setting stays personal.

`launch.json` (debug configurations) and `tasks.json` (build, test, and run
tasks) are tracked so a team can share them, but neither ships, because both
depend on the language. Add them once the project has something to launch.

Markdown lint rules do not live here. They are in `.markdownlint.json` at the
root, where the editor extension and a command-line run read the same file.

Both JSON files here are JSON with comments, which VS Code reads and the
repository validator parses the same way.

---

<div align="center">

**Commit what the team shares. Keep what is yours.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../LICENSE).

</div>
