from django.urls import path, include
from main2.views import *

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
]