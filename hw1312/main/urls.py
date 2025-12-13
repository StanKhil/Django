from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("history/", views.history, name="history"),
    path("history/<int:year>/", views.history),
    path("cities/", views.cities, name="cities"),
    path("cities/<str:city>/", views.cities),
    path("cities/<str:city>/<int:year>/", views.cities),
    path("facts/", views.facts, name="facts"),
]
