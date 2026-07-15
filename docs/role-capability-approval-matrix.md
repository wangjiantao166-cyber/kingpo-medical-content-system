# Role Capability and Approval Matrix

## Purpose

This matrix defines who may edit, review, approve, publish, or sync each high-risk area.

## Roles

| Role | Main Permission | Cannot Do |
| --- | --- | --- |
| `content_editor` | Draft page copy, FAQ, summaries, alt text suggestions | Approve specs, claims, mappings, URLs, or publish |
| `product_data_editor` | Create product and specification drafts with source IDs | Approve high-risk claims or publish |
| `technical_reviewer` | Approve technical parameters and configuration notes | Approve certification/compliance wording alone |
| `standards_reviewer` | Approve standard mappings and claim wording | Publish production pages |
| `asset_reviewer` | Approve public use of images, PDFs, diagrams, AI visuals | Approve product facts or claims |
| `seo_reviewer` | Approve canonical, noindex, schema, sitemap, and slug decisions | Override product facts or claims |
| `publisher` | Move approved content to staging or production | Modify high-risk facts during publish |
| `administrator` | Manage platform settings and emergency access | Bypass evidence and approval requirements |

## Approval Rules

| Action | Required Role |
| --- | --- |
| Edit product display copy | `content_editor` |
| Edit technical parameter draft | `product_data_editor` |
| Approve technical parameter | `technical_reviewer` |
| Approve standard mapping | `standards_reviewer` |
| Approve compliance/certification wording | `standards_reviewer` plus publisher gate |
| Approve public customer asset | `asset_reviewer` |
| Approve AI concept image for public use | `asset_reviewer` |
| Approve URL slug/canonical/noindex | `seo_reviewer` |
| Publish to production | `publisher` |
| Bulk import or sync | `publisher` plus `data-migration-sync` dry-run report |

Any role may create questions or draft suggestions. Only the owning reviewer may approve the controlled field.
