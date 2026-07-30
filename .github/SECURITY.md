<!--
title: '🛡️ SECURITY POLICY'
description: 'Supported versions and how to report vulnerabilities privately.'
tags: [security, policy, disclosure, vulnerabilities]
category: security
-->

<!-- markdownlint-disable MD041 -->
<div align="center">

# 🛡️ SECURITY POLICY

<a name="top"></a>

**Defining the zero-trust blueprint for a transparent and responsible engineering environment.**

_Report privately. Patch quickly. Disclose responsibly._

</div>

---

## 💡 Overview

This repository ships the Golden Path template's baseline security configurations, intended to help developers identify vulnerabilities early. Security is treated as a shared responsibility; the template provides the tooling, and each project must maintain and monitor its own instance.

> [!IMPORTANT]
> If you believe you have found a security vulnerability in this repository or its shipped configuration, please follow the process below. **Do not open a public issue.**

---

## ✅ Supported Versions

We provide configuration updates and patch guidance for the following versions:

| Version     | Status                |
| :---------- | :-------------------- |
| **0.1.x**   | ✅ Active Maintenance |
| **< 0.1.0** | ❌ End of Support     |

---

## 🧱 Reporting a Vulnerability

To protect the community, we ask that you report vulnerabilities through private channels.

### 1. Submit the Report

Use GitHub's private vulnerability reporting: open the repository's **Security** tab and click **Report a vulnerability**. This keeps the report private between you and the maintainers - no email required. (On **private** repositories, where issues are already non-public, the structured 🛡️ Vulnerability Report issue form is the intake channel instead - the issue chooser offers whichever applies.)

### 2. Required Information

Please provide a factual summary to assist in triage:

- A description of the vulnerability.
- Steps to reproduce the issue in a clean clone of the template.
- Potential impact on projects utilizing this architecture.

### 3. Response Timeline

- **Acknowledgment**: Expected within **24 hours**.
- **Status Update**: A preliminary assessment or plan will be shared within **7 days**.

### 4. Credit for Reporters

We **credit every reporter** who responsibly discloses a valid vulnerability. Unless you ask to remain anonymous, your name (or handle) is acknowledged in the security advisory and the release notes for the fix. We believe recognition is the least we owe the people who keep the community safe - tell us how you would like to be credited when you report.

---

## 🧭 Security Configurations

The Golden Path template includes pre-configured settings for the following GitHub security features:

- **Secret Scanning**: Automated secret detection (Gitleaks) runs on pushes and pull requests to catch committed credentials - a **required merge check** under the shipped rulesets.
- **Dependabot**: Monthly grouped checks of the `github-actions` ecosystem, with automated pull requests for known security updates. Enable the ecosystem matching your language in `.github/dependabot.yml` as you add manifests.
- **CodeQL Analysis**: An integrated GitHub Actions workflow for static analysis of common coding patterns (an advisory scan; add its check to the ruleset's required contexts to make it merge-blocking).
- **Dependency Review**: An advisory CI scan that flags vulnerabilities in newly introduced packages during the PR process (public repositories; not in the shipped ruleset's required checks - add it there to make it a hard gate).

---

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Proactive security. Responsible disclosure.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the MIT License.

</div>
