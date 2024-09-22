"""Implement the views to return JSON responses and perform CRUD operations
for the following API endpoints (method, URL, description):
For writers:
- GET, /writers/, return a list of all writers in the library
- POST, /writers/, create a new writer in the library
- GET, /writers/<writer_id>/, return the details of a specific writer
- PUT, /writers/<writer_id>/, update the details of a specific writer
- DELETE, /writers/<writer_id>/, delete a specific writer from the library
For books:
- GET, /books/, return a list of all books in the library
- POST, /books/, create a new book in the library.
- GET, /books/<book_id>/, return the details of a specific book
- PUT, /books/<book_id>/, update the details of a specific book.
- DELETE, /books/<book_id>/, delete a specific book from the library.

Method of implementation: 
- Class Based Views (CBVs)
"""

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Book, Writer
from .serializers import BookSerializer, WriterSerializer
from django.http import Http404
 
# Writers Endpoints
class WriterListView(APIView):
    """
    GET, /writers/, return a list of all writers in the library.        
    POST, /writers/, create a new writer in the library
    """    
    def get(self, request):
        writers = Writer.objects.all()
        serializer = WriterSerializer(writers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WriterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WriterDetailView(APIView):
    """
    GET, /writers/<writer_id>/, return the details of a specific writer    
    PUT, /writers/<writer_id>/, update the details of a specific writer
    DELETE, /writers/<writer_id>/, delete a specific writer from the library
    """
    def get_object(self, writer_id):
        try:
            return Writer.objects.get(pk=writer_id)
        except Writer.DoesNotExist:
            raise Http404
            
    def get(self, request, writer_id):
        writer = self.get_object(writer_id)
        serializer = WriterSerializer(writer)
        return Response(serializer.data)
        
    def put(self, request, writer_id):        
        writer = self.get_object(writer_id)
        serializer = WriterSerializer(writer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)        

    def delete(self, request, writer_id):
        writer = self.get_object(writer_id)                
        writer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
# Books Endpoints
class BookListView(APIView):
    """
    GET, /books/, return a list of all books in the library.
    POST, /books/, create a new book in the library.
    """
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    """
    GET, /books/<book_id>/, return the details of a specific book.
    PUT, /books/<book_id>/, update the details of a specific book.
    DELETE, /books/<book_id>/, delete a specific book from the library.
    """
    def get_object(self, book_id):
        try:
            return Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, book_id):
        book = self.get_object(book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, book_id):
        book = self.get_object(book_id)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        book = self.get_object(book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
