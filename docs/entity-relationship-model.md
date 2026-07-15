# Entity Relationship Model

## Core Entities

```mermaid
erDiagram
  SOURCE_RECORD ||--o{ PRODUCT_RECORD : supports
  SOURCE_RECORD ||--o{ SPECIFICATION_RECORD : supports
  SOURCE_RECORD ||--o{ CLAIM_RECORD : supports
  PRODUCT_RECORD ||--o{ SPECIFICATION_RECORD : has
  PRODUCT_RECORD ||--o{ STANDARD_MAPPING : maps_to
  STANDARD_RECORD ||--o{ STANDARD_MAPPING : referenced_by
  PRODUCT_RECORD ||--o{ ASSET_MANIFEST : uses
  APPLICATION_RECORD }o--o{ PRODUCT_RECORD : recommends
  PAGE_BRIEF }o--|| PRODUCT_RECORD : may_describe
  PAGE_BRIEF }o--|| APPLICATION_RECORD : may_describe
  RELEASE_GATE ||--o{ CLAIM_RECORD : checks
```

## Relationship Principles

- A standard does not prove a product complies by itself.
- A `standard_mapping` record is required to connect product, standard, clause/test item, configuration, evidence, and reviewer.
- Specifications are structured records, not WYSIWYG text.
- Claims are reviewed independently from marketing copy.
- Assets must carry rights, source, and public-use status.
