from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.http import require_POST


def index(request: HttpRequest) -> HttpResponse:
    """Feature 2 slice landing page (Dispatch Optimizer + Bonus AI Co-Pilot)."""
    return render(request, "optimizer/index.html")


@require_POST
def ping(request: HttpRequest) -> HttpResponse:
    """HTMX CSRF smoke endpoint confirming slice partial updates work."""
    return render(
        request,
        "optimizer/partials/status_card.html",
        {"checked_at": timezone.localtime().strftime("%H:%M:%S")},
    )
