from django.urls import path

from . import views

app_name = "optimizer"

urlpatterns = [
    path("", views.index, name="index"),
    path("ping/", views.ping, name="ping"),
]
