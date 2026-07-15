# Agent and Skill Roadmap

## Purpose

This document defines the agent system needed to maintain a WordPress-based B2B medical test equipment website over time.

## Core Agents

### Product Knowledge Base Agent

Converts product sources into structured records.

### Product Lifecycle Manager

Controls whether a product is existing, custom, R&D, internal, legacy, or discontinued.

### Application Page System Agent

Creates test-scenario and solution pages that connect products, standards, and inquiry needs.

### Standard Relation Auditor

Reviews standards relationships and prevents unsupported compliance claims.

### Internal Linking Architect

Builds and audits product/category/application/standard/article links.

### WordPress CPT / ACF Builder

Defines WordPress content types, taxonomies, and custom fields.

### WordPress Draft Publisher

Creates or updates WordPress drafts while preserving approval status.

### Product Publish QA Agent

Checks whether a page is safe and complete enough to publish.

### Asset Library Manager

Controls image, PDF, diagram, and download asset usage.

### Content Refresh Auditor

Finds old content, broken links, stale assets, outdated PDFs, and review gaps.

### Inquiry Conversion Agent

Improves forms and CTA routes for qualified technical inquiries.

### Data Import / Export Agent

Maps spreadsheets and structured data into WordPress-compatible product records.

## Recommended Operating Sequence

For any new product:

1. Product Knowledge Base Agent
2. Product Lifecycle Manager
3. Standard Relation Auditor
4. Asset Library Manager
5. Application Page System Agent when relevant
6. Internal Linking Architect
7. WordPress Draft Publisher
8. Product Publish QA Agent
9. Inquiry Conversion Agent
10. Content Refresh Auditor after publication

## Default Safety Rule

Agents should create drafts and review outputs by default. Publishing, production changes, DNS changes, plugin installation, and bulk imports require explicit approval.
