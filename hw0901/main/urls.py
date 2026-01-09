from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', restaurant_list, name='restaurant_list'),
    path('add/', restaurant_form, name='restaurant_add'),
    path('edit/<int:pk>/', restaurant_form, name='restaurant_edit'),
    path('delete/<int:pk>/', restaurant_delete, name='restaurant_delete'),
]
