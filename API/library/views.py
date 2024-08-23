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

import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_http_methods
from .models import Book, Writer


# Writers Endpoints
@require_http_methods(["GET", "POST"])
@csrf_exempt
def writer_list(request):
    """
    GET, /writers, return a list of all writers in the library.
    POST, /writers, create a new writer in the library.
    """
    if request.method == "GET":
        writers = Writer.objects.all()
        writer_data = [{"ID": writer.pk, "name": writer.name} for writer in writers]
        return JsonResponse(writer_data, safe=False)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)
        try:
            name = data.get("name")
            writer = Writer(name=name)
            writer.save()
            writer_data = {"ID": writer.pk, "name": writer.name}
            return JsonResponse(writer_data, status=201)
        except KeyError:
            return HttpResponse(status=400)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def writer_detail(request, writer_id):
    """
    GET, /writers/<writer_id>/, return the details of a specific writer
    PUT, /writers/<writer_id>/, update the details of a specific writer
    DELETE, /writers/<writer_id>/, delete a specific writer from the library
    """
    try:
        writer = Writer.objects.get(pk=writer_id)
    except ObjectDoesNotExist:
        return HttpResponse(
            f"Writer ID {writer_id} empty. Check another ID.", status=404
        )

    if request.method == "GET":
        writer_data = {"ID": writer.pk, "name": writer.name}
        return JsonResponse(writer_data)

    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)
        try:
            name = data.get("name")
            writer.name = name
            writer.save()
            writer_data = {"ID": writer.pk, "name": writer.name}
            return JsonResponse(writer_data)
        except KeyError:
            return HttpResponse(status=400)

    elif request.method == "DELETE":
        writer.delete()
        return HttpResponse(status=204)


# Books Endpoints
@require_http_methods(["GET", "POST"])
@csrf_exempt
def book_list(request):
    """
    GET, /books, return a list of all books in the library.
    POST, /books, create a new book in the library.
    """
    if request.method == "GET":
        books = Book.objects.all()
        book_data = [
            {"ID": book.pk, "title": book.title, "writer": book.writer.name}
            for book in books
        ]
        return JsonResponse(book_data, safe=False)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)
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
            return HttpResponse(
                "Writer not found: check the spelling or create a new one", status=400
            )
        except KeyError:
            return HttpResponse(status=400)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def book_detail(request, book_id):
    """
    GET, /books/<book_id>/, return the details of a specific book
    PUT, /books/<book_id>/, update the details of a specific book
    DELETE, /books/<book_id>/, delete a specific book from the library
    """
    try:
        book = Book.objects.get(pk=book_id)
    except ObjectDoesNotExist:
        return HttpResponse(f"Book ID {book_id} empty. Check another ID.", status=404)

    if request.method == "GET":
        book_data = {"ID": book.pk, "title": book.title, "writer": book.writer.name}
        return JsonResponse(book_data)

    elif request.method == "PUT":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)
        try:
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
        except Writer.DoesNotExist:
            return HttpResponse(
                "Writer not found: check the spelling or create a new one", status=400
            )        
        except KeyError:
            return HttpResponse(status=400)

    elif request.method == "DELETE":
        book.delete()
        return HttpResponse(status=204)
