# 💻 Source - your application starts here

This scaffold ships empty on purpose - the template imposes a layout, not a stack:

| Folder    | Put (and look for)                                                         |
| :-------- | :------------------------------------------------------------------------- |
| `app/`    | The application layer: entry points, use-cases, orchestration.             |
| `domain/` | The domain layer: entities, business rules, pure logic (no I/O).           |
| `infra/`  | The infrastructure layer: persistence, transport, adapters to the outside. |

Standards to follow while filling it in: the fill-in [Source Code](../docs/templates/technical/Source-Code.md) and [Technology Stack & Tooling](../docs/templates/technical/Technology-Stack-&-Tooling.md) documents seeded under `docs/templates/technical/` - instantiate them with your decisions.

This directory is **yours from the first commit**. Nothing here syncs, and nothing upstream will ever write to it or delete from it - there is no sync engine to protect it from.
