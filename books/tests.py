from django.test import TestCase
from django.utils.timezone import now, timedelta
from .models import Book
from rest_framework.test import APIClient
from rest_framework import status

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "title": "Test Book",
            "author": "phil",
            "publication_date":(now () - timedelta(days=1)).date(),
            "isbn": "1234567890123",
            "summary": "This is a test book",
        }
        self.book = Book.objects.create(**self.book_data)

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_book(self):
        new_book = {
            "title": "New Book",
            "author": "John",
            "publication_date": (now() - timedelta(days=10)).date(),
            "isbn": "1234567890124",
            "summary": "This is a new book",
        }

        response = self.client.post('/api/books/', new_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_invalid_isbn(self):
        invalid_book =  self.book_data.copy()
        invalid_book['isbn'] = "invalid_isbn"
        response = self.client.post('/api/books/', invalid_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_book_future_publication_date(self):
        future_book = self.book_data.copy()
        future_book['publication_date'] = (now() + timedelta(days=1)).date()
        response = self.client.post('/api/books/', future_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)