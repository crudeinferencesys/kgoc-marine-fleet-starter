from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("trips/", include("apps.trips.urls")),
    path("optimizer/", include("apps.optimizer.urls")),
    path("safety/", include("apps.safety.urls")),
]
