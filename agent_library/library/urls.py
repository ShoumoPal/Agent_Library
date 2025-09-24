from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/search/', views.get_books, name='get_books'),
]