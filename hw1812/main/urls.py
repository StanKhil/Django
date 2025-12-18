from django.urls import path
from main.views import *


urlpatterns = [
path('books/', books_list, name='books_list'),
path('books/<int:pk>/', book_details, name='book_details'),
path('readers/', readers_list, name='readers_list'),
path('readers/<int:pk>/', reader_details, name='reader_details'),
]