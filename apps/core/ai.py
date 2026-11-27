"""
Shared Gemini AI service for the in-app Bonus AI feature.

Uses the official `google-genai` SDK with Pydantic structured output and graceful
timeout/error handling so missing API keys or transient failures never crash judging.
"""

from __future__ import annotations

import logging
from typing import TypeVar

from django.conf import settings
from google import genai
from google.genai import types
from pydantic import BaseModel

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class DispatchBriefing(BaseModel):
    """Reference structured-output contract for the Theme 4 AI Dispatch Co-Pilot."""

    executive_summary: str
    recommended_actions: list[str]
    safety_flags: list[str]
    estimated_impact_note: str


def is_ai_configured() -> bool:
    """Return True when a Gemini API key is configured in Django settings."""
    return bool(getattr(settings, "GEMINI_API_KEY", "").strip())


def generate_structured(
    prompt: str,
    response_schema: type[T],
    system_instruction: str = "",
    timeout_seconds: float = 20.0,
) -> tuple[T | None, str | None]:
    """
    Call Gemini with structured JSON output validated into `response_schema`.

    Returns `(parsed_model, None)` on success or `(None, human_readable_error)` on
    missing configuration, timeout, or API error.
    """
    api_key = getattr(settings, "GEMINI_API_KEY", "").strip()
    if not api_key:
        return None, "GEMINI_API_KEY is not configured; using deterministic fallback."

    model_name = getattr(settings, "GEMINI_MODEL", "gemini-2.5-flash").strip() or "gemini-2.5-flash"
    timeout_ms = max(1000, int(timeout_seconds * 1000))

    try:
        client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=timeout_ms),
        )
        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=response_schema,
            system_instruction=system_instruction or None,
            temperature=0.2,
        )
        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=config,
        )
        if getattr(response, "parsed", None) is not None:
            return response.parsed, None
        raw_text = (getattr(response, "text", "") or "").strip()
        if not raw_text:
            return None, "Gemini returned an empty response."
        return response_schema.model_validate_json(raw_text), None
    except Exception as exc:
        logger.warning("Gemini structured generation failed: %s", exc)
        return None, f"Gemini request failed: {exc.__class__.__name__}"
