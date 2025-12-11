from django.urls import path, include, re_path
from main.views import *

urlpatterns = [
   path("", index, name="home"),
   re_path(r"^about/", about, name="about"),
   re_path(r"^news/", news, name="news"),
   re_path(r"^management/", management, name="management"),
   re_path(r"^contacts/", contacts, name="contacts"),
   path("branches/", branches, name="branches"),
   path("branches/<str:city>/", branches_city, name="branches_city")
   
               ]