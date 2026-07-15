# Content Types and ACF Field Map

## Implementation Rule

This file defines the WordPress-facing content model. Field implementation details must follow `docs/wordpress-implementation-spec.md` and the JSON schemas in `schemas/`.

Every field group must define:

```text
field_key
label
content_type
field_type
required
cardinality
default
validation
conditional_logic
public_visibility
editable_roles
translatable
REST_name
source_of_truth
AI_edit_allowed
```

## Recommended CPTs

```text
product
application
standard
standard_mapping
resource
case
```

Do not create ordinary public CPTs for product category, asset, or inquiry personal data.

## Recommended Taxonomies

```text
product_domain
application_industry
test_object
test_method
standard_organization
resource_type
asset_type
```

Workflow fields such as product lifecycle, verification status, claim risk, and editorial status should be controlled fields or workflow states, not public archive taxonomies.

## Product Core Fields

| Field Key | Label | Type | Required | Source of Truth | AI Edit |
| --- | --- | --- | --- | --- | --- |
| `product_id` | Stable product ID | text | yes | schema | no |
| `record_type` | Record type | select | yes | schema | no |
| `english_name` | English name | text | yes | reviewed source | draft only |
| `chinese_name` | Chinese name | text | no | reviewed source | draft only |
| `model` | Model | text | conditional | reviewed source | no |
| `product_family` | Product family | relationship | no | reviewed source | no |
| `lifecycle_status` | Lifecycle status | select | yes | reviewer | no |
| `primary_product_domain` | Primary product domain | taxonomy | yes | IA review | no |
| `site_targets` | Site targets | checkbox | yes | publisher | no |
| `public_visibility` | Public visibility | select | yes | publisher | no |

## Specification Fields

Specifications must be structured records, not a single WYSIWYG table.

| Field Key | Label | Type | Required | Source of Truth | AI Edit |
| --- | --- | --- | --- | --- | --- |
| `specification_id` | Specification ID | text | yes | schema | no |
| `spec_group` | Group | text | no | reviewer | draft only |
| `spec_name` | Name | text | yes | reviewed source | draft only |
| `value_type` | Value type | select | yes | reviewer | no |
| `nominal_value` | Nominal value | mixed | conditional | reviewed source | no |
| `minimum_value` | Minimum value | number | conditional | reviewed source | no |
| `maximum_value` | Maximum value | number | conditional | reviewed source | no |
| `unit` | Unit | text | conditional | reviewed source | no |
| `tolerance` | Tolerance | text | no | reviewed source | no |
| `accuracy` | Accuracy | text | no | reviewed source | no |
| `test_condition` | Test condition | text | no | reviewed source | no |
| `source_id` | Source ID | relationship | yes | source record | no |
| `verification_status` | Verification status | select | yes | reviewer | no |

## Standard Mapping Fields

`standard_mapping` is an independent relationship entity. A standard page alone does not prove a product complies.

| Field Key | Label | Type | Required | Source of Truth | AI Edit |
| --- | --- | --- | --- | --- | --- |
| `mapping_id` | Mapping ID | text | yes | schema | no |
| `product_id` | Product | relationship | yes | product record | no |
| `standard_id` | Standard | relationship | yes | standard record | no |
| `edition` | Standard edition | text | conditional | official/owned source | no |
| `clause` | Clause | text | no | official/owned source | no |
| `test_item` | Test item | text | no | reviewed source | no |
| `relationship_type` | Relationship type | select | yes | standards reviewer | no |
| `coverage_scope` | Coverage scope | textarea | no | standards reviewer | no |
| `required_configuration` | Required configuration | textarea | no | engineering reviewer | no |
| `evidence_level` | Evidence level | select | yes | reviewer | no |
| `allowed_public_wording` | Allowed public wording | textarea | no | reviewer | no |
| `review_status` | Review status | select | yes | reviewer | no |

## Claim Fields

High-risk public wording must come from claim records.

| Field Key | Label | Type | Required | Source of Truth | AI Edit |
| --- | --- | --- | --- | --- | --- |
| `claim_id` | Claim ID | text | yes | schema | no |
| `claim_text` | Claim text | textarea | yes | draft/source | draft only |
| `claim_type` | Claim type | select | yes | reviewer | no |
| `risk_level` | Risk level | select | yes | reviewer | no |
| `source_ids` | Evidence sources | relationship | yes | source record | no |
| `approved_wording` | Approved public wording | textarea | conditional | reviewer | no |
| `prohibited_wording` | Prohibited wording | repeater | no | reviewer | no |
| `review_due_date` | Review due | date | conditional | reviewer | no |
| `status` | Claim status | select | yes | reviewer | no |

## Asset Fields

Ordinary images and files should use WordPress Media Library plus structured attachment fields. A separate resource record is needed only for downloads that require SEO, versioning, gated access, or replacement history.

| Field Key | Label | Type | Required | Source of Truth | AI Edit |
| --- | --- | --- | --- | --- | --- |
| `asset_id` | Asset ID | text | yes | schema | no |
| `asset_type` | Asset type | select | yes | asset reviewer | no |
| `source_id` | Source | relationship | yes | source record | no |
| `public_use_status` | Public use status | select | yes | asset reviewer | no |
| `alt_text` | Alt text | text | conditional | editorial review | draft only |
| `caption` | Caption | text | no | editorial review | draft only |
| `ai_generated` | AI generated | true_false | yes | asset reviewer | no |

## SEO Fields

SEO title and meta description must have one final source of truth. Preferred approach: use the selected SEO plugin as the final publishing source and synchronize approved custom fields only through controlled tooling.

Do not invent price, availability, rating, review, shipping, return policy, certification, or compliance data for schema.
