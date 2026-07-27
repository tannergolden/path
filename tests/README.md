# 🧪 Tests - your suites start here

This scaffold ships empty on purpose - wire your framework of choice into the `test-command` that `.github/workflows/checks.yml` runs:

| Folder         | Put (and look for)                                                           |
| :------------- | :--------------------------------------------------------------------------- |
| `unit/`        | Fast, isolated tests of pure logic (co-locating next to source is fine too). |
| `integration/` | Tests that cross a real boundary: database, filesystem, HTTP.                |
| `e2e/`         | Full user-journey tests against a running system.                            |

The binding standard is the canonical [Testing Strategy](https://github.com/tannergolden/standards/blob/Development/docs/distribution/Testing-Strategy.md); the fill-in guidelines under `docs/templates/technical/testing/` are seeded for your own conventions.

This directory is **PROTECTED** from the template sync engine: it is yours, and no upstream sync will ever write or delete here.
