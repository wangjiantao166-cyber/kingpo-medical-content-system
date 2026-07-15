# data-migration-sync

## Purpose

Own imports, exports, deduplication, external IDs, dry runs, rollback plans, and old-site read-only inventory.

## Use Conditions

Use for spreadsheets, old site inventories, product identity maps, and WordPress sync planning.

## Do Not Use Conditions

Do not bulk import to production, overwrite reviewed records, or treat old sites as automatically verified.

## Accepted Input Schema

- source records
- product records
- migration maps

## Output Schema

Dry-run report, dedupe report, rollback plan, and unresolved conflicts.

## Blocking Conditions

Block if external IDs are missing, duplicate slugs are unresolved, or rollback is impossible.

## Handoff Rules

Send conflicts to `product-data-governance`; send final readiness to `release-quality-gate`.
