<!--
title: '📦 PACKAGES & WORKSPACES'
description: 'Guidelines for monorepo management and package isolation.'
tags: [monorepo, packages, architecture, workspaces]
category: docs
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 📦 PACKAGES & WORKSPACES

<a name="top"></a>

**The structural home for shared libraries and modular components within a monorepo architecture.**

_Modular by design. Shared logic. Atomic versioning._

</div>

---

## 🎯 When to Reach for Workspaces

Stay single-package until you have a concrete second consumer. Adopt a workspace layout when:

- Two or more deployables must **share non-trivial code** (a design system, a domain library, generated API clients).
- You need **independent versioning** of a published library alongside an application.
- Build times demand **per-package caching** and affected-only pipelines.

---

## 🛠️ Workspace Management

- **Tool**: `[NPM Workspaces | PNPM Workspaces | Turborepo | Nx]`
- **Manifest**: `[package.json "workspaces" | pnpm-workspace.yaml]`
- **Layout**:

```txt
/ (repo root)
├── apps/
│   └── [app-name]/          # Deployable applications
└── packages/
    └── [package-name]/      # Shared libraries (each with its own package.json)
```

---

## 📐 Boundary Rules

1. **Packages never import from `apps/`** - dependencies flow from apps down into packages.
2. **Cross-package imports go through the public entry point** (`exports` in `package.json`), never deep paths.
3. **One lockfile at the root**; per-package lockfiles are forbidden to keep installs deterministic.
4. **Versioning strategy**: `[fixed/lockstep | independent (changesets)]` - record the decision in an [ADR](/docs/adrs/Architecture-Decision-Records.md).

> [!IMPORTANT]
> The unified commands must keep working from the repository root: lint, test, and build should fan out across workspaces (e.g., `npm run build --workspaces --if-present`) so CI never needs package-specific knowledge.

---

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Modular for logic. Engineered for scale.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
