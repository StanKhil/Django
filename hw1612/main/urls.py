from django.urls import path
from main.views import *

urlpatterns = [
    path("", song),
    path("fr/", song, {"lang": "fr"}),
    path("de/", song, {"lang": "de"}),
    path("es/", song, {"lang": "es"}),

    path("cars/", cars),
    path("cars/toyota/", cars, {"brand": "toyota"}),
    path("cars/honda/", cars, {"brand": "honda"}),
    path("cars/renault/", cars, {"brand": "renault"}),

    path("day/", day_of_week),
    path("headphones/", headphones),
]
