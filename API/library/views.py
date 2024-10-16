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
- Django Rest Framework - DRF + Generic Class-Based Views (DRF-GenericCBVs)
- Implements the API using DRF's generic class-based views, 
providing a more concise and reusable structure for common patterns.
"""

from rest_framework import generics
from .models import Book, Writer
from .serializers import BookSerializer, WriterSerializer

# Writers Endpoints
class WriterListCreateView(generics.ListCreateAPIView):
    """
    GET, /writers/, return a list of all writers in the library.        
    POST, /writers/, create a new writer in the library
    """    
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class WriterRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET, /writers/<writer_id>/, return the details of a specific writer    
    PUT, /writers/<writer_id>/, update the details of a specific writer
    DELETE, /writers/<writer_id>/, delete a specific writer from the library
    """
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    lookup_field = 'id'
            
# Books Endpoints
class BookListCreateView(generics.ListCreateAPIView):
    """
    GET, /books/, return a list of all books in the library.        
    POST, /books/, create a new book in the library.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET, /books/<book_id>/, return the details of a specific book    
    PUT, /books/<book_id>/, update the details of a specific book
    DELETE, /books/<book_id>/, delete a specific book from the library
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
