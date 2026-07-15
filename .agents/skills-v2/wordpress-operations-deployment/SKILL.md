# wordpress-operations-deployment

## Purpose

Own WordPress environment audit, WP-CLI operations, staging deployment, production deployment planning, backups, rollback, cache/rewrite/cron checks, mail/form smoke tests, Site Health checks, deployment logs, and incident recovery.

## Use Conditions

Use for WordPress operations, deployment plans, staging/production topology, backup verification, WP-CLI command contracts, plugin/theme release installation, and rollback plans.

## Do Not Use Conditions

Do not approve product parameters, standards claims, content drafts, or public release decisions. Do not directly edit production databases, store plaintext passwords, deploy without backup, bypass release-quality-gate, or auto-update all plugins.

## Accepted Input Schema

- `schemas/wordpress-site-record.schema.json`
- `schemas/deployment-plan.schema.json`
- `schemas/backup-restore-record.schema.json`

## Output Schema

Environment audit, deployment report, backup record, rollback report, and blocker list.

## Blocking Conditions

Block when credentials are plaintext, SSH is root, backup is missing or unverified, dry-run is unavailable for write operations, staging test failed, or production approval is missing.

## Handoff Rules

Send operational readiness to `release-quality-gate`. Return content, claim, SEO, or asset blockers to their owner agents.
