<!--
title: '🚢 RELEASE PROCESS'
description: 'How this project cuts, checks and publishes a release with the 📦 Release workflow, adding its own choices to the shared Releases & Versioning standard. Fill it in before the first release, and follow it for every release after.'
type: template
-->

<div align="center">

# 🚢 RELEASE PROCESS

<a name="top"></a>

**How a release is cut, checked and published here, from draft to announcement.**

_The notes are the changelog. Keep them._

</div>

---

> [!NOTE]
> **How to use**: copy this file to `docs/distribution/Release-Process.md`, the same path minus `templates/`, and replace every `[bracket]`. The seed here stays pristine. It adds this project's choices to the shared [Releases & Versioning](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md) standard, which already sets the version policy, the tag format and the release workflows, and does not repeat them.

---

## 🔢 1. Versioning Scheme

- **Scheme**: `[SemVer | CalVer | REPLACE_ME]`. Under SemVer the release workflow works out the next version from the Conventional Commits since the last release, so nobody bumps it by hand. Any other scheme means setting the tag by hand when publishing.
- **Public interface**: `[What a breaking change is measured against: the API, the CLI flags, the file formats, the configuration keys]`
- **Before 1.0.0**: `[A breaking change bumps the minor | Anything may break]`
- **Version also written in**: `[Nowhere but the tag | A version file | The package manifest, kept in step by: REPLACE_ME]`
- **Supported versions**: `[The latest release only | The last N minor releases]`, listed in `.github/SECURITY.md`

---

## 🌿 2. Branches

Releases follow the promotion line in [Branching Strategy & Workflow](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Branching-Strategy-&-Workflow.md): `[Development]` → `[Preview]` → `[Release]`.

| Branch          | Role here                                                  | Reached by                                    |
| :-------------- | :--------------------------------------------------------- | :-------------------------------------------- |
| `[Development]` | Every change lands here first                              | Pull requests from topic branches             |
| `[Preview]`     | `[Smoke tests \| QA \| A preview deploy]` before a release | A promotion pull request from `[Development]` |
| `[Release]`     | Every release is published from here                       | A promotion pull request from `[Preview]`     |

- **Who may promote**: `[Any maintainer | The release manager: @handle]`

---

## 📝 3. The Weekly Draft

The `notes` task of 📦 Release, in `.github/workflows/release.yml`, keeps one draft release current, so the notes are already written when a release is due:

- It runs every Monday at 5:00 am UTC, and whenever someone dispatches 📦 Release with the `notes` task.
- A scheduled run skips a week with fewer than `[3]` commits (`minimum-commits` in the stub). A dispatched run never skips.
- It groups the changes since the branch's last release by Conventional Commit type, names the draft `v<next version>-<branch>.next`, and replaces the previous draft rather than adding another.
- `[@handle]` reads the draft each week and `[rewords unclear entries | leaves it as generated]`.

---

## 🚀 4. Publishing

1. **Promote** `[Development]` to `[Preview]` to `[Release]` by pull request, with the checklist in section 9 complete.
2. **Open the draft** on the repository's Releases page. Set its tag to the final version, dropping the `.next` suffix, as `[vX.Y.Z | vX.Y.Z-release]`, and set its target to `[Release]`.
3. **Edit the notes**: `[add a short summary at the top; put breaking changes and migration steps first; credit the reporter of each fixed vulnerability]`. Delete the "Draft, not published" section the workflow adds.
4. **Publish it.** That starts the `publish` task of 📦 Release. It keeps your notes, builds with `[the build-command input of the publish job | a make build target]`, and attaches:
   - `build-<tag>.tar.gz`: the contents of `[dist | build | target/release]`, the `artifact-path` input, which is `dist` unless the stub sets another
   - `sbom-<tag>.cdx.json`: a CycloneDX SBOM of the dependencies the release was built from
   - `README.md`: the README, with anything between `<!-- internal:start -->` and `<!-- internal:end -->` removed

   On a public repository it also signs a build provenance attestation for the archive. With no build output there is no archive and nothing to attest: the release carries its notes, the SBOM and the README.

5. **Verify it** the way a user would, with [Release Verification](Release-Verification.md).
6. **Announce it** in `[the Announcements discussion category | the chat channel | the project site]`.

The `publish` task can also be dispatched by hand, and then works out the version and notes itself, as the shared standard describes. This project `[uses that only for: REPLACE_ME | does not use it]`.

---

## 📦 5. Package Registries

A GitHub release is not a package: nobody installs a library from a release page. If users install this project from a registry, the `package` task of 📦 Release publishes it there.

- **Registries**: `[None: the release assets are the deliverable | npm | PyPI | crates.io | A container registry, GHCR by default]`, switched on in the `package` job of `.github/workflows/release.yml`
- **Credentials**: `[NPM_TOKEN | PYPI_API_TOKEN, or Trusted Publishing on PyPI | CARGO_REGISTRY_TOKEN | Nothing extra for GHCR]`, stored as repository secrets. A registry switched on without its credential fails the run rather than skipping it.
- **Rehearse first**: dispatch 📦 Release with the `package` task and `dry-run` on. It builds and checks everything, and publishes nothing.
- **Then automate**: once a dry run passes, add `github.event_name == 'release'` to the `package` job's condition, so every published release also publishes the package.

---

## 🔥 6. Hotfixes & Back-Merges

The shared [hotfix protocol](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Releases-&-Versioning.md#-hotfix-protocol) applies: branch `hotfix/<ticket>` from `[Release]`, make the smallest fix with a test, merge it by pull request, publish a patch release, then back-merge.

- **Approved by**: `[Any maintainer | The release manager | Two maintainers]`
- **Draft the patch at once**: dispatch 📦 Release on `[Release]` with the `notes` task, rather than waiting for Monday.
- **Back-merge** `[Release]` into `[Development]` and `[Preview]` within `[the same day | 24 hours]`, by `[the hotfix author | the release manager]`, so the next promotion cannot undo the fix.

---

## ⏪ 7. Rollback

A published release is never edited to undo it, and its tag is never moved or reused.

- **Go back**: redeploy the previous release, `[how this project redeploys an earlier tag]`, as [Deployment Protocols](../technical/infrastructure/Deployment-Protocols.md) sets out.
- **Fix forward**: ship the fix as a new patch release, through the hotfix path above.
- **Mark the bad release**: `[add a warning to the top of its notes that points to the fix | mark it as a pre-release]`
- **In a registry**: `[npm deprecate | Yank it on PyPI | cargo yank | Point the container tag back at the last good image]`

---

## 🗂️ 8. The Notes Are The Changelog

This project keeps no separate changelog file. Each release page carries the notes for its version, the credit for any vulnerability it fixed, and its assets, provenance and SBOM, so release pages are kept.

- The `prune` task of 📦 Release deletes old release pages, and runs only when someone dispatches it. Run it first with `dry-run` on: it lists what it would delete and deletes nothing. Then run it again with `dry-run` off.
- It keeps the newest `[1]` release (`keep` in the stub), leaves drafts and pre-releases alone, and never deletes a tag, so anything pinned to a version keeps working.
- **Pruned when**: `[Never | When the Releases page passes N releases]`, decided by `[@handle]`

---

## ✅ 9. Pre-Release Checklist

- [ ] `[Preview]` validated: `[smoke tests green; metrics normal for N hours]`
- [ ] The required checks are green on `[Release]`
- [ ] The version matches the changes: a breaking change means a major release
- [ ] Breaking changes and migration steps lead the notes
- [ ] Each fixed vulnerability has its advisory ready and its reporter credited
- [ ] The previous release can be redeployed, so a rollback is ready
- [ ] `[The package dry run passed, if this release goes to a registry]`
- [ ] `[Someone watches the release for N hours after publishing]`

### 🔗 See also

> [!TIP]
> Every canonical guide is indexed in the [&#x1F4DA; Standards Index](https://github.com/tannergolden/standards/blob/Development/docs/README.md). If you rename or move a file, update every reference to it across the repository to prevent link drift.

---

<div align="center">

**Cut from one branch, published by one workflow, recorded on one page.**

[↑ Back to Top](#top)

<br />

Built with ❤️ by the Engineering Team. Distributed under the terms in this repository's LICENSE.

</div>
