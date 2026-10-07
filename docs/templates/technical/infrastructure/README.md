<!--
title: '☁️ INFRASTRUCTURE TEMPLATES'
description: 'Logs the fill-in standards for environment configuration, the delivery pipelines, and deploying and rolling back releases.'
tags: [templates, infrastructure, ci-cd, deployment]
category: docs
-->

<div align="center">

# ☁️ INFRASTRUCTURE TEMPLATES

<a name="top"></a>

**Where the project runs, how a change reaches it, and how a release is undone.**

_Every environment declared. Every deploy reversible._

</div>

---

## 💡 What This Folder Is For

The fill-in standards for everything between a merged change and a running
system: the environments and their configuration, the pipeline that certifies a
change, and the protocol that promotes and rolls back a release. Each decision
is marked by `[square brackets]` until your project makes it.

Copy a file out to `docs/technical/infrastructure/` under the same name, then
replace every bracket. The seed here stays pristine.

The shared workflows already run the checks and the release chain. These
documents record how your project configures and extends them, and what they
cannot know for you: where it is hosted, and how it recovers.

---

## 📝 File Log

| File                                                           | Decides                                                                                                   |
| :------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| [`CI-CD-Pipelines.md`](CI-CD-Pipelines.md)                     | The CI platform, the integration and delivery phases, the artifact lifecycle, and quality-gate thresholds |
| [`Deployment-Protocols.md`](Deployment-Protocols.md)           | Hosting, the release methodology, the deploy lifecycle, observability, and recovery and rollback          |
| [`Environment-Configuration.md`](Environment-Configuration.md) | Infrastructure as code, networking, resource sizing, configuration and secrets, and resilience            |
| [`README.md`](README.md)                                       | This log. It is not a seed, and is not copied out                                                         |

Add a row here in the same change that adds a file.

---

## 🔗 See also

- [Technical templates](../README.md) - the level above, and every other area
- [Template catalogue](../../README.md) - every seed, and when to reach for it

---

<div align="center">

**Declared environments, rehearsed rollbacks.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
