# URL, Indexation, Canonical, and Facets

## Top-Level Navigation

Initial public navigation should use:

```text
Products
Applications
Standards & Test Methods
Resources
Projects / Capabilities
About KingPo
Contact / Request a Quote
```

## Product Domains

Use `product_domain` as the primary product hierarchy:

```text
Medical Device Test Equipment
Battery Safety Test Equipment
Environmental & IP Test Equipment
Electrical Safety Test Equipment
Flammability & Material Test Equipment
Plug, Socket, Cable & Gauge Test Equipment
Automotive & EV Test Equipment
Automation & Custom Test Systems
```

## Cross Taxonomies

Use separate dimensions for:

```text
application_industry
test_object
test_method
standard_organization
resource_type
```

Do not mix product domain, standard family, test method, and buyer industry into one public category tree.

## Indexation Rules

- Search result pages: `noindex`.
- Ordinary filter parameter combinations: not in sitemap and normally canonical to the base archive.
- Curated landing pages with unique value: may be indexed after review.
- Internal-only, R&D-only, not-public, or unreviewed pages: not in sitemap.
- Thin standard pages: do not publish or set `noindex`.
- Product family and near-duplicate model pages: require a canonical decision.
- Legacy models: require keep, merge, redirect, or retire decision.

## Internal Link Rule

Do not enforce a fixed number of links. Link only when the relationship helps a buyer, engineer, lab, or search crawler understand a real relationship.

Every important relationship should be bidirectional where appropriate:

- Product to standard mapping and standard page back to mapped products;
- Product to application and application back to recommended products;
- Product to related accessories and accessories back to parent product;
- Resource to product/application/standard entities it supports.
