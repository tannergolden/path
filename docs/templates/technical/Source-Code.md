<!--
title: '💻 SOURCE CODE'
description: 'Architecture and standards for the application source code.'
tags: [architecture, code, technical, structure]
category: docs
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# 💻 SOURCE CODE

<a name="top"></a>

**The primary directory for all application logic, business rules, and architectural components.**

_Logic-first. Clean architecture. Testable by design._

</div>

---

## 🎯 Purpose & Intent

This directory houses the foundational code of the project. It is structured to separate concerns and ensure that the core logic is isolated from external frameworks or delivery mechanisms.

### Source Root

- **Location**: `[src/ | app/]`
- **Language**: `[REPLACE_ME - e.g., TypeScript 5.x]`
- **Module system**: `[ESM | CommonJS]`

### Recommended Sub-structure

- **`/app`**: Application-specific logic and entry points.
- **`/lib`**: Sharable libraries and utility functions.
- **`/domain`**: Core business entities and logic (framework-agnostic).
- **`/infra`**: Implementation details (database, external APIs).

---

## 🧱 Layering Rules

Dependencies must point inward - the domain never imports from delivery or infrastructure:

1. **`domain` imports nothing** outside itself (and the standard library).
2. **`app` orchestrates**: it may import `domain` and `lib`, and receives `infra` via injection.
3. **`infra` implements** interfaces declared by `domain`/`app`; nothing imports `infra` directly except composition roots.
4. **`lib` stays generic**: if a helper knows your business rules, it belongs in `domain`, not `lib`.

> [!IMPORTANT]
> Every module must be reachable by this project's unified lint, test, and build commands - the ones CI is configured to run. Wire new tooling into those entry points rather than into bespoke scripts nobody else invokes.

---

## 📏 Quality Bar

- **Naming & style**: kebab-case files, formatter-enforced layout - see [Repository Hygiene](https://github.com/tannergolden/standards/blob/Development/docs/operations/Repository-Hygiene.md).
- **Tests live beside the layer they verify** and follow [Unit Test Standards](testing/Unit-Test-Standards.md).
- **Comments explain _why_**, decisions get an [ADR](../../adrs/Architecture-Decision-Records.md).

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Structured for logic. Built for scale.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
