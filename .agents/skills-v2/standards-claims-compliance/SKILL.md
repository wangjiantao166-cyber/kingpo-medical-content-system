# standards-claims-compliance

## Purpose

Own standards relationships, compliance wording, certification/calibration claims, and claim evidence approvals.

## Use Conditions

Use for IEC, ISO, EN, UL, UN ECE, SASO, BIS, ASTM, ANSI/AAMI, IEEE, GB, YY, YY/T, calibration, certification, medical, safety, or accuracy claims.

## Do Not Use Conditions

Do not copy paid standard text, invent clauses, or approve claims without evidence and reviewer.

## Accepted Input Schema

- `schemas/standard-record.schema.json`
- `schemas/standard-mapping.schema.json`
- `schemas/claim-record.schema.json`

## Output Schema

Approved public wording, blocked claim list, standard mapping review, and review due date.

## Blocking Conditions

Block if evidence level is insufficient, edition is unknown without edition-independent justification, reviewer is missing, or public wording overstates coverage.

## Handoff Rules

Approved wording may go to `content-strategy-authoring`; blocked claims must go to `release-quality-gate`.
