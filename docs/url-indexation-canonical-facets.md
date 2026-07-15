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

## Facet Matrix

| Facet or URL Type | Crawl | Index | Canonical | Sitemap | Empty Result |
| --- | --- | --- | --- | --- | --- |
| Product domain archive | yes | yes | self | yes | 404 or noindex utility page |
| Curated test-method landing page | yes | after review | self | after review | 404 |
| Application or industry landing page | yes | after review | self | after review | 404 |
| Sort parameter | controlled or nofollowed | no | base archive | no | not applicable |
| Pagination | yes when needed | design-dependent | self or series strategy | normally no | 404 |
| Multiple arbitrary filters | restricted | no | base or no canonical if blocked | no | 404 |
| Internal search | accessible | noindex | self | no | 200 |
| Invalid parameter | no useful crawl | no | base or 404 | no | 404 |

Parameter order, case, trailing slash, and empty parameters must be normalized. JavaScript filter links must be designed so they do not create uncontrolled crawl spaces.

## Sitemap Rule

Sitemaps may include only URLs that are:

- HTTP 200;
- indexable;
- self-canonical;
- not redirected;
- not ordinary filters;
- not internal workflow states;
- supported by a meaningful `lastmod`.

Do not refresh `lastmod` unless the visible page content or primary structured data changed in a meaningful way.

## Internal Link Rule

Do not enforce a fixed number of links. Link only when the relationship helps a buyer, engineer, lab, or search crawler understand a real relationship.

Every important relationship should be bidirectional where appropriate:

- Product to standard mapping and standard page back to mapped products;
- Product to application and application back to recommended products;
- Product to related accessories and accessories back to parent product;
- Resource to product/application/standard entities it supports.
