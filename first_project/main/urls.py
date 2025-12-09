from django.urls import path, include
from main.views import *

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
    path("task3", task3, name="task3"),
    path("task4", task4, name="task4"),
    path("task5", task5, name="task5"),
]