# AI Product Page Generation Guide

## Purpose

This guide defines how to generate English product page drafts from original product materials while keeping the content professional, accurate, buyer-focused, and safe for SEO.

AI-generated pages are drafts. They require source review and human approval before publishing.

## Input Materials

Use the original product page or source materials first:

- KingPo official product page
- Product PDF or catalog
- Product spreadsheet
- Product photos or diagrams
- User-confirmed notes
- Standard mapping sheet
- Approved internal technical notes

If the original material is incomplete, public information may be used for background understanding only, including:

- Brand official websites
- Related standard descriptions
- Industry application background
- Comparable product category pages
- Laboratory or certification context

Competitor information must not become KingPo product facts.

## Flexible Structure Rule

Do not force every page into the same rigid template.

Under Product Overview, choose modules based on the product's actual characteristics, testing purpose, customer concerns, and overseas B2B buyer reading habits.

Possible modules:

- Key Features
- Test Principle
- Standard Compliance / Standard Direction
- Applications
- Test Objects
- Configuration Notes
- Selection Guide
- Technical Specifications
- Software and Control
- Fixtures and Accessories
- PDF Downloads
- FAQ

Do not repeat content only to fill a template.

## Content Expansion Rules

AI may reasonably expand professional context, but must not invent facts.

Allowed expansion:

- Explain product purpose.
- Explain test purpose or principle.
- Explain common application scenarios.
- Explain what buyers should confirm before purchase.
- Explain how laboratories, manufacturers, and certification bodies may use the equipment.
- Add cautious standard background when source-supported or clearly framed as background.

Not allowed:

- Inventing technical parameters.
- Inventing standard versions or clause numbers.
- Inventing certification or compliance status.
- Inventing customer cases.
- Inventing price, stock, delivery time, or warranty.
- Claiming clinical or regulatory outcomes.

## Technical Parameter Rules

Technical specifications must have a clear source.

If a parameter is missing:

- Do not invent it.
- Mark it as `to be confirmed` if the field is needed.
- Or omit it if including it would create risk.

## Compliance and Standard Rules

Use cautious wording.

Preferred:

- The system is intended for test scenarios related to ...
- The equipment can be configured for ...
- Standard applicability should be confirmed according to the sample, version, and test conditions.
- The final test method should be confirmed by the laboratory or certification body.

Avoid unless verified:

- Fully complies with ...
- Certified to ...
- Guaranteed to pass ...
- Approved for ...
- Meets all clauses of ...

## Buyer-Focused Writing Rules

Write for overseas B2B buyers who need to understand quickly:

- What the equipment is
- Which test need it solves
- Which standard direction it relates to
- What type of sample it tests
- Why it is valuable for procurement or lab planning
- What configuration details must be confirmed
- What information to submit for quotation or solution evaluation

Use clear paragraphs, specific headings, and concise technical language.

Avoid:

- Overly academic explanations.
- Empty marketing language.
- Repetition.
- Keyword stuffing.
- Machine-translation style English.

## Recommended Output

For each generated page, provide:

- H1
- SEO title
- Meta description
- Suggested URL slug
- Product overview
- Flexible product-specific modules
- Technical specifications table if sourced
- Standard/compliance wording
- Applications
- Selection/configuration notes
- FAQ
- Inquiry CTA
- Source and uncertainty notes
- Fields requiring human confirmation

## Reusable Prompt

Use this prompt as a starting point, then adapt it to the product and available sources:

```text
Please generate a complete English product page based on the original product source materials.

Requirements:

1. Do not rigidly apply the same template to every product. The content structure under Product Overview should adapt to the product characteristics, testing purpose, customer concerns, and overseas B2B buyer reading habits. Suitable modules may include Key Features, Test Principle, Standard Compliance, Applications, Configuration Notes, Selection Guide, Technical Specifications, FAQ, and other relevant sections. Avoid repeated or filler sections.

2. If the original source is incomplete, use public information only for reasonable background supplementation, including brand official pages, related standard descriptions, industry information, and testing application context. All technical parameters must have a clear source. Do not invent parameters. Uncertain parameters should be marked as needing confirmation or omitted.

3. Optimize and moderately expand the content while preserving technical accuracy. The writing should be professional, natural, clear, and suitable for overseas B2B buyers. Avoid repetition, empty marketing claims, and keyword stuffing.

4. Strengthen the following areas: product purpose, applicable standards and compliance wording, test principle or test objective, typical applications, procurement value, selection or configuration notes, and real usage needs of laboratories, certification bodies, and manufacturers.

5. The style should be professional, clear, and trustworthy, but not overly long or academic. Help customers quickly understand what the equipment is, which standard or test need it relates to, what problem it solves, and why it may be suitable for procurement.

6. Separate confirmed product facts from background explanation. Mark missing or uncertain fields as needing human confirmation. Do not create unsupported compliance, certification, customer case, price, inventory, delivery, or clinical/regulatory claims.
```

## Final QA Before Use

Before using the generated page:

- Compare all specs against the source.
- Check standards and compliance wording.
- Remove unsupported claims.
- Add internal links.
- Add source notes.
- Add buyer-focused FAQ.
- Confirm product status.
- Confirm image and PDF permissions.
