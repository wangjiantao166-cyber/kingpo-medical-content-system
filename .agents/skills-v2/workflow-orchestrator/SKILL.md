# workflow-orchestrator

## Purpose

Route work by risk, choose the next v2 agent, enforce the state machine, and prevent profile or legacy documents from overriding normative docs.

## Use Conditions

Use for new tasks, architecture changes, workflow changes, and any handoff between agents.

## Do Not Use Conditions

Do not author product copy, approve claims, change WordPress production, or publish pages.

## Accepted Input Schema

- `schemas/agent-handoff.schema.json`
- task request with scope, entity IDs, risk, desired output, and constraints

## Output Schema

- routing decision
- state transition proposal
- blockers from `common-definitions.schema.json`

## Blocking Conditions

Block if the request depends on a `do_not_route` profile file without explicit profile scope, or if production changes are requested without human approval.

## Handoff Rules

Read `docs/DOCUMENT-INDEX.yaml` first. Route only to active v2 agents in `skills-manifest.yaml`.
