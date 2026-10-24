<!--
title: '🛡️ SECURITY POLICY'
description: 'How to report a vulnerability privately, what happens after you do, which versions receive security fixes, and the protections this repository runs.'
type: guide
-->

<div align="center">

# 🛡️ SECURITY POLICY

<a name="top"></a>

**How to report a vulnerability, and what happens after you do.**

_Report privately. Patch quickly. Disclose responsibly._

</div>

---

## 💡 Overview

If you believe you have found a security vulnerability in this repository, in
its configuration, or in anything it releases, please tell us privately and give
us the chance to fix it before it is made public.

> [!IMPORTANT]
> **Never report a vulnerability in a public issue, discussion, or pull
> request.** Anyone can read those, including the people who would exploit it.

---

## 🧱 Reporting a Vulnerability

### 1. Report it privately

Open this repository's **Security** tab and choose **Report a vulnerability**.
GitHub's private vulnerability reporting keeps the report between you and the
maintainers, needs no email, and lets us work on the fix with you in a private
advisory.

**If there is no Report a vulnerability button**, private reporting has not been
switched on yet. Do not describe the problem anywhere public. Either contact a
maintainer through the private contact listed under **Maintainers** in
[GOVERNANCE.md](GOVERNANCE.md), or open an issue titled
`Security contact request` containing nothing else, and a maintainer will open a
private advisory and invite you to it.

On a **private** repository, where issues are already closed to the public, the
🛡️ Vulnerability Report issue form is the intake instead.

### 2. What to include

The report form asks for these; the more of them you give, the faster we can
act:

- What is affected, and what an attacker can achieve.
- The steps to reproduce it, from a clean clone or a released version.
- A proof of concept, with any secrets or personal data removed.
- The versions or commits you tested.
- Any mitigation you know of.

### 3. What to expect

| Step                       | Our aim                                                                                          |
| :------------------------- | :----------------------------------------------------------------------------------------------- |
| **Acknowledgement**        | Within **7 days** of your report                                                                 |
| **Assessment**             | Within **14 days**: whether we can reproduce it, how severe it is, and what happens next         |
| **Fix**                    | Within **30 days** for critical and high severity, **60 days** for medium, **90 days** for low   |
| **Disclosure**             | When the fix is released, or after **90 days**, whichever is first, unless we agree another date |
| **Updates while you wait** | At least every **14 days** until the report is closed                                            |

> [!NOTE]
> **For maintainers:** these are the times the template ships. Set ones you can
> keep, because a promise you break costs more trust than a slower one you keep.

### 4. Credit for reporters

We **credit every reporter** who responsibly discloses a valid vulnerability.
Unless you ask to remain anonymous, your name or handle is acknowledged in the
security advisory and in the release notes for the fix. Tell us how you would
like to be credited when you report.

---

## 📢 How Fixes Are Published

- The fix is developed in a private **GitHub security advisory**, with you
  invited to it if you wish.
- When it ships, the advisory is published, and a **CVE** is requested through
  GitHub where the vulnerability warrants one, so dependency tools such as
  Dependabot can tell everyone affected.
- The release notes list it under **🔒 Security**, and they are kept: release
  pages are this repository's changelog and are never deleted on their own.

---

## ✅ Supported Versions

| Version              | Security fixes                                  |
| :------------------- | :---------------------------------------------- |
| **Latest release**   | ✅ Yes                                          |
| **Earlier releases** | ❌ No: upgrade to the latest release to get one |

A release stops receiving security fixes the day the next one is published. If
this project supports more than the latest release, list each supported line
here, with the date its support ends.

---

## 🧭 Scope

**In scope:** the code and configuration in this repository, its workflows, and
the artifacts its releases publish.

**Out of scope:**

- Vulnerabilities in a dependency, unless this project uses it in a way that
  makes it exploitable. Report those to the dependency's maintainers.
- Findings from automated scanners with no demonstrated impact.
- Social engineering, physical attacks, and denial of service against GitHub
  or any other host.

---

## 🤝 Safe Harbour

We will not pursue or support legal action against anyone who researches and
reports a vulnerability in good faith and in line with this policy: who avoids
privacy violations, data destruction and service disruption, uses only accounts
they own or have permission to use, and gives us reasonable time to fix the
problem before disclosing it.

---

## 🔒 What This Repository Runs

Each of these is configured by the files in this repository or by
🎯 Apply Standards:

- **Secret scanning**: Gitleaks scans every pull request, every push to the
  default branch and, weekly, the whole history, and is a required check under
  the shipped rulesets. GitHub's own secret scanning and push protection are
  switched on with the settings.
- **Static analysis**: CodeQL analyses the code and the GitHub Actions
  workflows, weekly and on every pull request (public repositories).
- **Dependency review**: every pull request is screened for dependencies with
  known vulnerabilities (public repositories).
- **Dependency updates**: Dependabot keeps the workflow actions, the development
  container and the repository scripts' requirements current, waits three days
  before proposing a new version, and opens security updates at once.
- **Supply-chain score**: OpenSSF Scorecard rates the repository weekly and
  files its findings under code scanning (public repositories).
- **Hardened runners**: every job starts by auditing its network egress.
- **Release integrity**: every release carries a CycloneDX SBOM, and on a
  public repository its build archive also carries a build provenance
  attestation. How to check them is in the project's Release Verification
  document, seeded from `docs/templates/distribution/Release-Verification.md`.

---

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Proactive security. Responsible disclosure.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in [LICENSE](/LICENSE).

</div>
