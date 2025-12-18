from django.urls import path, include
from main.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('contacts/', contacts, name="contacts"),
    path('sitemap/', sitemap, name="sitemap"),
    path('', TemplateView.as_view(template_name="base.html"), name="base"),
    path("song/", song, name="song"),
    path("fr/", song, {"lang": "fr"}, name="fr"),
    path("de/", song, {"lang": "de"}, name="de"),
    path("es/", song, {"lang": "es"}, name="es"),
]
