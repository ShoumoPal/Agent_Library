from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/search/', views.get_books, name='get_books'),
    path('books/summary/', views.stream_book_summary_view, name='get_summary'),
]