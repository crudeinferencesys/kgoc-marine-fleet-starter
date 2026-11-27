## Summary
- Feature slice touched (`trips` / `optimizer` / `safety` / `core` / `docs`):
- What changed:

## Guardrail Checklist
- [ ] Created from latest `origin/main` on a `feat/*` branch (NOT direct to `main`)
- [ ] No unintended edits to frozen shared files (`apps/core/models.py`, `config/settings.py`, `config/urls.py`, `templates/base.html`, `requirements.txt`, `Dockerfile`, `entrypoint.sh`)
- [ ] Passed `python manage.py check && python manage.py makemigrations --check --dry-run && python manage.py test`
- [ ] No login wall added; judging routes remain public
- [ ] No `.env`, API keys, service-account JSON, or `db.sqlite3` committed
