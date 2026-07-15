# Deployment, Backup, and Rollback Runbook

## Purpose

This runbook covers production-sensitive operations without creating another standalone agent. It is mandatory for production plugin/theme activation, WordPress bulk sync, redirects, and configuration changes.

## Required Before Production Change

- Staging validation completed.
- Current production backup verified.
- Rollback owner assigned.
- Changed files and database changes listed.
- Expected downtime or cache impact documented.
- Human publisher approval recorded.
- Security-sensitive credentials excluded from repository.

## Blockers

Block production changes when:

- backup is missing or untested;
- rollback steps are unclear;
- staging has not been tested;
- permission changes are unreviewed;
- bulk sync lacks dry-run report;
- redirects or canonical changes lack SEO approval.

## Rollback Record

Every production operation must record:

```text
operation_id
operator
approved_by
started_at
completed_at
changed_components
backup_reference
rollback_steps
validation_result
```
