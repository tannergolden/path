<!--
title: '🎭 E2E TESTING'
description: 'How end-to-end tests are organized and executed.'
tags: [testing, e2e, quality, automation]
category: docs
-->

<div align="center">

# 🎭 E2E TESTING

<a name="top"></a>

**How end-to-end tests are organized and executed.**

_Real-world scenarios. Cross-browser validation. Resilient assertions._

</div>

---

## 🎯 Our E2E Intent

We treat End-to-End (E2E) tests as our ultimate certification of system health. Our goal is to simulate real user behavior across the entire stack, ensuring that our core business journeys are functional, performant, and correctly integrated from the UI to the database.

- **User-Centric**: We test what the user sees and interacts with, not internal implementation details.
- **Resilience**: Tests are designed to handle the inherent latency and unpredictability of integrated systems.
- **Traceability**: Failures provide rich diagnostic data, including videos, screenshots, and network logs.

---

## ⚡ 1. The Automation Framework

The engine that drives our browser and system interactions.

- **Primary Tool**: `[Playwright | Cypress | Selenium]`
- **Execution Scripting**: `[Language used for scenario definitions]`
- **Mode**: `[Headless (CI) vs Headed (Local Debugging)]`

---

## 🌊 2. The "Golden Path" Scenarios

Defining the mission-critical user flows that must never fail.

1. **Authentication**: `[Identity verification, MFA, and Logout]`
2. **Transaction Integrity**: `[The primary business value flow, e.g., Checkout]`
3. **Domain Lifecycle**: `[End-to-end CRUD verification of core entities]`

---

## ⚙️ 3. Execution Environment

How we maintain a stable sandbox for integration testing.

| Attribute           | Specification                          | Policy                                 | Description                           |
| :------------------ | :------------------------------------- | :------------------------------------- | :------------------------------------ |
| **Test Target**     | `[Preview URI \| Localhost]`           | High-fidelity staging environment.     | Destination for automated tests.      |
| **Data Baseline**   | `[Seed per run \| Persistent Sandbox]` | Ensuring a predictable starting state. | Data management strategy.             |
| **Third-Party I/O** | `[Mocked Stripe \| Real Sandbox API]`  | Handling external service volatility.  | External service dependency handling. |

---

## 📸 4. Diagnostics & Artifacts

Capturing the forensic data required to debug failures.

- **Visual Evidence**: `[Automatic Screenshots & Video on Failure]`
- **Telemetry**: `[Browser Console & Network Activity Capture]`
- **Visual Regression**: `[Pixel-matching logic for UI consistency]`

---

## 🛡️ 5. Flakiness & Resilience Guardrails

Protecting the suite from false negatives.

- **Smart Selectors**: `[Prefer data-testid attributes over CSS selectors]`
- **Async Strategy**: `[Await expectations vs Fixed Sleep timers]`
- **Retry Protocol**: `[Maximum attempt count for transient failures]`

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Simulated for users. Hardened for scale.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
