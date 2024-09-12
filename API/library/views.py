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

from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.urls import reverse_lazy
from .models import Book, Writer
import json
 
def parse_json(request):
    """
    Parse JSON request body and return the parsed data and error response if JSON parsing fails.
    :param request: The HTTP request object
    :return: tuple (parsed_data, error_response) - parsed_data if successful, error_response if failed
    """
    try:
        return json.loads(request.body), None
    except json.JSONDecodeError:
        return None, HttpResponse(status=400)

def validate_id_is_integer(id_value, id_name="ID"):
    """
    Utility function to validate that a given ID is an integer.
    :param id_value: The ID value to validate
    :param id_name: The name of the ID (e.g., "Writer ID") for error messages
    :return: tuple (validated_id, error_response) - validated_id if successful, error_response if failed
    """
    try:
        validated_id = int(id_value)
        return validated_id, None
    except ValueError:
        error_response = JsonResponse({"error": f"{id_name} must be an integer."}, status=400)
        return None, error_response

# Writers Endpoints

@method_decorator (csrf_exempt, name='dispatch')
class WriterListView(View):
    def get(self, request):
        """
        GET, /writers/, return a list of all writers in the library.        
        """    
        writers = Writer.objects.all()
        writer_data = [{"ID": writer.pk, "name": writer.name} for writer in writers]
        return JsonResponse(writer_data, safe=False)

    def post(self, request):
        """
        POST, /writers/, create a new writer in the library
        """
        data, error_response = parse_json(request)
        if error_response:
            return error_response
        
        try:
            name = data.get("name")
            writer = Writer(name=name)
            writer.save()
            writer_data = {"ID": writer.pk, "name": writer.name}
            return JsonResponse(writer_data, status=201)
        except KeyError:
            # raise an error if the key is not present in the dictionary            
            return HttpResponse(status=400)


@method_decorator(csrf_exempt, name='dispatch')
class WriterDetailView(View):
    def get(self, request, writer_id, *args, **kwargs):
        """
        GET, /writers/<writer_id>/, return the details of a specific writer    
        """
        # Validate the writer_id is an integer
        writer_id, error_response = validate_id_is_integer(writer_id, "Writer ID")
        # print in a new line writer_is and error_response        
        print ("writer id:", writer_id, "& error response:", error_response)
        if error_response:
            return error_response        

        try:
            writer = Writer.objects.get(pk=writer_id)
            writer_data = {"ID": writer.pk, "name": writer.name}
            return JsonResponse(writer_data)
        except ObjectDoesNotExist:
            return HttpResponse(
                f"Writer ID {writer_id} empty. Check another ID.", status=404
            )

    def put(self, request, writer_id):
        """
        PUT, /writers/<writer_id>/, update the details of a specific writer
        """    
        writer_id, error_response = validate_id_is_integer(writer_id, "Writer ID")
        if error_response:
            return error_response
        
        
        
        data, error_response = parse_json(request)
        

        if error_response:
            return error_response       
        
        try:
            writer = Writer.objects.get(pk=writer_id)
            name = data.get("name")
            writer.name = name
            writer.save()
            writer_data = {"ID": writer.pk, "name": writer.name}
            return JsonResponse(writer_data)
        except ObjectDoesNotExist:
            return HttpResponse(f"Writer ID {writer_id} empty. Check another ID.", status=404)
        except KeyError:
            return HttpResponse(status=400)

    def delete(self, request, writer_id):
        """
        DELETE, /writers/<writer_id>/, delete a specific writer from the library
        """
        writer_id, error_response = validate_id_is_integer(writer_id, "Writer ID")
        if error_response:
            return error_response
        
        try:
            writer = Writer.objects.get(pk=writer_id)        
            writer.delete()
            return HttpResponse(status=204)
        except ObjectDoesNotExist:
            return HttpResponse(f"Writer ID {writer_id} empty. Check another ID.", status=404)

# Books Endpoints
@method_decorator(csrf_exempt, name='dispatch')
class BookListView(View):
    def get(self, request):
        """
        GET, /books, return a list of all books in the library.
        """
        books = Book.objects.all()
        book_data = [{"ID": book.pk, "title": book.title, "writer": book.writer.name} for book in books]
        return JsonResponse(book_data, safe=False)

    def post(self, request):
        """
        POST, /books, create a new book in the library.
        """
        data, error_response = parse_json(request)
        if error_response:
            return error_response

        try:
            title = data.get("title")
            writer_name = data.get("writer")

            # Fetch the Writer instance by name
            writer = Writer.objects.get(name=writer_name)

            # Create the Book instance with the fetched Writer instance
            book = Book(title=title, writer=writer)
            book.save()

            book_data = {"ID": book.pk, "title": book.title, "writer": book.writer.name}
            return JsonResponse(book_data, status=201)
        except Writer.DoesNotExist:
            return HttpResponse("Writer not found: check the spelling or create a new one", status=400)
        except KeyError:
            return HttpResponse(status=400)

@method_decorator(csrf_exempt, name='dispatch')
class BookDetailView(View):
    def get(self, request, book_id):
        """
        GET, /books/<book_id>/, return the details of a specific book.
        """
        book_id, error_response = validate_id_is_integer(book_id, "Book ID")
        if error_response:
            return error_response
        

        try:
            book = Book.objects.get(pk=book_id)
            book_data = {"ID": book.pk, "title": book.title, "writer": book.writer.name}
            return JsonResponse(book_data)
        except ObjectDoesNotExist:
            return HttpResponse(f"Book ID {book_id} empty. Check another ID.", status=404)

    def put(self, request, book_id):
        """
        PUT, /books/<book_id>/, update the details of a specific book.
        """
        book_id, error_response = validate_id_is_integer(book_id, "Book ID")
        if error_response:
            return error_response
        
        data, error_response = parse_json(request)
        if error_response:
            return error_response
        
        try:
            book = Book.objects.get(pk=book_id)
            title = data.get("title")
            writer_name = data.get("writer")

            # Fetch the Writer instance by name
            writer = Writer.objects.get(name=writer_name)
            # Update the Book instance with the fetched Writer instance and title
            book.title = title
            book.writer = writer
            book.save()
            book_data = {"ID": book.pk, "title": book.title, "writer": book.writer.name}
            return JsonResponse(book_data)
        except Book.DoesNotExist:
            return HttpResponse(f"Book ID {book_id} empty. Check another ID.", status=404)
        except Writer.DoesNotExist:
            return HttpResponse("Writer not found: check the spelling or create a new one", status=400)
        except KeyError:
            return HttpResponse(status=400)

    def delete(self, request, book_id):
        """
        DELETE, /books/<book_id>/, delete a specific book from the library.
        """
        book_id, error_response = validate_id_is_integer(book_id, "Book ID")
        if error_response:
            return error_response
        
        try:
            book = Book.objects.get(pk=book_id)
            book.delete()
            return HttpResponse(status=204)
        except ObjectDoesNotExist:
            return HttpResponse(f"Book ID {book_id} empty. Check another ID.", status=404)
