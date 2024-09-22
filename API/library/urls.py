"""Set up the url routes for the library application."""

from django.urls import path
from .views import WriterListView, WriterDetailView, BookListView, BookDetailView

urlpatterns = [
    path("writers/", WriterListView.as_view(), name="writer_list"),
    path("writers/<int:writer_id>/", WriterDetailView.as_view(), name="writer_detail"),
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/<int:book_id>/", BookDetailView.as_view(), name="book_detail"),
]
