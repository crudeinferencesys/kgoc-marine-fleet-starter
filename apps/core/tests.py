from django.test import TestCase, override_settings
from django.urls import reverse

from apps.core.ai import DispatchBriefing, generate_structured


class CoreSmokeTests(TestCase):
    def test_home_renders_with_global_htmx_csrf_header(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "X-CSRFToken")
        self.assertContains(response, "KGOC Marine Fleet")

    def test_healthz_reports_ok_and_database(self):
        response = self.client.get(reverse("core:healthz"))
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["database"], "sqlite3")
        self.assertIn("ai_configured", payload)

    @override_settings(GEMINI_API_KEY="")
    def test_generate_structured_handles_missing_api_key_gracefully(self):
        result, error = generate_structured(
            prompt="Summarize vessel utilization.",
            response_schema=DispatchBriefing,
        )
        self.assertIsNone(result)
        self.assertIsNotNone(error)
        self.assertIn("GEMINI_API_KEY", error)
