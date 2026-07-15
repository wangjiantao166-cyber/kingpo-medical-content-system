# Authoritative Source of Truth

## Purpose

This document decides which layer is allowed to own each type of information. It prevents WordPress, repository schemas, AI drafts, and legacy source pages from editing the same fact independently.

## Ownership Matrix

| Data Area | Authoritative Layer | WordPress Role | AI Role | Conflict Rule |
| --- | --- | --- | --- | --- |
| Product identity, model, family, lifecycle | Structured product record | Display and controlled editing only | Draft suggestions only | Product data reviewer decides. |
| Technical specifications | Specification records with source IDs | Render tables and admin review fields | No direct final edits | Missing or conflicting source blocks publication. |
| Standards and mappings | Standard and standard_mapping records | Display approved notices | Draft relation questions only | Standards reviewer decides. |
| Compliance, certification, calibration, medical claims | Claim ledger | Render approved wording only | No approval authority | Approved claim record overrides page copy. |
| Images and downloads | Asset manifest and Media Library metadata | Store files and render assets | May generate concept images only | Asset reviewer decides public-use status. |
| Page body copy | WordPress draft or page brief, depending on workflow | Editing surface | Draft and rewrite support | Claims and specs must be pulled from approved records. |
| SEO title and meta description | Selected SEO plugin after controlled sync | Final publishing field | Draft suggestions only | SEO reviewer/publisher decides. |
| Slug, canonical, indexation | Site publication record | Stores final URL fields | No final authority | Technical SEO reviewer decides. |
| Inquiry personal data | Form/CRM system | Collection and access control | No access unless explicitly approved | Privacy policy and role permissions decide. |

## Default Editing Model

The repository and schemas define the authoritative structure. WordPress is the first-stage publishing and editorial interface. WordPress may hold drafts and display fields, but it must not become an uncontrolled second truth for high-risk facts.

High-risk fields should be locked or role-restricted in WordPress:

- technical parameters;
- standard mappings;
- approved claim wording;
- certification or compliance badges;
- asset public-use status;
- URL and canonical decisions;
- publication status.

## Synchronization Rule

Every sync operation must record:

```text
source_content_version
target_site
wordpress_post_id
changed_fields
sync_direction
operator
timestamp
validation_result
```

If WordPress and the structured record disagree, the system must mark the field as `source_conflict` and block publication until reviewed.
