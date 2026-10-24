<!--
title: '📦 DEPENDENCY POLICY'
description: 'How this project chooses, obtains, pins and tracks its dependencies, how fast it fixes a vulnerable or wrongly licensed one, and what must be clear before a release. Fill it in before the first release, and review it on the cadence it sets.'
type: template
-->

<div align="center">

# 📦 DEPENDENCY POLICY

<a name="top"></a>

**What this project depends on, and how it keeps that safe.**

_Choose on purpose. Pin what you take. Fix on a clock._

</div>

---

> [!NOTE]
> **How to use**: copy this file to `docs/operations/Dependency-Policy.md`, the same path minus `templates/`, and replace every `[bracket]`. The seed here stays pristine. What this template already does about dependencies is filled in, so the work left is this project's own choices: its registries, its licences and its deadlines.

---

## 🎯 Purpose & Intent

One page that says how a dependency gets in, how it is kept current, and how fast a problem in one is fixed. Filled in, it is the dependency documentation of the [OpenSSF Baseline](https://baseline.openssf.org/) (OSPS-DO-06.01), its remediation thresholds for vulnerabilities and licences found by software composition analysis (OSPS-VM-05.04, OSPS-VM-05.05), its policy for those findings before a release (OSPS-VM-05.02), and its threshold for static analysis findings (OSPS-VM-06.01).

- **Deliberate**: every dependency is chosen, not just installed.
- **Pinned**: what CI tested is exactly what ships.
- **On a clock**: every finding has a deadline, and every exception an owner and an end date.

---

## 🧭 1. Choosing A Dependency

A new dependency is a decision, made in the pull request that adds it, which says why the project needs it rather than a few lines of its own.

- **Maintained**: `[a release or a commit within the last 12 months, and issues that get answers]`
- **Trusted**: `[an OpenSSF Scorecard score of 5 or more at scorecard.dev | published with provenance | widely used and reviewed]`
- **Licensed**: under a licence on the allowed list in **6. Licences**
- **Small**: `[the fewest transitive dependencies that do the job]`
- **Decided by**: `[@handle]`, when a new dependency is in doubt

---

## 📥 2. Where Dependencies Come From

- **Registries**: `[npm | PyPI | crates.io | Maven Central | the Go module proxy]`, and nowhere else. No `curl | sh` installs, and no vendored copy of a package the registry serves.
- **Actions**: every `uses:` in `.github/workflows/` names a full commit SHA, or a tag of `tannergolden/standards`; the repository validator fails one that names a branch.
- **Containers**: `[base images pinned by digest | none]`
- **Binaries**: none committed. The repository validator fails compiled code anywhere in the tree, unless `.gitattributes` marks it `reviewed-binary`.

---

## 🔒 3. Pinning And Lockfiles

- **Lockfiles are committed**: `[package-lock.json | poetry.lock | uv.lock | Cargo.lock | go.sum]`
- **CI installs from them**: `[npm ci | pip install --require-hashes | cargo build --locked | go mod verify]`, so a dependency cannot change between the pull request and the release.
- **Hashes where the ecosystem has them**: `.github/scripts/requirements.txt` pins PyYAML by the hash of every file PyPI serves for it, and every Python requirements file here does the same.

---

## 🔄 4. Keeping Them Current

- **Dependabot** opens version updates monthly for the ecosystems in `.github/dependabot.yml`: `[the workflows, the development container and the scripts' requirements, which ship on | the ones this project added]`. It waits until a release is three days old, and groups each ecosystem's updates into one pull request.
- **Security updates** arrive as soon as an advisory names a version in use, once 🎯 Apply Standards has switched them on.
- **🦾 Automate Dependabot** approves and merges a patch or minor update once the required checks pass. A major update waits for a person.
- **Somebody answers them**: after 90 days in which nobody responds to its pull requests, Dependabot stops opening any, security updates included. `[@handle]` reviews them every `[week]`.
- **Each release carries an SBOM**, `sbom-<tag>.cdx.json`, listing every dependency it was built from.

---

## 🛡️ 5. Vulnerabilities

The windows match the ones [`SECURITY.md`](/.github/SECURITY.md) promises reporters, so a vulnerability in a dependency is fixed as fast as one in this code.

| Severity | Blocks a merge             | Fixed within |
| :------- | :------------------------- | :----------- |
| Critical | Yes, by dependency review  | 30 days      |
| High     | Yes, by dependency review  | 30 days      |
| Medium   | `[No \| Yes, at moderate]` | 60 days      |
| Low      | No                         | 90 days      |

- **At the merge**: dependency review, a required check on a public repository, fails a pull request that adds a dependency with a known vulnerability at `high` or above. `dependency-review-severity` on the `ci` job in `.github/workflows/checks.yml` moves the line.
- **After it**: a Dependabot alert on a dependency already in use starts its window the day it opens.
- **Not exploitable here**: a finding that cannot be reached in this project is declared rather than fixed. Dismiss the alert with the reason, record it `[as a VEX statement in docs/operations/vex/ | in the alert alone]`, and give it an owner and a date to look again.

---

## ⚖️ 6. Licences

- **Allowed**: `[MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC, MPL-2.0]`
- **Denied**: `[GPL-3.0-only, AGPL-3.0-only]`, set as `deny-licenses` on the `ci` job in `.github/workflows/checks.yml`, so dependency review fails a pull request that adds one.
- **Threshold**: a denied licence blocks the merge. One found after a merge, or a licence nobody can identify, is resolved within `[30 days]` and always before the next release.

---

## 🔍 7. Static Analysis

- **What runs**: CodeQL analyses every pull request on a public repository, and the default branch weekly.
- **Threshold**: `[a new critical or high finding is fixed, or dismissed with its reason, before the pull request merges; a medium one within 60 days; a low one within 90]`
- **Enforced by**: `[review alone | code scanning merge protection, CodeQL at high or higher]`. Merge protection is a ruleset each repository opts into; the standards' Branch Protection checklist says what it costs.

---

## 🚢 8. Before Every Release

- [ ] No open critical or high alert on a shipped dependency, unless declared not exploitable as **5** describes
- [ ] No open critical or high CodeQL finding, unless dismissed with its reason
- [ ] No dependency under a denied licence, or one nobody could identify
- [ ] The SBOM attached to the release lists what was shipped

---

## 🔁 9. Review

Reviewed every `[six months]`, whenever the project adds an ecosystem, and after any incident a dependency caused.

| Date           | Reviewer    | Change                                        |
| :------------- | :---------- | :-------------------------------------------- |
| `[YYYY-MM-DD]` | `[@handle]` | `[First version \| No change \| Added Cargo]` |

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Every dependency chosen, pinned and answered for.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
