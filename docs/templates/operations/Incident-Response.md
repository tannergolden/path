<!--
title: '🚨 INCIDENT RESPONSE'
description: 'How this project declares, runs and closes an incident: severity levels, roles, who is told, the hand-off for security incidents, and the post-mortem. Fill it in before the first incident, and open it the moment one starts.'
type: template
-->

<div align="center">

# 🚨 INCIDENT RESPONSE

<a name="top"></a>

**Who declares an incident, who runs it, and who is told, at every severity.**

_Declare early. Downgrade freely._

</div>

---

> [!NOTE]
> **How to use**: copy this file to `docs/operations/Incident-Response.md`, the same path minus `templates/`, and replace every `[bracket]`. The seed here stays pristine. Fill it in before the first incident: in the middle of one, nobody has time to decide who is in charge.

---

## 🎯 Our Response Intent

An incident is anything that harms users, their data or their trust in the project, or is about to: an outage, lost or exposed data, a broken release, a leaked credential, an exploited vulnerability. This document decides in advance how one is declared, who runs it, who is told and how it ends, so the first minutes go to the problem.

- **Declare early**: an incident declared and then downgraded costs minutes. One declared late costs the first hour.
- **One lead**: one person decides, and everyone else reports to them.
- **Blameless**: the post-mortem names processes and safeguards, never people.

---

## 🌡️ 1. Severity Levels

When unsure between two levels, pick the higher one. The incident lead can lower it at any time; raising it later means people were told too late. Each level maps to a `priority:` label from the shared label set, which the weekly label sync in ⚖️ Governance writes to this repository.

| Level    | Means                                                    | Examples                                                          | Label                | Acknowledge       | Update every   | Mitigate within  |
| :------- | :------------------------------------------------------- | :---------------------------------------------------------------- | :------------------- | :---------------- | :------------- | :--------------- |
| **SEV1** | `[Down, or data at risk, for most users]`                | `[Every request fails; data lost or exposed; an active breach]`   | `priority: critical` | `[15 minutes]`    | `[30 minutes]` | `[4 hours]`      |
| **SEV2** | `[A major feature broken for many users, no workaround]` | `[Sign-in fails for some users; a release that will not install]` | `priority: high`     | `[1 hour]`        | `[2 hours]`    | `[1 day]`        |
| **SEV3** | `[A minor feature broken, or a workaround exists]`       | `[One integration failing; a slow page; a wrong message]`         | `priority: medium`   | `[1 working day]` | `[Daily]`      | `[1 week]`       |
| **SEV4** | `[Cosmetic, or no user impact yet]`                      | `[A new warning in the logs; a typo in the interface]`            | `priority: low`      | `[Next triage]`   | `[On change]`  | `[Next release]` |

---

## 📢 2. Declaring An Incident

- **Who may declare**: `[Anyone who notices | Any maintainer | The person on call]`. Nobody needs permission: declaring is cheap, and the lead can close a false alarm in a minute.
- **Where it is run**: `[An issue labelled with its priority | A chat channel per incident | A call, linked from the issue]`
- **Who is on call**: `[A rotation, kept in: tool | The sole maintainer, best effort | Nobody: issues are triaged on working days]`

To declare one:

1. Open `[the issue or channel]` titled `[SEV1] <what is broken, in a few words>`, with the level you chose.
2. Name the incident lead. Until someone takes over, it is whoever declared.
3. Post the first status: what is affected, the severity, and when the next update comes.
4. Start the timeline: each action and finding, with its time, in `[the issue | a shared document]`.

> [!CAUTION]
> **A suspected security incident is never declared in public.** No public issue, pull request or discussion: follow **5. Security Incidents** instead.

---

## 👥 3. Roles

| Role               | Does                                                                                                                                | Held by                |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| **Incident lead**  | Owns the response: sets the severity, decides each action, and declares it over. Directs rather than debugs, when someone else can. | `[@handle \| On call]` |
| **Communications** | Tells everyone outside the response what is happening, on the schedule for the severity, through the channels in section 4.         | `[@handle]`            |
| **Scribe**         | Keeps the timeline: every action, finding and decision, with its time. The post-mortem is written from it.                          | `[@handle]`            |

> [!NOTE]
> **A solo maintainer holds all three.** Keep the timeline anyway, one line for each action: it is what the post-mortem is written from, and the first thing lost under pressure.

To hand a role over, say so where the incident is run, such as `@from hands the lead to @to at 2:05 pm`, so nobody is left unsure who decides.

---

## 📣 4. Communication

| Audience                     | Where                                                                  | When                                                                          | By             |
| :--------------------------- | :--------------------------------------------------------------------- | :---------------------------------------------------------------------------- | :------------- |
| **Responders**               | `[The incident issue or channel]`                                      | Continuously                                                                  | Everyone       |
| **Maintainers and the team** | `[Chat channel \| Email list]`                                         | At declaration, then on the severity's update schedule                        | Communications |
| **Users**                    | `[Status page \| Announcements discussion \| Release notes \| Social]` | `[SEV1 and SEV2: at declaration and every update; SEV3 and SEV4: when fixed]` | Communications |
| **The reporter**             | The private advisory or report it came in through                      | Within the response times in `.github/SECURITY.md`                            | Incident lead  |

Every update says three things: what is affected, what is being done, and when the next update comes. Say what you know and what you do not, and never guess at a cause in public. Send each update on schedule even when nothing has changed: "No change. Next update at [time]."

---

## 🔒 5. Security Incidents

A suspected vulnerability, breach or leaked credential is handled in private until a fix is out.

1. **Keep it private.** Move the conversation out of any public issue, pull request or discussion, and hide or remove what was posted there.
2. **Take reports the way the security policy says.** `.github/SECURITY.md` sends reporters to private vulnerability reporting on a public repository, and to the Vulnerability Report form on a private one. Its response times bind this process, so keep the two documents in step.
3. **Coordinate in a draft security advisory.** Open one on the repository's **Security** tab. It gives the fix a temporary private fork to be built in, and lets you request a CVE identifier.
4. **For a leaked credential, revoke it first**, then rotate, audit and prevent, as [Security & Secrets](https://github.com/tannergolden/standards/blob/Development/docs/operations/Security-&-Secrets.md) sets out. Rewriting git history comes after revocation, never instead of it.
5. **Disclose with the fix.** Publish the advisory once the fixed release is out, credit the reporter as `.github/SECURITY.md` promises, and name the fix in the release notes.

- **Security contact**: `[@handle]`, backed up by `[@handle]`
- **A confirmed, exploitable vulnerability is**: `[SEV1 | SEV2]`

---

## 🧯 6. Containment, Recovery & Closure

1. **Contain**: stop the harm spreading before looking for the cause, by `[rolling back the release | turning off the feature flag | blocking the traffic | revoking the credential | taking the service offline]`. Prefer the step that can be undone.
2. **Recover**: bring the service and its data back to normal, by `[redeploying the last good release | restoring from backup | replaying the queued work]`. Where a [runbook](../Runbook.md) covers the failure, follow it, and finish with its verification.
3. **Close**: the incident lead declares it resolved when `[the impact has ended and the metrics have stayed normal for N minutes]`, and sends a final update to everyone who was told along the way.
4. **Learn**: every `[SEV1 and SEV2 | incident]` gets a blameless post-mortem from the [Post-Mortem](../Post-Mortem.md) template, filed in `docs/operations/post-mortems/` within `[5 working days]` of closing. Each action item in it becomes a tracked issue with an owner.

---

## 📇 7. Contacts

| Role                           | Who                  | Reach them by               | Backup         | Hours                       |
| :----------------------------- | :------------------- | :-------------------------- | :------------- | :-------------------------- |
| **Incident lead (default)**    | `[@handle]`          | `[Pager \| Chat \| Phone]`  | `[@handle]`    | `[Hours, or "best effort"]` |
| **Security contact**           | `[@handle]`          | `[Private channel]`         | `[@handle]`    | `[REPLACE_ME]`              |
| **Hosting provider**           | `[Provider support]` | `[Support portal and plan]` | `[REPLACE_ME]` | `[REPLACE_ME]`              |
| **[Key dependency or vendor]** | `[REPLACE_ME]`       | `[REPLACE_ME]`              | `[REPLACE_ME]` | `[REPLACE_ME]`              |

> [!WARNING]
> Keep personal phone numbers and private addresses out of the repository. Point to `[a private roster | the paging tool]` instead.

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Declared fast, run calmly, learned from every time.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
