<!--
title: '🛡️ OPERATIONS TEMPLATES'
description: 'Fill-in standards for keeping the project safe once it runs: how an incident is declared, run and closed, and a threat model of what the project protects and how.'
type: index
-->

<div align="center">

# 🛡️ OPERATIONS TEMPLATES

<a name="top"></a>

**How this project runs an incident, and what it defends, decided ahead of time.**

_Decide the response before the alert fires._

</div>

---

## 💡 What This Folder Is For

The fill-in standards for keeping the project safe once it runs: who does what
when something breaks, who is told, and a threat model that names what the
project protects, who could attack it, and which control answers each threat.
Each decision is marked by `[square brackets]` until your project makes it.

Copy a file out to `docs/operations/` under the same name, then replace every
bracket. The seed here stays pristine.

Two forms that fill up over time sit one level up: a [Runbook](../Runbook.md)
for each routine task or known failure, and a [Post-Mortem](../Post-Mortem.md)
after each incident. The controls this template already ships, from the secret
scan to the release attestation, are listed in the threat model, so the work
left is the part only your project knows.

---

## 📝 File Log

<!-- AUTO-INDEX:BEGIN dir=. style=log -->

| Entry                                          | Purpose                                                                                                                                                                                                                                                            |
| :--------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Incident-Response.md`](Incident-Response.md) | How this project declares, runs and closes an incident: severity levels, roles, who is told, the hand-off for security incidents, and the post-mortem. Fill it in before the first incident, and open it the moment one starts.                                    |
| [`README.md`](README.md)                       | This file.                                                                                                                                                                                                                                                         |
| [`Threat-Model.md`](Threat-Model.md)           | What this project protects, who could attack it and where, and the control that answers each threat, ending in what users can and cannot rely on. Fill it in before the first release, and review it on the cadence it sets and whenever the architecture changes. |

<!-- AUTO-INDEX:END -->

🗂️ Machined Indexes redraws this log after every push, from each template's own
frontmatter.

---

## 🔗 See also

- [Template catalogue](../README.md) - the level above: every seed, and when to reach for it
- [Operations & Security](https://github.com/tannergolden/standards/blob/Development/docs/operations/README.md) - the shared guardrails: protection, dependencies, secrets and troubleshooting

---

<div align="center">

**A response agreed in advance, and every threat given an owner.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
