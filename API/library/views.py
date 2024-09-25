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
- Django Rest Framework - Class Based Views with ViewSets (DRF-CBVs-ViewSets branch)
"""

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Book, Writer
from .serializers import BookSerializer, WriterSerializer
from django.shortcuts import get_object_or_404
 
# Writers Endpoints
class WriterViewSet(viewsets.ViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting Writers.
    """    
    def list(self, request):
        """GET /writers/ - return a list of all writers in the library."""        
        writers = Writer.objects.all()
        serializer = WriterSerializer(writers, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST, /writers/ - create a new writer in the library"""
        serializer = WriterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def retrieve(self, request, pk=None):
        """GET /writers/<writer_id>/ - return the details of a specific writer"""
        writer = get_object_or_404(Writer, pk=pk)
        serializer = WriterSerializer(writer)
        return Response(serializer.data)
        
    def update(self, request, pk=None):        
        """PUT /writers/<writer_id>/ - update the details of a specific writer"""
        writer = get_object_or_404(Writer, pk=pk)
        serializer = WriterSerializer(writer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)        

    def delete(self, request, pk=None):
        """DELETE /writers/<writer_id>/ - delete a specific writer from the library"""
        writer = get_object_or_404(Writer, pk=pk)          
        writer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
# Books Endpoints
class BookViewSet(viewsets.ViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting Books.
    """

    def list(self, request):
        """GET /books/ - List all books"""
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """GET /books/<id>/ - Get a specific book"""
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def create(self, request):
        """POST /books/ - Create a new book"""
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            # Use custom logic to handle writer by name
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """PUT /books/<id>/ - Update an existing book"""
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            # Use custom logic to handle writer by name
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """DELETE /books/<id>/ - Delete a specific book"""
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
