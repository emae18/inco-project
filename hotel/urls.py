from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reservas", views.reservas, name="reservas"),
    path("search", views.filterRules, name="test"),
    path("habitaciones", views.GetHabitaciones, name="test"),
    path("tipos", views.GetTiposHab, name="test")
]