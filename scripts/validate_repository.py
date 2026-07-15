from __future__ import annotations

import json
import pathlib
import sys

import yaml
from jsonschema import Draft202012Validator, RefResolver


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "schemas"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def load_json(path: pathlib.Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path} is not valid JSON: {exc}")


def load_yaml(path: pathlib.Path) -> dict:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"{path} is not valid YAML: {exc}")


def schema_store() -> tuple[dict[str, dict], dict[str, dict]]:
    by_name = {}
    store = {}
    for path in SCHEMAS_DIR.glob("*.schema.json"):
        schema = load_json(path)
        by_name[path.name] = schema
        if "$id" in schema:
            store[schema["$id"]] = schema
        store[path.name] = schema
        store[str(path.resolve().as_uri())] = schema
    return by_name, store


def validator_for(schema: dict, store: dict) -> Draft202012Validator:
    resolver = RefResolver.from_schema(schema, store=store)
    return Draft202012Validator(schema, resolver=resolver)


def validate_instance(instance: dict, schema_name: str, schemas: dict, store: dict) -> list[str]:
    schema = schemas[schema_name]
    validator = validator_for(schema, store)
    return [error.message for error in sorted(validator.iter_errors(instance), key=lambda item: item.path)]


def main() -> None:
    schemas, store = schema_store()
    if not schemas:
        fail("No schemas found")

    for name, schema in schemas.items():
        if "$schema" not in schema or "title" not in schema:
            fail(f"Schema is missing required metadata: {name}")
        Draft202012Validator.check_schema(schema)

    manifest = ROOT / "skills-manifest.yaml"
    if not manifest.exists():
        fail("Missing skills-manifest.yaml")
    manifest_data = load_yaml(manifest)
    errors = validate_instance(manifest_data, "skills-manifest.schema.json", schemas, store)
    if errors:
        fail(f"skills-manifest.yaml failed schema validation: {errors[0]}")

    active_agents = {item["name"] for item in manifest_data["active_skills"]}
    if len(active_agents) != len(manifest_data["active_skills"]):
        fail("Duplicate active skill name in skills-manifest.yaml")
    for agent in active_agents:
        skill_path = ROOT / ".agents" / "skills-v2" / agent / "SKILL.md"
        if not skill_path.exists():
            fail(f"Missing v2 skill entry: {skill_path}")

    required_docs = [
        "docs/00-system-scope-and-sites.md",
        "docs/DOCUMENT-INDEX.yaml",
        "docs/authoritative-source-of-truth.md",
        "docs/role-capability-approval-matrix.md",
        "docs/site-publication-sync-model.md",
        "docs/source-tier-and-conflict-policy.md",
        "docs/claim-evidence-ledger.md",
        "docs/agent-contracts-and-state-machine.md",
        "docs/wordpress-implementation-spec.md",
        "docs/url-indexation-canonical-facets.md",
        "docs/schema-markup-matrix.md",
        "docs/deployment-backup-rollback-runbook.md",
        "docs/frontend-design-system-and-templates.md",
        "docs/editorial-authorship-ai-policy.md",
        "docs/standard-version-and-claim-policy.md",
    ]
    for doc in required_docs:
        if not (ROOT / doc).exists():
            fail(f"Missing required doc: {doc}")

    doc_index = load_yaml(ROOT / "docs" / "DOCUMENT-INDEX.yaml")
    for item in doc_index.get("documents", []):
        if item.get("status") == "normative" and item.get("do_not_route") is not False:
            fail(f"Normative document is not routable: {item.get('path')}")

    profile_dir = ROOT / "profiles" / "medical-cn"
    if profile_dir.exists():
        for path in profile_dir.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            if "do_not_route: true" not in text[:250]:
                fail(f"Profile file missing do_not_route frontmatter: {path}")

    valid_dir = ROOT / "tests" / "fixtures" / "valid"
    if valid_dir.exists():
        for path in valid_dir.glob("*.json"):
            instance = load_json(path)
            schema_name = instance.pop("$schema_file", None)
            if not schema_name:
                fail(f"Fixture missing $schema_file: {path}")
            errors = validate_instance(instance, schema_name, schemas, store)
            if errors:
                fail(f"Valid fixture failed {path}: {errors[0]}")

    invalid_dir = ROOT / "tests" / "fixtures" / "invalid"
    if invalid_dir.exists():
        for path in invalid_dir.glob("*.json"):
            instance = load_json(path)
            schema_name = instance.pop("$schema_file", None)
            if not schema_name:
                fail(f"Invalid fixture missing $schema_file: {path}")
            errors = validate_instance(instance, schema_name, schemas, store)
            if not errors:
                fail(f"Invalid fixture unexpectedly passed: {path}")

    print("Repository validation passed.")


if __name__ == "__main__":
    main()
