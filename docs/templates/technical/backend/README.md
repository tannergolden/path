<!--
title: '📡 BACKEND TEMPLATES'
description: 'Logs the fill-in standards for backend services: API design, authentication and security, and schemas and validation.'
tags: [templates, backend, api, security]
category: docs
-->

<div align="center">

# 📡 BACKEND TEMPLATES

<a name="top"></a>

**How services talk, who they let in, and what they accept at the boundary.**

_Decide the contract before the first endpoint._

</div>

---

## 💡 What This Folder Is For

The fill-in standards for the backend: how its interfaces are shaped, how it
decides who may do what, and how it checks everything that crosses its edge.
Each decision is marked by `[square brackets]` until your project makes it.

Copy a file out to `docs/technical/backend/` under the same name, then replace
every bracket. The seed here stays pristine.

---

## 📝 File Log

| File                                                           | Decides                                                                                                  |
| :------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| [`API-Design-Standards.md`](API-Design-Standards.md)           | Protocol and interface specification, data representation, endpoint strategy, errors, limits, versioning |
| [`Authentication-&-Security.md`](Authentication-&-Security.md) | Authentication, token and session lifecycle, authorization, perimeter and transport security, auditing   |
| [`Schema-&-Validation.md`](Schema-&-Validation.md)             | Where validation runs, domain property rules, sanitization, input and output schemas, localization       |
| [`README.md`](README.md)                                       | This log. It is not a seed, and is not copied out                                                        |

Add a row here in the same change that adds a file.

---

## 🔗 See also

- [Technical templates](../README.md) - the level above, and every other area
- [Template catalogue](../../README.md) - every seed, and when to reach for it

---

<div align="center">

**One contract, held at every boundary.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
