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
- Django Rest Framework - Class Based Views with ModelViewSets (DRF-CBVs-ModelViewSets branch)
"""

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Writer
from .serializers import BookSerializer, WriterSerializer

# Writers Endpoints
class WriterViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting Writers.
    """

    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    
# Books Endpoints
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting Books.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def create(self, request, *args, **kwargs):
        """Custom creation logic to handle writer by name"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Use custom create method from BookSerializer to handle writer by name
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """Custom update logic to handle writer by name"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            # Use custom update method from BookSerializer to handle writer by name
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)