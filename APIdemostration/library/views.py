"""Implement the views to return JSON responses for the following API endpoints:

1. /books: Retrieve a list of all books in the library.
2. /authors: Retrieve a list of all authors in the library."""

from django.http import JsonResponse
from .models import Book, Writer


def book_list(request): #pylint:disable=unused-argument
    """Return a list of all books in the library."""

    books = Book.objects.all() #pylint:disable=no-member
    book_data = [
        {
            "title": book.title,            
            "author": book.writer.name,
        }
        for book in books
    ]
    return JsonResponse(book_data, safe=False)


def author_list(request): #pylint:disable=unused-argument
    """Return a list of all authors in the library."""

    authors = Writer.objects.all() #pylint:disable=no-member
    author_data = [
        {"name": author.name}
        for author in authors
    ]
    return JsonResponse(author_data, safe=False)
