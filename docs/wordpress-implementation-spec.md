# WordPress Implementation Spec

## Content Types

Recommended CPTs:

```text
product
application
standard
standard_mapping
resource
case
```

Do not create public CPTs for ordinary product categories, assets, or inquiries.

- Product category belongs in hierarchical taxonomy `product_domain`.
- Ordinary assets belong in WordPress Media Library with structured attachment fields.
- Inquiries should be managed by a form/CRM workflow with privacy and retention controls.

## Taxonomies

```text
product_domain
application_industry
test_object
test_method
standard_organization
resource_type
asset_type
```

Do not expose workflow fields such as lifecycle status, verification status, claim risk, or editorial status as public archives.

## Field Definition Requirements

Each ACF or custom field must define:

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

## SEO Source of Truth

Choose one final source of truth for SEO title and meta description:

- SEO plugin fields, or
- custom fields synchronized into the SEO plugin.

Do not allow both to be edited independently.
