# Claim Evidence Ledger

## Purpose

Every public technical, standards, certification, calibration, safety, medical, customer, delivery, pricing, warranty, and performance claim must be traceable to evidence.

The system must never publish a high-risk claim because an AI draft sounds plausible.

## Claim Record

Each claim should be stored as a structured record with:

```text
claim_id
entity_id
field_or_section
claim_text
claim_type
risk_level
source_ids
evidence_level
allowed_surfaces
approved_wording
prohibited_wording
reviewer
approval_date
review_due_date
status
```

## High-Risk Claim Types

High-risk claims include:

- complies with, meets, conforms to, certified, approved;
- calibration, accredited, ISO/IEC 17025;
- medical, clinical, registration testing, patient safety;
- precision, accuracy, guaranteed performance;
- customer names, projects, installations, case studies;
- delivery time, warranty, price, stock, annual sales;
- R&D percentage, factory capability, exclusive technology.

## Public Wording Rule

Use cautious wording unless a reviewer approves stronger wording.

Allowed examples:

- "Designed for test scenarios related to IEC 60601-1 after configuration review."
- "Can be configured for selected clauses when fixtures and parameters are confirmed."
- "Please confirm the final standard edition and test item with KingPo before procurement."

Blocked examples without evidence:

- "Fully certified to IEC 60601-1."
- "Guaranteed compliance with all clauses."
- "Approved by UL."
- "Used by [customer name]" unless public permission exists.
