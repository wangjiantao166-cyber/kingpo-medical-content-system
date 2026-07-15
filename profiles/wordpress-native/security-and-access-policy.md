# WordPress Security and Access Policy

- Use dedicated deploy users.
- SSH root login is prohibited.
- Secrets belong in GitHub Environments or Secrets, not Git.
- Production deploys require database and uploads backup.
- WP-CLI writes must support dry-run when practical.
- Direct production SQL writes are prohibited.
- Production publishing requires human approval.
