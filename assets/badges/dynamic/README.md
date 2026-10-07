<!--
title: '🔄 DYNAMIC BADGES'
description: 'Logs the gold-label health badges the badge kit draws into this folder, and the traffic-light rule their message colours obey.'
tags: [badges, health, assets, automation]
category: docs
-->

<div align="center">

# 🔄 DYNAMIC BADGES

<a name="top"></a>

**Health badges whose colour says something true about the repository right now.**

_Gold on the label. Traffic lights on the message._

</div>

---

## 💡 What This Folder Is For

The badge kit writes every badge with a **gold** label (`C0A062`) here. A gold
label marks live data - a build status, the age of the last commit, a score -
so its message colour is not decoration. It is restricted to the traffic-light
triad: **green** healthy, **yellow** degraded, **red** failing, and **slate**
for nothing measured yet. The kit refuses any other colour on a gold label.

Each time the kit runs it redraws these, and it commits only when something it
shows has changed.

---

## 📝 File Log

| File                     | Holds                                                                                     |
| :----------------------- | :---------------------------------------------------------------------------------------- |
| `<name>.svg`             | One per gold-label entry in `.github/badges.yml`, named after the entry, drawn by the kit |
| [`README.md`](README.md) | This log                                                                                  |

**The badges are logged by their data file, not row by row here.** Each SVG is
drawn from one entry, and the kit deletes any SVG no entry names, so the data
file is always the exact list of what this folder holds. Add a row here only for
a file the kit did not draw.

---

## 🔗 See also

- [Badges](../README.md) - both badge folders, and how to reference a badge
- [Static badges](../static/README.md) - the label colours that are not gold

---

<div align="center">

**A badge that reports health must be able to report ill health.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
