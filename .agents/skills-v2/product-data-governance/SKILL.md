# product-data-governance

## Purpose

Own product facts, lifecycle status, source records, specification records, and source conflict decisions.

## Use Conditions

Use when collecting product data, importing sources, structuring specifications, resolving old-site conflicts, or deciding whether a product is active, custom, R&D, legacy, discontinued, or internal.

## Do Not Use Conditions

Do not approve compliance claims, publish drafts, or use competitor data as KingPo facts.

## Accepted Input Schema

- `schemas/source-record.schema.json`
- `schemas/product-record.schema.json`
- `schemas/specification-record.schema.json`

## Output Schema

Structured product record, source conflict report, and next-state recommendation.

## Blocking Conditions

Block public use when source is missing, source conflict exists, product identity is unclear, or lifecycle is R&D/internal.

## Handoff Rules

Send standards-sensitive facts to `standards-claims-compliance`. Send complete product records to `content-strategy-authoring`.
