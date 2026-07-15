# content-strategy-authoring

## Purpose

Create page briefs and draft content for products, applications, standards, resources, and technical guides using approved evidence.

## Use Conditions

Use after product facts are structured and claim risk is understood.

## Do Not Use Conditions

Do not invent specs, use one fixed template for all products, approve your own output, or create bulk low-value pages.

## Accepted Input Schema

- `schemas/page-brief.schema.json`
- `schemas/product-record.schema.json`
- `schemas/application-record.schema.json`

## Output Schema

Draft content, content brief, unresolved questions, and source IDs used.

## Blocking Conditions

Block if no buyer intent, no parent page, no source evidence, or page would duplicate an existing page.

## Handoff Rules

Send drafts to `editorial-trust-review`, asset needs to `asset-visual-production`, and link needs to `technical-seo-link-graph`.
