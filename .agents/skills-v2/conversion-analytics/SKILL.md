# conversion-analytics

## Purpose

Own inquiry CTAs, form routing, analytics event definitions, conversion measurement, and privacy-aware tracking.

## Use Conditions

Use for RFQ forms, downloads, WhatsApp/email routes, GA4/GSC event plans, and inquiry quality scoring.

## Do Not Use Conditions

Do not expose personal data in public content or add tracking without privacy review.

## Accepted Input Schema

- page brief
- form spec
- analytics plan

## Output Schema

CTA plan, form field plan, event dictionary, privacy blockers.

## Blocking Conditions

Block if personal data retention, access, or deletion rules are missing.

## Handoff Rules

Send privacy or publication blockers to `release-quality-gate`.
