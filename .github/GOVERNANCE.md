<!--
title: '🏛️ PROJECT GOVERNANCE'
description: 'How this project is led, who decides what, how access continues, and the review and security standards every change meets.'
type: standard
-->

<div align="center">

# 🏛️ PROJECT GOVERNANCE

<a name="top"></a>

**How this project is led, who decides, and how it survives any one person leaving.**

_Decisions in the open. Access that outlives individuals._

</div>

---

## 🎯 Governance Model

This project uses a **lightweight maintainer model**. A small group of **Maintainers** holds merge and administrative authority; everyone else contributes through pull requests. Decisions are made in the open on issues and pull requests, and the documented standards - not any individual's preference - are the authority.

- **Standards over opinions.** The binding rules live in the [engineering standards](https://github.com/tannergolden/standards/blob/Development/docs/README.md). When a person and a documented standard disagree, the standard wins until the standard is changed by PR.
- **Lazy consensus.** A proposal open for review with no unresolved objection from a Maintainer may be merged once CI is green. Substantive disagreements are resolved by discussion; if consensus fails, a majority of Maintainers decides.
- **Everything is a change request.** Governance itself is edited the same way as code: by pull request to this file.

---

## 👥 Roles & Responsibilities

| Role                   | Who they are                                    | Responsibilities                                                                               |
| :--------------------- | :---------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| **Maintainer**         | Listed under [Maintainers](#-maintainers) below | Review and merge PRs, cut releases, steward security response, administer repository settings. |
| **Contributor**        | Anyone who opens a PR or issue                  | Follow the [Contributing Guidelines](CONTRIBUTING.md); respond to review feedback.             |
| **Security responder** | Every Maintainer, unless one is named below     | Triage private reports per the [Security Policy](SECURITY.md) within the stated timelines.     |

Maintainers are added by consensus of the existing Maintainers after a sustained record of quality contributions, and are recorded in the table below. Give each the matching rule in [`CODEOWNERS`](CODEOWNERS) as well, so their review is requested on the code they own.

---

## 👥 Maintainers

The people who hold merge and administrative access, and how to reach them in private. The [Code of Conduct](CODE_OF_CONDUCT.md) and the [Security Policy](SECURITY.md) send people here.

| Maintainer                                       | Responsibilities                                      | Private contact                                                                                                        |
| :----------------------------------------------- | :---------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| [@tannergolden](https://github.com/tannergolden) | Maintainer, administrator, and the security responder | **Report content** on GitHub for conduct; [private vulnerability reporting](SECURITY.md) for anything security-related |

> [!IMPORTANT]
> **Keep this table true.** Add a row when someone gains merge or admin
> access and remove it the day they lose it; this list, not a team's
> membership, is what a reporter trusts. Add a private address to a row if
> reports should reach that person outside GitHub.

---

## 🔑 Access Continuity & Bus Factor

The project is designed so that **no single person is a point of failure**:

- **Administrative access is held by at least two people.** The GitHub repository (or its owning organization) MUST list two or more admins, so loss of any one account never strands the project. Record the continuity contacts in the organization's owner list.
- **No credentials live only in one head.** Release signing, publishing, and any service tokens are kept in a private store every admin can open, such as a shared password manager - never in this repository, and never tied to one person's personal account. Name the store, but never a secret, in the project's [Runbook](../docs/templates/Runbook.md) for rotating them.
- **Succession plan.** If a Maintainer becomes unavailable, the remaining Maintainers (or, if none remain, the organization owners) appoint replacements by updating the [Maintainers](#-maintainers) table, `CODEOWNERS` and the admin list. Because every standard, workflow, and guardrail is committed to the repository, a new Maintainer can take over from the documentation alone.

> [!IMPORTANT]
> **Two-factor authentication is required** for every account with commit or admin access. Enable it organization-wide (Settings → Authentication security → _Require two-factor authentication_), and prefer a security key or authenticator app over SMS. This is a standing requirement, not a suggestion.

---

## 🧑‍⚖️ Change Review Standard

Quality is enforced by process, not trust:

- **Every change lands by pull request.** Direct pushes to long-lived branches are blocked by the [rulesets](https://github.com/tannergolden/standards/blob/Development/data/README.md); CI (`🧪 Lint, Test & Build`, `🔍 Scan for Secrets`, and `✍️ DCO Sign-Off`) must be green to merge.
- **Independent review is the goal state.** Once the project has two or more Maintainers, **at least half of all non-trivial merged changes MUST be reviewed by someone other than the author** before merging. Solo-maintainer repositories run on the shipped 0-approval ruleset (CI still gates every merge) and raise the required-approval count the moment a second Maintainer exists - see [Branch Protection](https://github.com/tannergolden/standards/blob/Development/docs/operations/Branch-Protection.md).
- **A workflow must not be able to supply that review.** When the required approvals go above zero, also turn off <kbd>Settings</kbd> → <kbd>Actions</kbd> → <kbd>General</kbd> → **Allow GitHub Actions to create and approve pull requests**, and give the automation that opens pull requests a `BOT_ACCESS_TOKEN` instead. Left on, a workflow's approval counts as a review.
- **Review looks for correctness, security, and standards alignment**, using the rubric in [Pull Requests & Code Reviews](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Pull-Requests-&-Code-Reviews.md).

---

## 🌱 Onboarding New Contributors

- Start with the [Contributing Guidelines](CONTRIBUTING.md) and the setup checklist in the repository [README](../README.md).
- Good entry points are issues labelled **`good first issue`** and **`help wanted`** - small, well-scoped tasks that need no deep context. Maintainers keep a few of these open on purpose.
- Ask questions in **Discussions** (the tab on this repository; enable it under Settings → General → Features if it is not there) or via [Support](SUPPORT.md).

---

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Led in the open. Built to outlast any single maintainer.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](../LICENSE).

</div>
