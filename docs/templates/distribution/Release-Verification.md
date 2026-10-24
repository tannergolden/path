<!--
title: '🔏 RELEASE VERIFICATION'
description: 'How someone who downloads a release checks that it is intact and was built from this repository by the shared release workflow, using the build provenance attestation, a checksum and the SBOM. Read it before running a downloaded release, and link it from every release.'
type: template
-->

<div align="center">

# 🔏 RELEASE VERIFICATION

<a name="top"></a>

**How to check that a download is intact, and was built here from this source.**

_Trust the signature, not the link._

</div>

---

> [!NOTE]
> **How to use**: copy this file to `docs/distribution/Release-Verification.md`, the same path minus `templates/`, and replace every `[bracket]`. The seed here stays pristine. Filled in, it is the instructions the [OpenSSF Baseline](https://baseline.openssf.org/) asks for, to verify a release's integrity and authenticity (OSPS-DO-03.01) and the identity of the process that built it (OSPS-DO-03.02), and the documented way to check a signed release that the [OpenSSF Best Practices badge](https://www.bestpractices.dev/) asks for (`signed_releases`).

---

## 📦 1. What A Release Carries

Every release that 📦 Release publishes carries these files:

| Asset                 | What it is                                                                                                        | Attested                                            |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| `build-<tag>.tar.gz`  | `[The build output: what is inside, and how to run or install it]`                                                | Yes, on a public repository                         |
| `sbom-<tag>.cdx.json` | A CycloneDX SBOM: each dependency the release was built from, read from the manifests and lockfiles in the source | No                                                  |
| `README.md`           | The project README as of the release                                                                              | No                                                  |
| `[Registry package]`  | `[The same release on npm \| PyPI \| crates.io \| a container registry]`                                          | `[The registry's own provenance, where it has one]` |

The attestation is a signed statement that names the archive's SHA-256 digest, the repository and commit it was built from, and the workflow that built it. There is no long-lived signing key to fetch: GitHub signs each attestation with a short-lived certificate issued to the workflow run, and `gh` checks it against Sigstore's public trust root. The "Source code" archives GitHub adds to every release page are generated on request and are not attested: to check the source, check out the tag instead.

---

## 🔐 2. Verify The Build Provenance

This one check shows both that the file is intact and where it came from. It needs the GitHub CLI, `gh`, signed in with `gh auth login`.

```bash
gh release download <tag> --repo [OWNER/REPOSITORY] --pattern 'build-*.tar.gz'
gh attestation verify build-<tag>.tar.gz \
  --repo [OWNER/REPOSITORY] \
  --signer-workflow tannergolden/standards/.github/workflows/release-publish.yml
```

- **`--repo [OWNER/REPOSITORY]`** checks that the archive was built from this repository.
- **`--signer-workflow`** pins the identity that signed it. The attestation is made inside the shared reusable workflow `tannergolden/standards/.github/workflows/release-publish.yml`, which this repository's 📦 Release calls, so that workflow is the signer. `gh` needs this flag, or `--signer-repo`, whenever a reusable workflow signs, and with it a valid attestation from any other workflow fails.
- **A pass**: `gh` says verification succeeded, shows the repository and workflow the attestation names, and exits with status 0. Anything else is a failure.
- **Stricter**: add `--deny-self-hosted-runners` to also refuse a build made on a self-hosted machine. The shared workflow builds on GitHub-hosted runners, so a genuine release still passes.
- **Offline**: fetch the attestation first with `gh attestation download`, then pass the file it writes to `--bundle`.

> [!NOTE]
> **A private repository's releases carry no attestation.** A private repository needs GitHub Enterprise Cloud for attestations, and the shared release workflow skips the step on every private repository, so `gh attestation verify` finds nothing to check. Use the checksum below, and the repository's own access controls, instead.

---

## 🧮 3. Check The Checksum

A checksum shows the file was not damaged or changed after it was published. On its own it does not show who built it: the attestation above checks the same SHA-256 digest and the origin, so where both are available, the attestation is the stronger check.

```bash
# Linux
sha256sum build-<tag>.tar.gz
# macOS
shasum -a 256 build-<tag>.tar.gz
# Windows (PowerShell)
Get-FileHash build-<tag>.tar.gz -Algorithm SHA256
```

- **Compare it with**: `[The SHA256SUMS file attached to each release | The digests listed in each release's notes | Nothing: this project relies on the attestation, which carries the digest]`
- **Who publishes it**: the shared release workflow attaches no checksum file of its own, so this project `[adds one in: REPLACE_ME | publishes none]`.

---

## 🧾 4. Inspect The SBOM

```bash
gh release download <tag> --repo [OWNER/REPOSITORY] --pattern 'sbom-*.cdx.json'
jq -r '.components[] | "\(.name) \(.version)"' sbom-<tag>.cdx.json
```

The SBOM is CycloneDX JSON. Each entry under `components` is one dependency, with its name, its version and its package URL (`purl`). Read it with any JSON tool, as above, or load it into `[a scanner or inventory that reads CycloneDX: REPLACE_ME]` to see whether a release contains a dependency with a known vulnerability. A release built from a tree with no manifests or lockfiles has no SBOM.

The SBOM is not attested: it lists what the release was built from, and proves nothing about who built it.

---

## 🚩 5. If Verification Fails

1. **Do not run or install the file.** Delete it.
2. **Rule out the simple causes**: an interrupted download (download it again), a mistyped `--repo`, a release published before `[the first attested release: vX.Y.Z]`, or a private repository, which has no attestations.
3. **If it still fails, report it privately.** Follow `.github/SECURITY.md`: on a public repository, choose **Report a vulnerability** on the **Security** tab; on a private one, use the Vulnerability Report issue form. Give the release tag, the file name, the exact command and its full output. Do not open a public issue: treat a release that fails verification as tampered with until it is shown not to be.
4. **Maintainers** handle the report as a security incident, under [Incident Response](../operations/Incident-Response.md).

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Checked before it runs, reported before it spreads.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in this repository's LICENSE.

</div>
