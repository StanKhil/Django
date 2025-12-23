from django.urls import path, include
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("contact/", get_contacts, name="contact"),
    path("prime-numbers/", prime_numbers, name="prime_numbers"),
    path("contactcbv/", ContactFormView.as_view(), name="contactcbv"),
    path("water/", WaterFormView.as_view(), name="water"),
    path("contact1/", get_contact1, name="contact1"),
    path("feedback/", get_feedback, name="feedback"),
    path("film/", add_film, name="film"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)