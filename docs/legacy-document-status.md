# Legacy Document Status

## Purpose

This repository contains older planning documents for a Chinese medical testing equipment website under `profiles/medical-cn/`. They are useful background, but they are no longer the top-level system scope.

The current controlling documents are:

- `docs/00-system-scope-and-sites.md`
- `docs/source-tier-and-conflict-policy.md`
- `docs/entity-relationship-model.md`
- `docs/claim-evidence-ledger.md`
- `docs/agent-contracts-and-state-machine.md`
- `docs/wordpress-implementation-spec.md`
- `docs/url-indexation-canonical-facets.md`
- `docs/frontend-design-system-and-templates.md`
- `skills-manifest.yaml`
- `schemas/*.schema.json`
- `docs/DOCUMENT-INDEX.yaml`
- `docs/authoritative-source-of-truth.md`

## How to Use Older Documents

Older Chinese medical-site documents may be used as scoped profile material only when explicitly requested:

- vertical market notes;
- future medical fixture ideas;
- Chinese-language drafting references;
- source and SEO caution reminders.

They must not be used to:

- redefine the repository as medical-only;
- override the v2 agent architecture;
- bypass claim evidence requirements;
- publish content without source and review records;
- exclude battery, environmental, electrical safety, flammability, plug/socket/gauge, automotive/EV, or custom automation product domains.

## Migration Rule

When an old document conflicts with a v2 document, the v2 document wins. Do not delete old documents until their useful content has been migrated or explicitly retired.

Every profile file must include frontmatter with:

```yaml
status: profile
scope: medical-cn
do_not_route: true
superseded_by: docs/00-system-scope-and-sites.md
```
