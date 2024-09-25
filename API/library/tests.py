from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Writer, Book

class WriterViewSetTests(APITestCase):
    
    def setUp(self):
        """Set up initial data for testing."""
        self.writer = Writer.objects.create(name="Carmen Posadas")
        self.writer2 = Writer.objects.create(name="Luis García Rey")
    
    def test_get_all_writers(self):
        """Test GET /writers/ to fetch all writers."""
        url = reverse('writer-list')  # The name of the URL pattern for the writer list
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check if we get two writers

    def test_get_single_writer(self):
        """Test GET /writers/<writer_id>/ to fetch a single writer."""
        url = reverse('writer-detail', args=[self.writer.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Carmen Posadas")

    def test_create_writer(self):
        """Test POST /writers/ to create a new writer."""
        url = reverse('writer-list')
        data = {'name': 'Robert Menasse'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Robert Menasse')

    def test_update_writer(self):
        """Test PUT /writers/<writer_id>/ to update an existing writer."""
        url = reverse('writer-detail', args=[self.writer.id])
        data = {'name': 'Updated Name'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Name')

    def test_delete_writer(self):
        """Test DELETE /writers/<writer_id>/ to delete a writer."""
        url = reverse('writer-detail', args=[self.writer.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
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

    def test_get_single_book(self):
        """Test GET /books/<book_id>/ to fetch a single book."""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "La leyenda de la peregrina")

    def test_create_book(self):
        """Test POST /books/ to create a new book."""
        url = reverse('book-list')
        data = {
            'title': 'The Capital',
            'writer': 'Carmen Posadas'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'The Capital')

    def test_update_book(self):
        """Test PUT /books/<book_id>/ to update an existing book."""
        url = reverse('book-detail', args=[self.book.id])
        data = {'title': 'Updated Book Title', 'writer': 'Carmen Posadas'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book Title')

    def test_delete_book(self):
        """Test DELETE /books/<book_id>/ to delete a book."""
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify book has been deleted
        self.assertFalse(Book.objects.filter(pk=self.book.id).exists())
