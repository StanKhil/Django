from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', books_list, name='home'),
    path('books/', books_list, name='books_list'),
    path('books/create/', book_create, name='book_create'),
    path('books/<int:pk>/', book_details, name='book_details'),
    path('books/<int:pk>/edit/', book_update, name='book_update'),
    path('books/<int:pk>/delete/', book_delete, name='book_delete'),

    path('readers/', readers_list, name='readers_list'),
    path('readers/create/', reader_create, name='reader_create'),
    path('readers/<int:pk>/', reader_details, name='reader_details'),
    path('readers/<int:pk>/edit/', reader_update, name='reader_update'),
    path('readers/<int:pk>/delete/', reader_delete, name='reader_delete'),

    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)