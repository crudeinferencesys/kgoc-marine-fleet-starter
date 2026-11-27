from django.test import TestCase
from django.urls import reverse


class TripsSliceSmokeTests(TestCase):
    def test_index_returns_200(self):
        response = self.client.get(reverse("trips:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Trips &amp; Utilization")

    def test_htmx_ping_post_returns_200(self):
        response = self.client.post(reverse("trips:ping"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "HTMX POST + CSRF verified")
