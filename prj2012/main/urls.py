from django.urls import path, include
from main.views import *

urlpatterns = [
    path("contact/", get_contacts, name="contact"),
    path("prime-numbers/", prime_numbers, name="prime_numbers"),
    path("contactcbv/", ContactFormView.as_view(), name="contactcbv"),
    path("water/", WaterFormView.as_view(), name="water"),
]