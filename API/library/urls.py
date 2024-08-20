"""Set up the url routes for the library application."""

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('writers/', views.writer_list, name='writer_list'),
]
