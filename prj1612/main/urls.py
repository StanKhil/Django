from django.urls import path
from main.views import *

urlpatterns = [
    path('', index, name = "index"),
    path('index1/', index1, name = "index1"),
    path('index2/', index2, name = "index2"),
    path('index3/', index3, name = "index3"),
    path('index4/', index4, name = "index4"),
    path('index5/', index5, name = "index5"),
]