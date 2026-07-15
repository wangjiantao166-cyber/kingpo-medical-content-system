---
name: wordpress-draft-publisher
description: Create or update WordPress draft content from approved structured records while preserving review and approval controls.
---

# WordPress Draft Publisher

## Use When

Use this skill after a product, standard, application, or article record has been structured and reviewed enough to create a WordPress draft.

## Default Behavior

Create drafts by default. Do not publish unless the user explicitly approves publication.

## Draft Creation Inputs

- Content type
- Title
- Slug
- Structured fields
- Body sections
- SEO fields
- Related links
- Assets
- Inquiry CTA
- Review status

## Workflow

1. Confirm target WordPress environment is staging or approved.
2. Create or update draft.
3. Fill structured fields.
4. Attach approved assets only.
5. Add internal links.
6. Set SEO fields.
7. Set status to draft or pending review.
8. Return draft URL or record ID when available.

## Output

- Created/updated item
- Draft status
- Missing fields
- Warnings
- Next review step

## Prohibited

- Do not publish by default.
- Do not upload unapproved images or PDFs.
- Do not overwrite existing product data without change notes.
- Do not modify production forms, themes, plugins, or DNS.
