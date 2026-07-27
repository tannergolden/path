<!--
title: '🔄 MIGRATION POLICIES'
description: 'Policies for writing, reviewing, and rolling back schema migrations.'
tags: [database, migrations, policy, schema]
category: docs
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🔄 MIGRATION POLICIES

<a name="top"></a>

**Evolving the schema with zero-downtime protocols and transactional safety.**

_Safe evolution. Expand-and-contract. Zero-loss backups._

</div>

---

## 🎯 Our Evolution Philosophy

We treat database migrations as high-risk, high-reward events. Our goal is to evolve the data schema in a way that minimizes downtime, avoids destructive modifications, and ensures that the state can be recovered or reverted at any time.

- **Immutability**: Migration scripts are never modified once they reach the integration branch.
- **Safety**: Destructive changes always follow a multi-phase "Expand and Contract" pattern.
- **Automation**: migrations are applied automatically through verified pipeline gates.

---

## 🛠️ 1. Migration Management

How we coordinate schema transitions.

- **Tooling Engine**: `[Flyway | Liquibase | ORM Handlers]`
- **Versioning Logic**: `[Timestamp-based (recommended) | Sequential]`
- **Execution Hook**: `[Pipeline Step (recommended) | App Startup]`

---

## 🌊 2. Standard Workflow

The lifecycle of a schema change from intent to production.

1. **Origin**: `[Generate script via CLI or manual creation]`
2. **Local Validation**: `[Execution of UP and DOWN logic in dev environment]`
3. **Peer Audit**: `[Mandatory SQL review for indexing and locking risks]`
4. **Integration**: `[Promotion through Preview to Release]`

---

## 💥 3. Breaking Change Protocol

Mitigating risk for high-volume or structural modifications.

| Phase             | Action                    | Purpose                                     |
| :---------------- | :------------------------ | :------------------------------------------ |
| **1. Expand**     | Add new column/table.     | Introduce change without breaking old code. |
| **2. Dual-Write** | Write to both paths.      | Populate new storage while maintaining old. |
| **3. Migrate**    | Backfill historical data. | Ensure data parity.                         |
| **4. Contract**   | Remove old path.          | Clean up debt after full transition.        |

---

## 🌱 4. Seeding & Reference Data

Managing the baseline data across environments.

- **Static Seeds**: `[System-critical lookup data, e.g., Country Codes]`
- **Ephemeral Seeds**: `[Anonymized developer sets for local testing]`
- **Idempotency**: `[Ensuring scripts can be run repeatedly without duplication]`

---

## 🛡️ 5. Backup & Recovery

Protecting the system's most critical assets.

- **Cadence**: `[Daily Snapshots | Continuous Write-Ahead Logging]`
- **Retention**: `[Policy for historical archival]`
- **Recovery Exercise**: `[Scheduled 'Restore and Verify' procedures]`

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Safe evolution. Predictable migrations.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
