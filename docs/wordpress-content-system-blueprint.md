# WordPress Product Content System Blueprint

## Purpose

This document defines the target system for a self-maintainable KingPo Chinese B2B medical test equipment website.

The goal is not only to publish pages, but to create a durable product knowledge system where products, standards, applications, technical articles, PDFs, images, and inquiry forms can be maintained over time.

The site may study the information architecture of strong B2B equipment websites such as LISUN, but it must not copy their text, images, layouts, model naming systems, tables, claims, or customer cases.

## System Positioning

The site should work as:

- A product catalog
- A technical knowledge base
- A standards-based equipment discovery system
- An application and test-scenario library
- A PDF and asset download center
- A qualified inquiry generation system
- A long-term SEO content platform

## Recommended Technology Route

Use WordPress as the first-phase implementation layer.

Recommended stack:

- WordPress
- Lightweight custom theme or maintainable block theme
- ACF Pro or equivalent structured custom fields
- Custom Post Types for Products, Standards, Applications, Technical Articles, Assets, and Case/Installation records
- Rank Math or Yoast SEO
- Fluent Forms, Gravity Forms, or equivalent inquiry form plugin
- SMTP plugin for mail testing
- Image optimization and WebP plugin
- Caching/performance plugin
- Backup and security plugins

Do not start with NestJS unless there is a confirmed need for a custom application layer. WordPress should first become the content source of truth.

## Core Content Types

### 1. Product

Represents equipment, test systems, modules, accessories, or product families.

Required relationships:

- Product Category
- Related Standards
- Related Applications
- Related Technical Articles
- Related PDFs and images
- Related Products

### 2. Product Category

Represents major catalog entry points. Category pages should not be thin list pages. They should explain test needs, standards, applications, and inquiry routes.

First-phase category examples:

- BCI test equipment
- Active implantable medical device test equipment
- Neural stimulation test equipment
- Pacemaker / ICD test equipment
- Electrophysiological signal simulation and closed-loop testing
- Transcutaneous energy transfer test equipment
- Defibrillation compatibility test equipment
- Magnetic field / TMS / ultrasound / EMC compatibility test equipment
- Electrode, lead, insulation, withstand voltage, and tissue-interface test equipment
- Medical electrical safety test equipment

### 3. Application

Represents test scenarios and solution pages.

Examples:

- BCI closed-loop testing
- Active implantable medical device verification testing
- Neural stimulation waveform and load simulation
- Pacemaker low-frequency electromagnetic immunity testing
- Transcutaneous energy transfer verification
- Defibrillation compatibility testing
- TMS compatibility testing

Application pages should connect user intent to products, standards, test objects, test items, and inquiry forms.

### 4. Standard

Represents standard-based discovery pages.

Standards should be handled cautiously. A related standard is not proof that a product fully complies with that standard.

Each standard page should classify product relationships as:

- Main standard
- Supporting standard
- Background standard
- Not applicable
- Human verification required

### 5. Technical Article

Represents long-tail SEO and technical education content.

Articles should explain testing principles, selection questions, standard mapping logic, sample preparation, and inquiry preparation. They must link back to relevant products, applications, standards, and inquiry pages.

### 6. Asset

Represents images, PDFs, diagrams, catalogs, manuals, certificates, and downloadable files.

Every asset must have:

- Source
- Public-use permission status
- Related products or pages
- Version/date
- Alt text or description
- Replacement/deprecation status when needed

### 7. Case / Installation / Project Record

Use only when authorization exists. If no customer authorization exists, create internal project notes or anonymized scenario examples instead.

Do not invent customers, countries, installations, certificates, or results.

## Product Status Model

Every product or direction must have one clear status:

- Existing product
- Custom development available
- R&D direction
- R&D reference / needs confirmation
- Internal only
- Not public
- Legacy product
- Discontinued

Product status controls page wording, CTA, indexability, and publish approval.

## Relationship Model

Every public page should be part of a linking graph.

Product Category links to:

- Products
- Applications
- Standards
- Technical Articles
- Inquiry page

Product links to:

- Category
- Related standards
- Applications
- PDFs
- Technical articles
- Related products
- Inquiry page

Standard links to:

- Related products
- Related applications
- Related articles
- Source/evidence notes

Application links to:

- Recommended products
- Related standards
- Test objects
- Test items
- Inquiry page

Technical Article links to:

- Products
- Applications
- Standards
- PDF resources
- Inquiry page

## Publishing Principles

Default state for generated content is draft.

A page may be published only after:

- Product status is clear
- Source ownership is classified
- Key fields have source records
- Standard relationships are reviewed
- Medical/regulatory claim risk is reviewed
- Images and PDFs are approved for public use
- SEO title, meta description, slug, FAQ, and internal links are complete
- Inquiry CTA is present
- Mobile and desktop layout are checked

## First Implementation Milestone

Create a staging WordPress environment and implement:

1. Product CPT
2. Standard CPT
3. Application CPT
4. Technical Article CPT
5. Asset records or media fields
6. Product status fields
7. Source and verification fields
8. Relationship fields
9. Inquiry CTA field group
10. SEO field mapping

Then create 5 sample pages:

1. BCI test equipment category/page
2. Active implantable medical device test equipment category/page
3. EEG closed-loop dynamic simulation test system page
4. ISO 14708 related equipment standard page
5. Medical test equipment technical inquiry page
