<!--
title: '📦 PACKAGES'
description: 'Workspace packages, one folder each, for when a second consumer needs shared code.'
tags: [packages, workspaces, monorepo, scaffold]
category: docs
-->

<div align="center">

# 📦 PACKAGES

<a name="top"></a>

**Shared libraries, one folder each, for the day a second consumer needs them.**

_Single-package until a second consumer arrives._

</div>

---

## 💡 What This Folder Is For

Reserved for a workspace layout: shared libraries, each in its own folder with
its own manifest, consumed by more than one deployable. Most projects never need
it, and until this one does, `src/` is where the code goes.

The fill-in [Packages & Workspaces](../docs/templates/technical/Packages-&-Workspaces.md)
standard sets the bar for starting: two deployables that share non-trivial code,
a library that needs its own version, or build times that demand per-package
caching. It also records the tool that runs the workspace and the boundary rules
between packages.

This directory is **yours from the first commit**. Nothing upstream will ever
write to it or delete from it.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                    | Purpose    |
| :----------------------- | :--------- |
| [`README.md`](README.md) | This file. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push: a package appears the
moment its folder exists, described by the README that package carries for its
own files.

---

<div align="center">

**Split a package out when two things need it, not before.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
