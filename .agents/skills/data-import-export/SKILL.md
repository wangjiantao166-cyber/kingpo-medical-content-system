---
name: data-import-export
status: deprecated
replacement: data-migration-sync
do_not_use_for_new_work: true
---

# Data Import / Export

## Use When

Use this skill when importing product data from Excel/CSV, exporting WordPress product records, preparing bulk updates, or generating missing-field reports.

## Input Types

- Excel product sheet
- CSV export
- PDF-derived table
- Structured product record
- WordPress export
- ACF field mapping

## Required Mapping

Map each column to:

- WordPress content type
- ACF field
- Taxonomy
- Relationship field
- SEO field
- Asset field
- Source/verification field

## Validation Checks

- Required fields missing
- Duplicate products
- Duplicate slugs
- Invalid product status
- Missing source record
- Unapproved asset
- Unverified standard
- Conflicting parameters

## Output

- Import-ready mapping table
- Missing-field report
- Conflict report
- Draft import recommendation
- Fields requiring human review

## Prohibited

- Do not bulk publish imported products.
- Do not overwrite confirmed fields with weaker sources.
- Do not import competitor facts as KingPo data.



