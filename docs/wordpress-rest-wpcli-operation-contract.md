# WordPress REST and WP-CLI Operation Contract

WP-CLI is the primary automation interface. REST API use is restricted to explicitly approved operations.

All write operations must:

- support dry-run when practical;
- output JSON reports;
- record operator, timestamp, and affected objects;
- be idempotent or document why not;
- return non-zero exit codes on failure.

Production write operations require release gate approval and human approval.
