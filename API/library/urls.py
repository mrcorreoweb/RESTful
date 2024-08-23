"""Set up the url routes for the library application."""

from django.urls import path
from . import views

urlpatterns = [
    path("writers/", views.writer_list, name="writer_list"),
    path("writers/<int:writer_id>/", views.writer_detail, name="writer_detail"),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
]
