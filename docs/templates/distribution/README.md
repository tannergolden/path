<!--
title: '🌿 DISTRIBUTION TEMPLATES'
description: 'Fill-in standards for releasing: how this project cuts, checks and publishes a release, and how the people who download one verify it.'
type: index
-->

<div align="center">

# 🌿 DISTRIBUTION TEMPLATES

<a name="top"></a>

**How a release is cut and published here, and how its users check it.**

_Published by the workflow. Checkable by anyone._

</div>

---

## 💡 What This Folder Is For

The fill-in standards for the last step of a change's journey: how this project
cuts, checks and publishes a release, and how someone who downloads one proves
it came from here. Each decision is marked by `[square brackets]` until your
project makes it.

Branching, versioning and the shared release workflows are written down once,
in the standards'
[Releases & Versioning](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md),
and followed by link. These documents record what your project does with them.

Copy a file out to `docs/distribution/` under the same name, then replace every
bracket. The seed here stays pristine.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                                | Purpose                                                                                                                                                                                                                                                                       |
| :--------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`README.md`](README.md)                             | This file.                                                                                                                                                                                                                                                                    |
| [`Release-Process.md`](Release-Process.md)           | How this project cuts, checks and publishes a release with the &#x1F4E6; Release workflow, adding its own choices to the shared Releases & Versioning standard. Fill it in before the first release, and follow it for every release after.                                   |
| [`Release-Verification.md`](Release-Verification.md) | How someone who downloads a release checks that it is intact and was built from this repository by the shared release workflow, using the build provenance attestation, a checksum and the SBOM. Read it before running a downloaded release, and link it from every release. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from each template's own
frontmatter.

---

## 🔗 See also

- [Template catalogue](../README.md) - the level above: every seed, and when to reach for it
- [Distribution & Workflow](https://github.com/tannergolden/standards/blob/Development/docs/distribution/README.md) - the shared workflow, from a branch to a release

---

<div align="center">

**Every release cut the same way, and checkable by anyone who downloads it.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../../../LICENSE).

</div>
