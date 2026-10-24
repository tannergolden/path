<!--
title: '📒 RUNBOOK TEMPLATE'
description: 'The steps for one routine task or one known failure, written to be followed under pressure. Copy it once for each task or alert that needs a written procedure.'
type: template
-->

<div align="center">

# 📒 RUNBOOK TEMPLATE

<a name="top"></a>

**One task or one failure, the exact steps to handle it, and how to know it worked.**

_Written in daylight. Followed at 3 am._

</div>

---

> [!CAUTION]
> **How to use**: copy this file to `docs/operations/runbooks/<short-slug>.md`, one runbook for each routine task or known failure, and keep this template pristine. Write for a reader who is tired, interrupted and doing this for the first time: every step is the exact command or action and the result it should give, with nothing left to memory. Link the runbook from the alert or dashboard that sends people to it.

---

## 🚦 When To Use It

| Attribute       | Value                                                        |
| :-------------- | :----------------------------------------------------------- |
| **Kind**        | [Routine task \| Known failure]                              |
| **Trigger**     | [The alert, symptom, report or schedule that sends you here] |
| **Systems**     | [The services, environments and data these steps touch]      |
| **Owner**       | [@handle or team who keeps these steps true]                 |
| **Time to run** | [Minutes from the first step to a verified result]           |
| **Last tested** | [YYYY-MM-DD], by [drill \| real use \| dry run]              |

Use this runbook when [the symptom, in the words the alert or the report uses]. It does **not** cover [the look-alike case]: for that, use [the other runbook, or escalate].

---

## 🔥 Impact & Urgency

- **Who is affected**: [Users, systems or data, and how they notice]
- **Severity**: [SEV1 | SEV2 | SEV3 | SEV4 | Not an incident], as [Incident Response](operations/Incident-Response.md) defines the levels
- **How fast**: [Start within N minutes of the trigger | The same working day | The next maintenance window]
- **If it waits**: [What gets worse, and how quickly: a queue that fills in N hours, data lost after N days]
- **Declare an incident**: [Always | When users are affected | Never: this is routine]

---

## 🔑 Prerequisites

**Who may run it**: [Anyone on call | Maintainers only | Named people: @handle]

Check every item before the first step. A permission found missing halfway through is how a five-minute task becomes an incident.

- [ ] **Access**: [The role, account or permission needed, and how to get it in a hurry]
- [ ] **Tools**: [Each CLI, console or script, with the version where it matters]
- [ ] **Announced**: [Posted in the incident channel | Nothing to announce for a routine run]
- [ ] **Safety net**: [A backup taken | The scheduled job paused | Nothing needed]

---

## 🪜 Steps

Run the steps in order, and compare each result with its **Expect** before going on. If a result does not match, stop and go to **Rollback / Abort** below. Write every value out in full: "restart the service" leaves the reader to guess which service, on which host, with which command.

1. **[Name of the step]**

   ```bash
   [The exact command, with every value written out]
   ```

   **Expect**: [The output, state or screen that means it worked]

2. **[Name of the step]**: [The exact action, such as the console page, the setting and the value to enter]

   **Expect**: [What changes, and where you see it]

3. **[Name of the step]**

   ```bash
   [The exact command]
   ```

   **Expect**: [The result]. **If instead** [a known wrong result], [what it means, and the step or runbook to go to next].

---

## ✅ Verification

The task is done, or the failure is fixed, only when every check below passes.

- [ ] [A command and its expected output, a request that succeeds, or a dashboard reading]
- [ ] [The alert has cleared, or the metric is back under its threshold for N minutes]
- [ ] [The person who reported it confirms, where there is one]

---

## ↩️ Rollback / Abort

- **Stop when**: [a result does not match its Expect | an error you do not recognise | more than N minutes have passed]
- **Safe to stop after**: [the steps that change nothing, so stopping there needs no undo]
- **Say where you stopped**: post the last step you completed in [the incident channel], so whoever picks it up starts from there.

To undo the steps that changed something, newest first:

1. **Undo step [N]**: [the exact command or action]. **Expect**: [the state before step N]
2. **Undo step [N - 1]**: [the exact command or action]. **Expect**: [the state before it]

---

## 📣 Escalation

| When                                            | Who                | How                                            |
| :---------------------------------------------- | :----------------- | :--------------------------------------------- |
| A step fails, or its result does not match      | [@handle or team]  | [Page \| Chat channel \| Phone]                |
| Data may be lost, or it may be a security issue | [Security contact] | [The private channel in `.github/SECURITY.md`] |
| No answer within [N] minutes                    | [Next contact]     | [How to reach them]                            |

The full contact list, and who does what once an incident is declared, are in [Incident Response](operations/Incident-Response.md).

---

## 📎 Related Links

- **Alert**: [The alert that triggers this runbook, and where it is defined]
- **Dashboard**: [Where to watch the effect of each step]
- **Post-mortems**: [The post-mortems where this runbook was written or used]
- **Code and configuration**: [The paths and settings the steps touch]

---

## 🗓️ Revision History

Add a row each time the runbook is used, tested or changed. When a step did not match what happened, fix the step the same day.

| Date         | Change                                                                 | By        |
| :----------- | :--------------------------------------------------------------------- | :-------- |
| [YYYY-MM-DD] | [Written \| Steps changed \| Tested in a drill \| Used in an incident] | [@handle] |

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Exact steps, expected results, and a way back.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in this repository's LICENSE.

</div>
