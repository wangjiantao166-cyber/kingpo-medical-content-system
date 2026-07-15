# wordpress-content-model-admin

## Purpose

Own WordPress CPTs, taxonomies, ACF field groups, admin columns, roles, capabilities, post statuses, validation hooks, and editorial workflows.

## Use Conditions

Use for WordPress implementation specs, plugin scaffold, admin workflow, REST/WP-CLI contracts, and field permissions.

## Do Not Use Conditions

Do not put content model ownership into the theme or install on production without approval.

## Accepted Input Schema

- `docs/wordpress-implementation-spec.md`
- entity schemas
- site publication schema

## Output Schema

CPT spec, taxonomy spec, field spec, role matrix, admin workflow spec.

## Blocking Conditions

Block if high-risk fields are freely editable or source of truth is unclear.

## Handoff Rules

Send display needs to `wordpress-theme-template`; send release readiness to `release-quality-gate`.
