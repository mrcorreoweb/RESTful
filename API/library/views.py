"""Implement the views to return JSON responses for the following API endpoints:

1. /books: Retrieve a list of all books in the library.
2. /writers: Retrieve a list of all authors in the library."""

from django.http import JsonResponse
from .models import Book, Writer


def book_list(request): #pylint:disable=unused-argument
    """Return a list of all books in the library."""

    books = Book.objects.all() #pylint:disable=no-member
    book_data = [
        {
            "title": book.title,            
            "writer": book.writer.name,
        }
        for book in books
    ]
    return JsonResponse(book_data, safe=False)


def writer_list(request): #pylint:disable=unused-argument
    """Return a list of all writers in the library."""

    writers = Writer.objects.all() #pylint:disable=no-member
    writer_data = [
        {"name": writer.name}
        for writer in writers
    ]
    return JsonResponse(writer_data, safe=False)
