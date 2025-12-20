from django.urls import path
from main.views import *


urlpatterns = [
    path("login/", login),
    path("math/", math),
    path("register/", register),
    path("programmer-day/", programmer_day),
]