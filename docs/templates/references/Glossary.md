<!--
title: '📘 GLOSSARY'
description: 'The words this project gives a meaning of its own, what each means here, and what it is not to be confused with. Add a term when a word starts to mean something specific to the project, and look one up whenever a word is unclear.'
type: template
-->

<div align="center">

# 📘 GLOSSARY

<a name="top"></a>

**Every term this project uses its own way, what it means here, and what it does not.**

_One word, one meaning._

</div>

---

> [!NOTE]
> **How to use**: copy this file to `docs/references/Glossary.md`, the same path minus `templates/`, and replace every `[bracket]`. The seed here stays pristine. Terms every repository on the standards shares, such as a ruleset or a Conventional Commit, are already in the shared [Glossary](https://github.com/tannergolden/standards/blob/Development/docs/references/Glossary.md): link there, and define here only what this project means by its own words.

---

## 🔤 Terms

In alphabetical order, one term to a row.

| Term          | Meaning here                                                                         | Not to be confused with                                    |
| :------------ | :----------------------------------------------------------------------------------- | :--------------------------------------------------------- |
| **[Account]** | [An organization that pays for the service and holds many users]                     | [User: one person who signs in]                            |
| **[Job]**     | [One unit of background work, queued by the application and run by the worker]       | [A job in a GitHub Actions workflow]                       |
| **[Term]**    | [What it means in this project, in one or two sentences, linked to where it is used] | [The everyday or industry meaning, or a neighbouring term] |

---

## 🔠 Acronyms

| Acronym          | Stands for                   | Meaning here                                             |
| :--------------- | :--------------------------- | :------------------------------------------------------- |
| **ADR**          | Architecture Decision Record | One decision, recorded in `docs/adrs/`                   |
| **[SLO]**        | [Service Level Objective]    | [The availability and latency targets this project sets] |
| **[REPLACE_ME]** | [REPLACE_ME]                 | [REPLACE_ME]                                             |

---

## ✍️ Adding A Term

1. **Add it the first time a word means something specific here**, or the second time someone asks what it means.
2. **Keep the table in alphabetical order**, one term to a row, and each meaning to one or two sentences. Link to the code, document or ADR the term names.
3. **Fill in "Not to be confused with"** wherever a reader could mistake the term: for its industry meaning, a library's meaning, or a neighbouring term in this project.
4. **Use the term exactly as written** in code, documents and the interface. Where the code uses another name, rename one of them, or list both in the row.
5. **Change a meaning in the same pull request** that changes the behaviour it describes.
6. **Do not copy a shared term**: link to the shared glossary instead.

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Words pinned down, so the code and the docs say the same thing.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
