# Agent Contracts and State Machine

## Purpose

Agents must coordinate through machine-readable contracts, not only natural-language handoff notes.

## Risk Levels

```text
LOW
MEDIUM
HIGH
REGULATORY_HIGH
PRODUCTION_CHANGE
```

## Content States

```text
source_incomplete
structured
technical_review
standards_review
content_draft
editorial_review
visual_review
seo_review
ready_for_publish
published
refresh_due
retired
blocked
```

AI may create or improve drafts, but AI must not move a record to `ready_for_publish` or `published`.

## Blocker Codes

```text
missing_source
source_conflict
unverified_standard
unsupported_claim
missing_reviewer
missing_public_asset_permission
duplicate_slug
canonical_unresolved
thin_or_duplicate_page
production_approval_required
privacy_risk
competitor_source_misuse
```

## Required Handoff Fields

Each agent handoff must include:

```text
task_id
entity_ids
from_agent
to_agent
risk_level
current_state
requested_next_state
decisions
source_ids
claim_ids
blockers
open_questions
allowed_mutations
human_approval_required
timestamp
```

## Routing Examples

Low-risk text or alt correction:

```text
product-data-governance
→ editorial-trust-review
→ release-quality-gate
```

Ordinary new product:

```text
product-data-governance
→ content-strategy-authoring
→ asset-visual-production
→ wordpress draft operation
→ release-quality-gate
```

Standards-sensitive or medical product:

```text
product-data-governance
→ standards-claims-compliance
→ content-strategy-authoring
→ editorial-trust-review
→ technical-seo-link-graph
→ release-quality-gate
```

Site architecture:

```text
workflow-orchestrator
→ information-architecture-navigation
→ wordpress-content-model-admin
→ wordpress-theme-template
→ technical-seo-link-graph
→ release-quality-gate
```
