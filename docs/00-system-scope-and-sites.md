# System Scope and Sites

## Purpose

This repository is the KingPo content operating system for product master data, source evidence, WordPress publishing, SEO architecture, visual asset governance, and release quality control.

It is not a single medical-only website plan. Medical testing equipment is an important vertical, but the system must also support other KingPo product domains when source evidence and business priority justify them.

## Supported Site Sources and Publishing Targets

The system supports, but is not limited to, these KingPo-related sites:

| Site | Role | Use Policy |
| --- | --- | --- |
| `dgkingpo.com` | Main KingPo / DGKingPo broad equipment source | Use as owned source, with page-level source records and field-level verification for technical claims. |
| `batterytestingmachine.com` | English product site for battery, environmental, safety, and related equipment | Use as owned source, but do not assume all fields are current without review. |
| `kingpocn.com` | Domestic Chinese site | Use for Chinese-market source material, product understanding, images, and capability references. Rewrite for overseas B2B buyers; do not machine translate directly. |
| `kingpo.hk` | KingPo-related site to be included in source registry | Treat as owned/related source after page-level review. If unavailable, do not infer facts from it. |

Competitor or public reference sites may be used for market learning, page structure, buyer questions, and terminology research. They must not be converted into KingPo product facts, parameters, images, certifications, customer cases, or compliance claims.

## Publishing Model

WordPress is the first-phase publishing layer. The repository should produce staging-ready content models, templates, data contracts, validation checks, and draft workflows before any production release.

Each content record must carry:

- `site_target`: target site or group of sites;
- `language`: source language and intended publishing language;
- `source_ids`: evidence records supporting the content;
- `review_status`: current human review state;
- `public_visibility`: whether the content is approved for public use.

## Product Scope

Supported product domains include:

- Medical Device Test Equipment
- Battery Safety Test Equipment
- Environmental & IP Test Equipment
- Electrical Safety Test Equipment
- Flammability & Material Test Equipment
- Plug, Socket, Cable & Gauge Test Equipment
- Automotive & EV Test Equipment
- Automation & Custom Test Systems

IEC, ISO, EN, UL, UN ECE, SASO, BIS, ASTM, ANSI/AAMI, GB, YY/T, and similar organizations are standard families, not product categories by themselves.

## Approval Rule

All production publishing, DNS changes, plugin installation on production, redirects, bulk imports, and public claims about certification, compliance, calibration, standards coverage, medical use, price, delivery, customers, or stock status require human approval.
