# WordPress Operations and Deployment

## Purpose

This document defines how Codex may operate WordPress through GitHub, WP-CLI, staging, backups, and release gates.

## Rules

- Staging and production must be separate.
- Codex uses a dedicated deploy user, not root.
- Secrets are stored in GitHub Environments or Secrets.
- Production deployment requires database and uploads backup.
- WP-CLI write operations must support `--dry-run` when practical.
- Import operations need external IDs and idempotency.
- Direct production SQL writes are prohibited.
- Production publish and deployment require human approval.

## Standard Flow

```text
GitHub branch
-> Codex PR
-> automated tests
-> deploy staging
-> WP-CLI draft/update
-> engineering/standards/SEO review
-> release-quality-gate
-> human approval
-> production deploy/publish
```

## Required Reports

- environment audit
- deployment report
- backup record
- rollback report
- WP-CLI operation report
- smoke test report
