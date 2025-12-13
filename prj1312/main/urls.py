from django.urls import path, include
from main.views import *

urlpatterns = [
    path("", index, name="home"),
    path("person/", person, name="person"),
    path("articles/<int:year>/", articles, name="articles"),
    path("request_info/", request_info, name="request_info"),
    path("response_info/", response_info, name="response_info"),
    path("user/", user),
    path("bad/", bad),
    path("about/", about),
    path("simple/", SimpleView.as_view()),
]