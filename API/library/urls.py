"""Set up the url routes for the library application."""

from django.urls import path
from .views import WriterListCreateView, WriterRetrieveUpdateDeleteView, BookListCreateView, BookRetrieveUpdateDeleteView

urlpatterns = [
    path("writers/", WriterListCreateView.as_view(), name="writer_list"),
    path("writers/<int:id>/", WriterRetrieveUpdateDeleteView.as_view(), name="writer_detail"),
    path("books/", BookListCreateView.as_view(), name="book_list"),
    path("books/<int:id>/", BookRetrieveUpdateDeleteView.as_view(), name="book_detail"),
]
