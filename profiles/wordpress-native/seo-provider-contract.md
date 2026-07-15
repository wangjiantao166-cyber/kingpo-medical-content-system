# SEO Provider Contract

```yaml
seo_provider:
  allowed:
    - rank_math
    - yoast
    - kingpo_core
  only_one_active: true
```

Rank Math or Yoast may provide the editing interface and basic sitemap. KingPo core validates business schema, canonical decisions, claim safety, and release blockers.

Canonical, robots, and schema must have one final output source. Do not generate fake price, availability, rating, review, certification, or compliance data.
