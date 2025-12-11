from django.urls import path, include, re_path
from main.views import *

prodact_urlpatterns = [
    path("", products),
    path("new/", new),
    path("top/", top),
]

urlpatterns = [
    path("", index, kwargs={'a' : 1}, name="home"),
    path("user/<str:name>/<int:age>/", user, name="user_info"),
    path("user/<str:name>/", user, name="user_info"),
    path("prodacts/", include(prodact_urlpatterns)),
    re_path(r"^about/", about),
    re_path(r"^calc/(?P<number1>\d{2})/(?P<number2>\d{2})$", calc),
    re_path(r"^user1/(?P<name>\D+)/(?P<age>\d+)", user1),
    re_path(r"^user1/(?P<name>\D+)/", user1),
    re_path(r"^user1/", user1),
               ]

