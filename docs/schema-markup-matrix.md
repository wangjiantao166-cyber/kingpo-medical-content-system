# Schema Markup Matrix

## Purpose

Structured data must describe verified page content. It must not invent price, availability, ratings, reviews, shipping, return policy, certification, compliance, or customer claims.

For custom B2B equipment that is not directly purchased online, prefer product snippet style markup over merchant-listing assumptions.

## Page Matrix

| Page Type | Allowed Schema | Required Evidence | Blocked Fields |
| --- | --- | --- | --- |
| Home | `Organization`, `WebSite`, `BreadcrumbList` | Organization profile, site search if implemented | fake sameAs links |
| Product family | `Product`, `BreadcrumbList` | product record, approved specs, approved assets | price, rating, availability, unsupported certification |
| Product model | `Product`, variant strategy when confirmed | model-specific product record | invented variants or offers |
| Application | `WebPage`, `Article` or `TechArticle` when appropriate | page brief and source records | false standards coverage |
| Standard overview | `Article` or `TechArticle` | official standard source for title/scope | copyrighted standard text, compliance claims |
| Standard mapping | `WebPage`, `BreadcrumbList` | approved standard_mapping record | unreviewed clause claims |
| Technical resource | `Article` or `TechArticle` | source records and reviewer | fake author expertise |
| Video page | `VideoObject` | actual video asset and metadata | generated duration/thumbnail claims |
| PDF/download page | `CreativeWork` or `DigitalDocument` when supported | asset manifest and version | fake access or copyright status |
| FAQ section | FAQ markup only when visible and allowed by current Google policy | reviewed visible FAQ | hidden or mass-generated FAQ |

## Review Rule

Schema output must be reviewed by `technical-seo-link-graph` and blocked by `release-quality-gate` if it contains unsupported commercial, compliance, or review data.
