from django.test import TestCase
from django.urls import reverse


class SafetySliceSmokeTests(TestCase):
    def test_index_returns_200(self):
        response = self.client.get(reverse("safety:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Safety &amp; Fuel")

    def test_htmx_ping_post_returns_200(self):
        response = self.client.post(reverse("safety:ping"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "HTMX POST + CSRF verified")
