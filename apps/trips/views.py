from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_POST


def index(request: HttpRequest) -> HttpResponse:
    """Feature 1 slice landing page (Trips & Utilization)."""
    return render(request, "trips/index.html")


@require_POST
def ping(request: HttpRequest) -> HttpResponse:
    """HTMX CSRF smoke endpoint confirming slice partial updates work."""
    return render(
        request,
        "trips/partials/status_card.html",
        {"checked_at": timezone.localtime().strftime("%H:%M:%S")},
    )
