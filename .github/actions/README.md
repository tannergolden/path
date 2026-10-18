<!--
title: '🎬 REPOSITORY ACTIONS'
description: 'The composite actions this repository keeps for its own workflows, and for any other repository that calls them.'
tags: [github-actions, composite-action, workflows, automation]
category: docs
-->

<div align="center">

# 🎬 REPOSITORY ACTIONS

<a name="top"></a>

**Where this repository keeps its composite actions.**

_A step written once, beside the workflows that run it._

</div>

---

## 💡 What This Folder Is For

A composite action bundles steps, and any script or config they need, into one
`uses:` line. Each one gets a folder of its own here, as
`.github/actions/<name>/action.yml`. None ships with the template: the folder is
here so every repository keeps its actions in the same place.

A workflow in this repository calls one by its path, `./.github/actions/<name>`,
after `actions/checkout`. Another repository calls it by address and tag, as
`OWNER/REPOSITORY/.github/actions/<name>@<tag>`, and GitHub fetches it from this
repository's source archive at that tag. That is why `.gitattributes` keeps this
folder in the archive while it leaves the rest of `.github/` out.

A reusable workflow, one that describes whole jobs, belongs in
[`workflows/`](../workflows/README.md) instead: GitHub reads a workflow another
repository calls from nowhere else.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                    | Purpose    |
| :----------------------- | :--------- |
| [`README.md`](README.md) | This file. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push.

---

<div align="center">

**One step, written once, called by its path.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../../LICENSE).

</div>
