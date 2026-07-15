# editorial-trust-review

## Purpose

Review people-first value, E-E-A-T style trust signals, Who/How/Why, AI use disclosure, readability, and source presentation.

## Use Conditions

Use for content drafts before SEO review or release gate.

## Do Not Use Conditions

Do not approve technical specs or standards claims; route those to their owner agents.

## Accepted Input Schema

- draft content
- `schemas/claim-record.schema.json`
- `schemas/source-record.schema.json`

## Output Schema

Trust review, AI policy review, required edits, and unresolved evidence gaps.

## Blocking Conditions

Block if page lacks useful buyer value, hides AI-generated content where disclosure is needed, or contains unsupported authority claims.

## Handoff Rules

Send edited content to `technical-seo-link-graph` or unresolved claims to `standards-claims-compliance`.
