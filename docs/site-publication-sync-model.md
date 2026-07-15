# Site Publication Sync Model

## Purpose

The same product master record may be published to multiple sites, languages, and WordPress post IDs. Site publication data must be separate from the product master record.

## Publication Record

Use `schemas/site-publication-record.schema.json` to store:

```text
publication_id
entity_id
site_target
locale
wordpress_post_id
public_url
slug
seo_title
meta_description
canonical_url
indexation_status
publication_state
published_at
last_synced_at
source_content_version
```

## Sync Direction

Default sync direction:

```text
structured record → WordPress staging draft → reviewed WordPress page → publication record
```

WordPress may be used as an editorial interface, but high-risk facts must sync back only through controlled review.

## Conflict Handling

If WordPress content conflicts with structured records:

1. Mark the publication as `blocked`.
2. Create a `source_conflict` blocker.
3. Route product facts to `product-data-governance`.
4. Route claim or standard conflicts to `standards-claims-compliance`.
5. Do not publish until the conflict is resolved.

## Slug and Canonical Rule

Slug, canonical, index/noindex, and sitemap decisions belong to `technical-seo-link-graph`, not ordinary content editors.
