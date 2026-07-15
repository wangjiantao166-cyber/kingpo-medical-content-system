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

### 3. Application

Represents test scenarios and solution pages. Application pages should connect user intent to products, standards, test objects, test items, and inquiry forms.

### 4. Standard

Represents standard-based discovery pages. A related standard is not proof that a product fully complies with that standard.

### 5. Technical Article

Represents long-tail SEO and technical education content.

### 6. Asset

Represents images, PDFs, diagrams, catalogs, manuals, certificates, and downloadable files.

### 7. Case / Installation / Project Record

Use only when authorization exists. If no customer authorization exists, create internal project notes or anonymized scenario examples instead.

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

Product Category links to products, applications, standards, technical articles, and inquiry pages.

Product links to category, standards, applications, PDFs, articles, related products, and inquiry pages.

Standard links to related products, applications, articles, and evidence notes.

Application links to recommended products, standards, test objects, test items, and inquiry pages.

Technical Article links to products, applications, standards, PDF resources, and inquiry pages.

## Publishing Principles

Default state for generated content is draft.

A page may be published only after product status, source records, standard relationships, claim risk, approved assets, SEO fields, internal links, and inquiry CTA are complete.

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
