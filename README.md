# KingPo Content Operating System

KingPo multi-site product master data, WordPress content, SEO, asset, and publishing governance system.

This repository is a working system for building a WordPress-based B2B product knowledge website similar in information architecture depth to mature equipment-industry websites, while keeping KingPo content original, source-based, and safe for technical, standards, medical, and regulatory claims.

It is not limited to medical testing equipment. Medical products are an important vertical, but the system is intended to support KingPo product domains across medical, battery safety, environmental/IP, electrical safety, flammability/material, plug/socket/cable/gauge, automotive/EV, and custom automation categories.

The repository currently contains:

- System scope, site targeting, and source ownership policy
- WordPress content system blueprint
- Product, standard, application, resource, asset, claim, and inquiry field models
- JSON schemas for source, product, specification, claim, standard mapping, assets, agent handoff, and release gates
- Internal linking and SEO architecture
- Google SEO, E-E-A-T, customer-first content, and Search Content Trust Signal rules
- AI-assisted English product page generation workflow
- Agent/skill workflows for product data governance, standards review, content drafting, technical SEO, WordPress implementation, visual assets, QA, and data import/export

This repository does not directly modify a production website. All implementation should start in a staging WordPress environment.

## Platform Decision

This repository is not a single website and is not a deployable finished site by itself. It is KingPo's company-level B2B content operating system:

- content governance layer
- product and standards data contracts
- agent operation rules
- WordPress base platform
- SEO and claim-safety rules
- publishing, deployment, backup, and operations control plane

Current default implementation platform:

```yaml
platform: wordpress
frontend: native-wordpress-block-theme
headless: false
nextjs: disabled_by_default
content_database: wordpress-mysql
code_source_of_truth: github
published_content_source_of_truth: wordpress
operations_interface: wp-cli
```

Vertical sites inherit this repository through WordPress profiles, plugin/theme releases, schemas, and agent contracts. Next.js is not the default platform.
