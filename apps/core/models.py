"""
FROZEN SHARED SCHEMA FILE.

Do NOT add domain tables here until the organizer dataset is inspected at 11:00 AM
via `python manage.py inspect_dataset <path>` and the team agrees on the frozen schema.
Do NOT use PostgreSQL-only ORM fields (ArrayField, HStoreField, etc.) so local SQLite
remains 100% compatible with Cloud SQL PostgreSQL.
"""

from django.db import models


class TimestampedModel(models.Model):
    """Abstract base class providing creation and update timestamps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
