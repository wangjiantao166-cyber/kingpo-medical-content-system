# technical-seo-link-graph

## Purpose

Own canonical, noindex, sitemap, facets, schema, crawl health, internal link graph, orphan checks, and keyword cannibalization decisions.

## Use Conditions

Use for URL rules, structured data, sitemap policy, link graph design, facet controls, and technical SEO audits.

## Do Not Use Conditions

Do not invent product data or approve claims.

## Accepted Input Schema

- `schemas/canonical-decision.schema.json`
- `schemas/site-publication-record.schema.json`
- page intent data

## Output Schema

Canonical decision, indexation rule, schema plan, internal link map, and blockers.

## Blocking Conditions

Block if page has unresolved canonical, duplicate intent, thin content, unsafe schema, or uncontrolled crawl space.

## Handoff Rules

Send publish blockers to `release-quality-gate`; send structure conflicts to `information-architecture-navigation`.
