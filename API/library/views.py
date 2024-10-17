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
- Django Rest Framework - DRF + Mixins (DRF-Mixins)
- implements the API using DRF's mixins for common actions
like list, create, retrieve, update, and destroy.
"""

from rest_framework import generics, mixins
from .models import Book, Writer
from .serializers import BookSerializer, WriterSerializer

# Writers Endpoints
class WriterListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    GET, /writers/, return a list of all writers in the library.        
    POST, /writers/, create a new writer in the library
    """    
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class WriterRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
    GET, /writers/<writer_id>/, return the details of a specific writer    
    PUT, /writers/<writer_id>/, update the details of a specific writer
    DELETE, /writers/<writer_id>/, delete a specific writer from the library
    """
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
            
# Books Endpoints
class BookListCreateView(generics.ListCreateAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    GET, /books/, return a list of all books in the library.        
    POST, /books/, create a new book in the library.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """
    GET, /books/<book_id>/, return the details of a specific book    
    PUT, /books/<book_id>/, update the details of a specific book
    DELETE, /books/<book_id>/, delete a specific book from the library
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)