# cSpell:disable

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Writer, Book

class WriterViewSetTests(APITestCase):
    
    def setUp(self):
        """Set up initial data for testing."""
        self.writer = Writer.objects.create(name="Carmen Posadas") # Create a writer
        self.writer2 = Writer.objects.create(name="Luis García Rey") # Create another writer
    
    def test_get_all_writers(self):
        """Test GET /writers/ to fetch all writers."""
        url = reverse('writer-list')  # The name of the URL pattern for the writer list
        response = self.client.get(url) # Make a GET request to the URL
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Check if the request was successful
        self.assertEqual(len(response.data), 2)  # Check if we get two writers
        # Check that the 'url' field exists in the response
        self.assertIn('url', response.data[0])

    def test_get_single_writer(self):
        """Test GET /writers/<writer_id>/ to fetch a single writer."""
        url = reverse('writer-detail', args=[self.writer.id])
        response = self.client.get(url) # Make a GET request to the URL
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Check if the request was successful
        self.assertEqual(response.data['name'], "Carmen Posadas")  # Check if we get the correct writer
        # Check that the 'url' field exists in the response
        self.assertIn('url', response.data)

    def test_create_writer(self):
        """Test POST /writers/ to create a new writer."""
        url = reverse('writer-list')  # The name of the URL pattern for the writer list
        data = {'name': 'Robert Menasse'}  # Data to send in the request body
        response = self.client.post(url, data, format='json') # Make a POST request to the URL
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # Check if the request was successful
        self.assertEqual(response.data['name'], 'Robert Menasse')  # Check if we get the correct writer
        # Check that the 'url' field exists in the response
        self.assertIn('url', response.data)

    def test_update_writer(self):
        """Test PUT /writers/<writer_id>/ to update an existing writer."""
        url = reverse('writer-detail', args=[self.writer.id])  # The name of the URL pattern for the writer detail
        data = {'name': 'Updated Name'} # Data to send in the request body
        response = self.client.put(url, data, format='json') # Make a PUT request to the URL
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Check if the request was successful
        self.assertEqual(response.data['name'], 'Updated Name') # Check if we get the correct writer
        # Check that the 'url' field exists in the response
        self.assertIn('url', response.data)

    def test_delete_writer(self):
        """Test DELETE /writers/<writer_id>/ to delete a writer."""
        url = reverse('writer-detail', args=[self.writer.id])  # The name of the URL pattern for the writer detail
        response = self.client.delete(url) # Make a DELETE request to the URL
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) # Check if the request was successful
        # Verify writer has been deleted
        self.assertFalse(Writer.objects.filter(pk=self.writer.id).exists())


class BookViewSetTests(APITestCase):

    def setUp(self):
        """Set up initial data for testing."""
        self.writer = Writer.objects.create(name="Carmen Posadas")
        self.book = Book.objects.create(title="La leyenda de la peregrina", writer=self.writer)

    def test_get_all_books(self):
        """Test GET /books/ to fetch all books."""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        # Check that the 'url' and 'writer' (hyperlinked) fields exist in the response
        self.assertIn('url', response.data[0])
        self.assertIn('writer', response.data[0])
        self.assertIn('writer_name', response.data[0])
        self.assertEqual(response.data[0]['writer_name'], "Carmen Posadas")

    def test_get_single_book(self):
        """Test GET /books/<book_id>/ to fetch a single book."""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "La leyenda de la peregrina")
        # Check that the 'url' and 'writer' (hyperlinked) fields exist in the response
        self.assertIn('url', response.data)
        self.assertIn('writer', response.data)
        self.assertIn('writer_name', response.data)
        self.assertEqual(response.data['writer_name'], "Carmen Posadas")

    def test_create_book(self):
        """Test POST /books/ to create a new book."""
        url = reverse('book-list')
        # Use the hyperlinked writer URL for creating a book
        writer_url = reverse('writer-detail', args=[self.writer.id])
        data = {
            'title': 'The Capital',
            'writer': writer_url  # Pass the URL of the writer instead of the name
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'The Capital')
        # Check that the 'url' and 'writer' (hyperlinked) fields exist in the response
        self.assertIn('url', response.data)
        self.assertIn('writer', response.data)
        self.assertIn('writer_name', response.data)
        self.assertEqual(response.data['writer_name'], "Carmen Posadas")

    def test_update_book(self):
        """Test PUT /books/<book_id>/ to update an existing book."""
        url = reverse('book-detail', args=[self.book.id])
        writer_url = reverse('writer-detail', args=[self.writer.id])
        data = {'title': 'Updated Book Title', 'writer': writer_url}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book Title')
        # Check that the 'url' and 'writer' (hyperlinked) fields exist in the response
        self.assertIn('url', response.data)
        self.assertIn('writer', response.data)
        self.assertIn('writer_name', response.data)
        self.assertEqual(response.data['writer_name'], "Carmen Posadas")

    def test_delete_book(self):
        """Test DELETE /books/<book_id>/ to delete a book."""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify book has been deleted
        self.assertFalse(Book.objects.filter(pk=self.book.id).exists())
