# WordPress State Machine

```text
source_pending
draft
technical_review
standards_review
seo_review
ready_for_publish
publish
retired
blocked
```

Codex may create drafts and submit to review. Codex must not directly change a post to `publish` in production.
