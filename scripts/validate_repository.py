from __future__ import annotations

import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED_SCHEMA_FILES = [
    "source-record.schema.json",
    "product-record.schema.json",
    "specification-record.schema.json",
    "claim-record.schema.json",
    "standard-record.schema.json",
    "standard-mapping.schema.json",
    "application-record.schema.json",
    "page-brief.schema.json",
    "asset-manifest.schema.json",
    "agent-handoff.schema.json",
    "release-gate.schema.json",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def load_json(path: pathlib.Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path} is not valid JSON: {exc}")


def main() -> None:
    schemas_dir = ROOT / "schemas"
    for name in REQUIRED_SCHEMA_FILES:
        path = schemas_dir / name
        if not path.exists():
            fail(f"Missing schema: {name}")
        schema = load_json(path)
        if "$schema" not in schema or "title" not in schema:
            fail(f"Schema is missing required metadata: {name}")

    manifest = ROOT / "skills-manifest.yaml"
    if not manifest.exists():
        fail("Missing skills-manifest.yaml")

    required_docs = [
        "docs/00-system-scope-and-sites.md",
        "docs/source-tier-and-conflict-policy.md",
        "docs/claim-evidence-ledger.md",
        "docs/agent-contracts-and-state-machine.md",
        "docs/wordpress-implementation-spec.md",
        "docs/url-indexation-canonical-facets.md",
        "docs/frontend-design-system-and-templates.md",
        "docs/editorial-authorship-ai-policy.md",
        "docs/standard-version-and-claim-policy.md",
    ]
    for doc in required_docs:
        if not (ROOT / doc).exists():
            fail(f"Missing required doc: {doc}")

    print("Repository validation passed.")


if __name__ == "__main__":
    main()
