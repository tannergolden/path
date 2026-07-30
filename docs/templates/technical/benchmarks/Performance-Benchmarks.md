<!--
title: '⚡ PERFORMANCE BENCHMARKS'
description: 'Reference data and methodologies for performance testing.'
tags: [performance, benchmarks, metrics, testing]
category: docs
-->

<!-- markdownlint-disable MD041 -->

<div align="center">

# ⚡ PERFORMANCE BENCHMARKS

<a name="top"></a>

**The centralized suite for performance profiling, load testing, and scaling validation.**

_Metric-driven. Performance-first. Scalable by default._

</div>

---

## 🎯 Purpose & Intent

Performance is a feature with a budget. This document records **what we measure, the numbers we refuse to regress past, and how the measurements are produced** - so a "it feels slower" debate always resolves to data.

- **Budgets over vibes**: Each critical path has an explicit numeric target.
- **Reproducibility**: Benchmarks run from pinned scripts on defined hardware/CI runners.
- **Trend tracking**: Results are recorded per release, not just when problems surface.

---

## 📊 Performance Budgets

| Metric                       | Target                          | Measured by                              |
| :--------------------------- | :------------------------------ | :--------------------------------------- |
| API p95 latency              | `[REPLACE_ME - e.g., < 200 ms]` | `[k6 / autocannon / Artillery]`          |
| Throughput (sustained)       | `[REPLACE_ME - req/s]`          | Load suite below                         |
| Client bundle size (gzipped) | `[REPLACE_ME - e.g., < 250 KB]` | `[size-limit / webpack-bundle-analyzer]` |
| Web vitals (LCP / INP / CLS) | `[REPLACE_ME]`                  | `[Lighthouse CI]`                        |
| Build time (CI, cold)        | `[REPLACE_ME - minutes]`        | CI job duration                          |

---

## 🔬 Methodology

1. **Baseline**: benchmark `Development` HEAD before optimizing; commit the numbers with the change that motivated them.
2. **Load**: ramp to expected peak for `[REPLACE_ME]` minutes; record p50/p95/p99, error rate, and saturation point.
3. **Soak** (optional): hold moderate load for `[REPLACE_ME]` hours to surface leaks and drift.
4. **Compare**: a change that worsens a budgeted metric needs either a fix or an [ADR](../../../adrs/Architecture-Decision-Records.md) accepting the new budget.

> [!IMPORTANT]
> Wire the suite into the Makefile (e.g., `make bench`) and keep scenario scripts in this directory so results are reproducible by any contributor - numbers without a committed script are anecdotes.

---

## 🗃️ Recording Results

Store each run as a dated entry using the [&#x1F50E; Research Log template](../../Research-Log.md): environment, commit SHA, scenario, raw numbers, and the conclusion drawn.

---

<div align="center">

**Validated for speed. Hardened for scale.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
