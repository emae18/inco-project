from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reservas", views.reservas, name="reservas"),
    path("servicios", views.filterRules, name="test")
]