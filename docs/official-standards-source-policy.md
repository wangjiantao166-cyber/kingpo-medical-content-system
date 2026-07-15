# Official Standards Source Policy

## Purpose

This document defines how KingPo agents should handle standards information when product source materials are incomplete.

The core rule is simple: standards must not be invented.

Agents may use official or authoritative standards organization sources to understand standard titles, scope, standard families, test application context, and public descriptions. However, agents must not fabricate standard versions, clause numbers, test conditions, acceptance criteria, certification status, or KingPo product compliance.

## Priority Standard Sources

When standard information is missing or incomplete, prefer official or authoritative sources such as:

- IEC: International Electrotechnical Commission
- ISO: International Organization for Standardization
- EN / European Standards via CEN, CENELEC, ETSI, or official European standards bodies
- UL: UL Standards & Engagement / Underwriters Laboratories related official sources
- UN ECE: United Nations Economic Commission for Europe
- SASO: Saudi Standards, Metrology and Quality Organization
- BIS: Bureau of Indian Standards
- ANSI / AAMI official or standards catalog sources
- ASTM official standards catalog sources
- IEEE official standards catalog sources
- National standards bodies or official government/regulatory standards catalogs when relevant

Use official catalog pages, public summaries, scope descriptions, standard title pages, or official previews where available.

## What Official Sources Can Support

Official standards sources may support standard number, standard title, publishing organization, standard family, general scope, publicly described application area, whether a standard appears relevant for a test object or product direction, and whether a page should treat it as main, supporting, background, or needs verification.

## What Official Sources Cannot Automatically Support

Official standards sources do not automatically prove KingPo product compliance, certification or approval, test pass result, suitability for registration testing, full clause coverage, exact test setup for a specific customer sample, product technical parameters, or legal right to reproduce paid standard text.

## Paid Standards and Copyright Rule

Many standards are copyrighted and paid. Do not reproduce full standard text, tables, figures, clauses, or detailed requirements unless the user provides licensed material and explicit permission for internal use.

For public pages, summarize only high-level relevance in original wording.

## Required Fields for Standard Mapping

Every standard mapping record should include:

- Standard number
- Standard title
- Organization
- Standard family
- Confirmed version or `version not confirmed`
- Public source URL or user-provided source reference
- Related test object
- Possible test item
- Relationship type: main, supporting, background, not applicable, or human verification required
- Confidence level
- Human verification required
- Allowed public wording
- Prohibited wording

## Safe Public Wording

Preferred wording:

- This product direction is related to test scenarios involving ...
- This standard may be relevant when evaluating ...
- Standard applicability should be confirmed based on sample type, version, and test conditions.
- The final test method and acceptance criteria should be confirmed by the laboratory, certification body, or customer.

Avoid unless verified:

- Fully complies with ...
- Certified to ...
- Meets all clauses of ...
- Guaranteed to pass ...
- Approved for registration testing ...
- Equivalent to a competitor product certified under ...

## Agent Behavior

When source material is incomplete:

1. Look for official standard organization information.
2. Record source URL and what it actually supports.
3. Do not infer product compliance.
4. Mark uncertain version, clause, or applicability fields as needing human confirmation.
5. Use cautious language in product pages.
6. Ask for human confirmation when a page depends on a specific clause, test condition, or standard version.
