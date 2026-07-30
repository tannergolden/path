<!--
title: '📋 PROJECT TEMPLATES'
description: 'Index of the reusable document templates and when to use each one.'
tags: [templates, index, documentation, scaffold]
category: docs
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 📋 PROJECT TEMPLATES

<a name="top"></a>

**The index of copy-source templates - what each one is for and where its copies live.**

_Structured excellence. Rapid documentation. Unified standards._

</div>

---

> [!TIP]
> Use these standardized templates to bootstrap your technical work. They are designed to meet the repository's professional standards.

> [!IMPORTANT]
> **Where a project gives its agents instructions, these templates are binding rather than optional.** The convention is that an agent fills in the [📜 Implementation Plan](Implementation-Plan.md) to be filled in and **delivered to the user as a report before any non-trivial change**, and the other templates to be used at the moments they help the user steer - research before direction, design before build, post-mortem after failure.

---

## Available Templates

| Template                                                                | Purpose                                                | Copy to                                             |
| :---------------------------------------------------------------------- | :----------------------------------------------------- | :-------------------------------------------------- |
| [&#x1F4D0; Technical Design](Technical-Design.md)       | High-level system architecture and trade-offs.         | `docs/technical/designs/<slug>.md`                  |
| [&#x1F4DC; Implementation Plan](Implementation-Plan.md) | Concrete changes, sequencing, and verification.        | `docs/technical/plans/<slug>.md`                    |
| [&#x1F464; User Story](User-Story.md)                   | Requirements from the user's perspective.              | `docs/<area>/stories/<slug>.md` (or your tracker)   |
| [&#x1F50E; Research Log](Research-Log.md)               | Discovery evidence and recommendations.                | `docs/technical/research/<topic>.md`                |
| [&#x1F4C9; Post-Mortem](Post-Mortem.md)                 | Blameless incident and outcome analysis.               | `docs/operations/post-mortems/YYYY-MM-DD-<slug>.md` |
| [&#x1F4C4; ADR](ADR.md)                                 | One architecture decision, recorded durably.           | `docs/adrs/ADR-NNNN-Short-Slug.md` (next number)            |
| [&#x1F4AC; Communication](Communication.md)             | Meeting notes, status heartbeats, stakeholder updates. | reuse in issues, discussions, and reviews           |
| [&#x1F4DD; ADR index](../adrs/Architecture-Decision-Records.md) | The register every ADR is listed in.                   | already in place; add a row per decision            |

## Fill-In Technical Standards

Every document here is one you complete: either a **fill-in standard** whose decisions are marked by `[square brackets]` - a bare `[REPLACE_ME]`, a choice list like `[REST | GraphQL | gRPC]`, or a prompt like `[why]` - or a **work-product form** whose blank sections you write under (an ADR, a post-mortem, a user story). There are no index pages, deliberately - this catalogue is the index, and a second layer of navigation carrying nobody's decisions is a file that goes stale for free. A fill-in standard's destination **mirrors its path minus `templates/`**: `docs/templates/technical/backend/API-Design-Standards.md` instantiates as `docs/technical/backend/API-Design-Standards.md`. **Living inside `docs/templates/` is what marks them all as seed content**, with no in-file directive needed. Everything in this folder is **yours from the moment the repository is generated**: nothing syncs it, nothing overwrites it, and editing a file here has no upstream consequence.

| Area                                                                              | Templates                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :-------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stack & Source** | [&#x1F527; Technology Stack & Tooling](technical/Technology-Stack-&-Tooling.md), [&#x1F4BB; Source Code](technical/Source-Code.md), [&#x1F4E6; Packages & Workspaces](technical/Packages-&-Workspaces.md)                                                                                                                                                                               |
| **Interface** | [&#x1F4D0; Formatting & Standards](technical/interface/Formatting-&-Standards.md), [&#x1F58C;&#xFE0F; Styling & Theming](technical/interface/Styling-&-Theming.md), [&#x1F6E0;&#xFE0F; UI Setup & Environment](technical/interface/UI-Setup-&-Environment.md)                  |
| **Backend** | [&#x1F4E1; API Design Standards](technical/backend/API-Design-Standards.md), [&#x1F512; Authentication & Security](technical/backend/Authentication-&-Security.md), [&#x1F4CB; Schema & Validation](technical/backend/Schema-&-Validation.md)                                |
| **Database** | [&#x1F5C4;&#xFE0F; Data Models & Entities](technical/database/Data-Models-&-Entities.md), [&#x1F504; Migration Policies](technical/database/Migration-Policies.md)                                                                                                                                          |
| **Infrastructure** | [&#x2601;&#xFE0F; Environment Configuration](technical/infrastructure/Environment-Configuration.md), [&#x1F504; CI CD Pipelines](technical/infrastructure/CI-CD-Pipelines.md), [&#x1F680; Deployment Protocols](technical/infrastructure/Deployment-Protocols.md) |
| **Testing** | [&#x1F9E9; Unit Test Standards](technical/testing/Unit-Test-Standards.md), [&#x1F3AD; E2E Testing](technical/testing/E2E-Testing.md), [&#x26A1; Performance Benchmarks](technical/benchmarks/Performance-Benchmarks.md)                                                                        |

## How to Use

1. **Copy** the template to its destination above - never fill in the template file itself; your `docs/templates/` copies are seeded once and stay pristine as long as you copy rather than edit them, and the canonical originals remain in the template home (later template improvements are never re-shipped over your seeded copies, so consult upstream for the newest form).
2. **Replace** every bracketed placeholder; delete sections that genuinely don't apply.
3. **Link** the document from the pull request (or issue) it supports, so decisions stay traceable.

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Reproducible formats. Professional velocity.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
