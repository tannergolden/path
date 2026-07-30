<!--
title: '🧩 UNIT TEST STANDARDS'
description: 'Standards and coverage expectations for unit tests.'
tags: [testing, unit-tests, standards, quality]
category: docs
-->

<div align="center">

# 🧩 UNIT TEST STANDARDS

<a name="top"></a>

**Standards and coverage expectations for unit tests.**

_Hermetic tests. AAA Pattern. Rapid feedback._

</div>

---

## 🎯 Our Unit Testing Intent

We treat unit tests as our first line of defense. Our goal is to maintain a high-velocity, deterministic suite of tests that validate individual units of logic in isolation, ensuring that changes are safe and regressions are caught instantly.

- **Isolation**: Units are tested without external dependencies or environmental side effects.
- **Determinism**: A test must yield the same result every time, regardless of the environment.
- **Speed**: The unit suite must execute in seconds to enable a rapid developer loop.

---

## 🧪 1. The Validation Engine

Define the tools used to execute and assert logic.

| Role            | Tooling Options                    | Specification                | Description                   |
| :-------------- | :--------------------------------- | :--------------------------- | :---------------------------- |
| **Test Runner** | `[Vitest \| Jest \| JUnit]`        | Execution and reporting.     | Core execution engine.        |
| **Assertions**  | `[Expect \| Chai \| AssertJ]`      | Semantic validation results. | Rule enforcement library.     |
| **Mocking**     | `[Sinon \| Mockito \| Jest Mocks]` | Dependency isolation.        | External resource simulation. |

---

## 🎯 2. Quality Benchmarks

Target thresholds for code verification.

- **Thresholds**: `[e.g., 80% Line | 75% Branch Coverage]`
- **Enforcement**: `[Strict failure in CI on coverage drop]`
- **Safe Zones**: `[Excluding Boilerplate (DTOs, Configs, Main Entrypoints)]`

---

## 🏷️ 3. Organization & Nomenclature

Standardizing the structure and language of tests.

- **File Mapping**: `[Co-location (filename.test.ts) | Separate /tests directory]`
- **Test Anatomy**: `[describe() blocks for Units | it() blocks for Scenarios]`
- **Naming Pattern**: `[Given_State_Expect_Outcome | Verb-first (should_calculate_total)]`

---

## 🧱 4. Execution Pattern (AAA)

Utilizing a consistent structure for test logic.

```javascript
/* 1. Arrange (Given) */
// Setup state, mocks, and system-under-test.

/* 2. Act (When) */
// Execute the specific logic being validated.

/* 3. Assert (Then) */
// Verify the outcome matches expectations.
```

---

## 🃏 5. Isolation & Mocking

The protocol for handling external dependencies.

- **Mock Targets**: `[Network I/O | File System | Database Clients]`
- **State Logic**: `[Favoring real Value Objects over complex mocks]`
- **Mock Behavior**: `[Strict invocation counting vs Loose stubs]`

---

## ⚡ 6. Performance & Reliability

Ensuring a healthy, high-confidence suite.

- **Suite Time Limit**: `[Target execution for full suite, e.g., < 30s]`
- **Anti-Flake Policy**: `[Zero usage of sleep/wait | Immutable clock injection]`

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Atomic for safety. Hardened for scale.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
