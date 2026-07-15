---
name: product-knowledge-base
description: Convert KingPo product sources into structured, source-recorded product records for WordPress product catalog maintenance.
---

# Product Knowledge Base

## Use When

Use this skill when adding or updating a product, product family, test system, module, R&D direction, or product category from spreadsheets, PDFs, images, old website pages, internal notes, or user confirmations.

## Goal

Create a structured product record that can later be reviewed, linked, drafted in WordPress, and maintained over time.

## Required Inputs

- Product source files or URLs
- Product name or direction
- Source ownership classification
- Any available product images, PDFs, or parameter tables
- User/boss confirmation if available

## Source Classification

Classify every source as one of:

- KingPo owned official source
- User-confirmed source
- Historical KingPo source
- Internal reference
- Competitor reference
- Public standard/source reference
- Needs verification

Competitor sources may not be used as KingPo product facts.

## Output Fields

Produce:

- Chinese product name
- English product name
- Model number
- Product family
- Product category
- Product status
- Test object
- Sample type
- Test items
- Technical parameters
- Related standards
- Related applications
- Related products
- Images and PDFs
- Source notes per field
- Human verification status
- Public-use status

## Workflow

1. Inventory all sources.
2. Extract facts only from owned or confirmed sources.
3. Mark missing or conflicting information as `needs human confirmation`.
4. Separate existing products from R&D directions.
5. Create a structured product record.
6. Recommend whether the record is ready for drafting, needs review, or should remain internal.

## Prohibited

- Do not invent specifications.
- Do not infer compliance from a related standard.
- Do not convert competitor products into KingPo products.
- Do not mark R&D reference directions as existing products.
- Do not publish or push to WordPress directly.
