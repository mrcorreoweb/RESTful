"""Implement the views to return JSON responses and perform CRUD operations
for the following API endpoints (method, URL, description):
For writers:
- GET, /writers, return a list of all writers in the library
- POST, /writers, create a new writer in the library
- GET, /writers/<writer_id>/, return the details of a specific writer
- PUT, /writers/<writer_id>/, update the details of a specific writer
- DELETE, /writers/<writer_id>/, delete a specific writer from the library
For books:
- GET, /books, return a list of all books in the library
- POST, /books, create a new book in the library.
- GET, /books/<book_id>/, return the details of a specific book
- PUT, /books/<book_id>/, update the details of a specific book.
- DELETE, /books/<book_id>/, delete a specific book from the library.

Method of implementation: 
- Function Based Views (FBVs)
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import Book, Writer
from .serializers import BookSerializer, WriterSerializer   


# Writers Endpoints
@api_view(['GET', 'POST'])
def writer_list(request):
    """
    GET, /writers, return a list of all writers in the library.
    POST, /writers, create a new writer in the library.
    """
    if request.method == "GET":
        writers = Writer.objects.all()
        serializer = WriterSerializer(writers, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = WriterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def writer_detail(request, writer_id):
    """
    GET, /writers/<writer_id>/, return the details of a specific writer
    PUT, /writers/<writer_id>/, update the details of a specific writer
    DELETE, /writers/<writer_id>/, delete a specific writer from the library
    """
    try:
        writer = Writer.objects.get(pk=writer_id)
    except Writer.DoesNotExist:
        return Response(
            f"Writer ID {writer_id} empty. Check another ID.", 
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        serializer = WriterSerializer(writer)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = WriterSerializer(writer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    elif request.method == "DELETE":
        writer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Books Endpoints
@api_view(["GET", "POST"])
def book_list(request):
    """
    GET, /books, return a list of all books in the library.
    POST, /books, create a new book in the library.
    """
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)    

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)             


@api_view(["GET", "PUT", "DELETE"])
def book_detail(request, book_id):
    """
    GET, /books/<book_id>/, return the details of a specific book
    PUT, /books/<book_id>/, update the details of a specific book
    DELETE, /books/<book_id>/, delete a specific book from the library
    """
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return Response(f"Book ID {book_id} empty. Check another ID.", status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)    

    elif request.method == "PUT":        
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save() # This calls the `update` method in the serializer
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    elif request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
