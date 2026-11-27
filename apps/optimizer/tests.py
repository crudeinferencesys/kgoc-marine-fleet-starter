from django.test import TestCase
from django.urls import reverse


class OptimizerSliceSmokeTests(TestCase):
    def test_index_returns_200(self):
        response = self.client.get(reverse("optimizer:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dispatch Optimizer")

    def test_htmx_ping_post_returns_200(self):
        response = self.client.post(reverse("optimizer:ping"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "HTMX POST + CSRF verified")
