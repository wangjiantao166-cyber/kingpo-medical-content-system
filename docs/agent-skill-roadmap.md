# Agent and Skill Roadmap

## Purpose

This document defines the v2 agent system needed to maintain KingPo product master data, WordPress content, SEO architecture, visual assets, and publishing quality over time.

## v2 Core Agent Domains

The old skills remain in the repository during migration. New work should route through these 13 domains and the machine-readable `skills-manifest.yaml`.

| v2 Agent | Merged or Extended From | Main Responsibility |
| --- | --- | --- |
| `workflow-orchestrator` | `multi-agent-workflow-coordinator` | Risk routing, state machine, handoff, approval gates |
| `product-data-governance` | `product-knowledge-base`, `product-lifecycle-manager` | Product facts, lifecycle, source conflicts, master data |
| `standards-claims-compliance` | `standard-relation-auditor`, `medical-standards-mapping` | Standard versions, clauses, claim wording, compliance risk |
| `content-strategy-authoring` | `ai-product-page-generator`, `application-page-system` | Product, application, standard, and resource briefs/drafts |
| `editorial-trust-review` | `google-seo-eeat-content` | People-first content, Who/How/Why, AI disclosure, trust review |
| `information-architecture-navigation` | `seo-site-architecture-planner`, `content-cluster-planner`, `navigation-mega-menu-architect`, `homepage-authority-hub` | URL, taxonomy, navigation, breadcrumbs, content clusters |
| `technical-seo-link-graph` | `internal-linking-architect`, `orphan-link-auditor`, `content-refresh-auditor` | Link graph, canonical, sitemap, facets, structured data, crawl health |
| `wordpress-content-model-admin` | `wordpress-cpt-acf-builder`, `wordpress-admin-operator`, `wordpress-backend-workflow` | CPT, taxonomy, fields, permissions, admin lists, validation |
| `wordpress-theme-template` | `theme-framework-planner`, `page-template-designer`, `site-ux-template-system` | Block theme, templates, Gutenberg patterns, responsive front end |
| `asset-visual-production` | `asset-library-manager`, `visual-asset-generator`, `brand-art-director` | Image rights, diagrams, AI visuals, asset QA |
| `conversion-analytics` | `inquiry-conversion` | CTAs, forms, events, inquiry quality, privacy-aware tracking |
| `data-migration-sync` | `data-import-export`, `product-data-collector` | Import, dedupe, external IDs, dry runs, rollback |
| `release-quality-gate` | `product-publish-qa`, `qa-launch-check`, `security-backup` | Final independent QA and publish blocker decisions |

## Deprecated Independent Agent Roles

The following should no longer be called as standalone planning agents for new work:

- `homepage-authority-hub`
- `navigation-mega-menu-architect`
- `content-cluster-planner`
- `orphan-link-auditor`
- `content-refresh-auditor`
- `wordpress-draft-publisher`

Their functions are now task modes inside the v2 domains. `wordpress-draft-publisher` should become a controlled runbook or tool contract: validate, dry-run, create/update draft, return post ID, and write audit log.

## Default Routing

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

## Default Safety Rule

Agents should create drafts, specs, fixtures, and review outputs by default. Publishing, production changes, DNS changes, plugin installation, redirects, and bulk imports require explicit approval.

Content generation agents cannot approve their own output. Any blocker in `docs/agent-contracts-and-state-machine.md` prevents `ready_for_publish`.
