# SEO Site Architecture and Agent Coordination

## Purpose

This document defines the professional site architecture and multi-agent coordination model for the KingPo B2B test equipment website system.

The goal is to build a searchable, crawlable, maintainable website structure before large-scale product publishing begins. The structure should support product discovery, standards-based discovery, application-based discovery, and technical article clusters.

This is inspired by mature B2B test equipment websites such as LISUN, but the KingPo system must remain original, source-based, and appropriate to KingPo's product scope.

## Why KingPo Needs This Framework

KingPo products belong to technical B2B testing equipment categories. Buyers do not search only by product model. They also search by:

- Test standard
- Test object
- Test method
- Application scenario
- Industry
- Sample type
- Test risk
- Certification or lab requirement

Therefore, the site should not be a flat product list. It should be a structured product knowledge system with four connected content axes:

1. Products
2. Applications
3. Standards
4. Technical Resources

## Recommended SEO Pyramid

### L0: Homepage

The homepage is the authority hub. It should introduce KingPo as a professional test equipment supplier and route users to the most important content clusters.

Homepage should link to core product categories, major applications, standards center, technical resources, inquiry/contact page, and selected high-value product pages.

The homepage should not become a random link directory.

### L1: Core Pillar Pages

Recommended L1 structure:

- Battery Testing Equipment
- Environmental Test Chambers
- Safety Compliance Test Equipment
- IEC Test Equipment
- Medical Test Equipment
- IP Waterproof / Dustproof Test Equipment
- Plug, Socket and Gauge Test Equipment
- Flame and Fire Resistance Test Equipment
- Applications
- Standards
- Technical Resources

Each L1 page should be a strong pillar page with a clear introduction, subcategory links, application links, standard links, product links, and inquiry CTA.

### L2: Subcategory, Application, and Standard Pages

L2 pages support more specific search intent, such as Battery Crush Test Equipment, Battery Nail Penetration Test Equipment, Medical Electrical Safety Test Equipment, Active Implantable Medical Device Test Equipment, BCI Test Equipment, Defibrillation Compatibility Test Equipment, IEC 60601 Related Test Equipment, and Battery Safety Testing Applications.

### L3: Product Pages and Technical Articles

L3 pages capture model-specific, long-tail, and technical intent, such as product model pages, selection guides, standards FAQ pages, and testing method overviews.

## Core Internal Linking Model

Homepage links down to L1 pages and selected priority pages.

L1 pages link down and across to L2 subcategories, priority products, applications, standards, technical articles, and inquiry pages.

L2 pages link down, up, and across to parent L1 pages, related products, related applications, standards, and technical articles.

Product pages link up and across to parent category, standards, applications, related products, PDF resources, and inquiry pages.

Technical articles should link back to relevant L1/L2 pillar pages and product pages.

## Anchor Text Rules

Use mixed but natural anchor text:

- Exact keyword: Battery Crush Test Equipment
- Descriptive long-tail: equipment for battery crush safety testing
- Category phrase: battery safety test equipment
- Application phrase: lithium battery abuse testing

Avoid repeated exact-match anchors, linking the same target many times in one article, generic anchors like click here, and sitewide footer keyword stuffing.

## Agent Coordination Model

No single agent should independently publish a page without other agents checking the related areas.

### Required Sequence for New Website Architecture

1. `multi-agent-workflow-coordinator` defines the task scope and required agents.
2. `seo-site-architecture-planner` creates the L0/L1/L2/L3 map.
3. `product-knowledge-base` checks whether each proposed product/category has real source support.
4. `content-cluster-planner` builds product/application/standard/article clusters.
5. `navigation-mega-menu-architect` translates the architecture into navigation and breadcrumbs.
6. `homepage-authority-hub` decides which hubs and clusters should be linked from the homepage.
7. `standard-relation-auditor` reviews standard-related pages and wording.
8. `google-seo-eeat-content` checks customer-first value, E-E-A-T, S-CTs, and metadata.
9. `internal-linking-architect` validates link direction, anchor text, and crawl paths.
10. `orphan-link-auditor` checks orphan pages, weak pages, broken links, and over-optimization risks.
11. `product-publish-qa` performs final publication readiness review.

### Required Sequence for a New Product Page

1. `product-knowledge-base`
2. `product-lifecycle-manager`
3. `standard-relation-auditor`
4. `ai-product-page-generator`
5. `google-seo-eeat-content`
6. `content-cluster-planner`
7. `internal-linking-architect`
8. `asset-library-manager`
9. `wordpress-draft-publisher`
10. `product-publish-qa`

## Deliverables Before WordPress Build

Before building or importing content into WordPress, create:

- L0/L1/L2/L3 site architecture map
- Product category map
- Application map
- Standards map
- Technical resource map
- URL slug map
- Navigation and mega menu map
- Breadcrumb rules
- Internal linking rules
- Content cluster matrix
- Priority publishing roadmap

## Quality Controls

Every proposed page should have page type, search intent, primary keyword, secondary keywords, parent page, child pages, required inbound links, required outbound links, product/source support, index/noindex recommendation, and review status.

## Avoid These Risks

- Flat product catalog with no application or standard links
- Product pages with no inbound links
- Technical articles that do not link to commercial pages
- Overloaded homepage with too many unrelated links
- Repeated exact-match anchors
- Publishing pages without product source support
- Copying competitor structure too closely
- Treating domestic Chinese wording as export-ready English copy
