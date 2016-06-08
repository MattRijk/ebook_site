from django.test import TestCase
from books.models import Book

class BookModelTest(TestCase):

    def test_string_representation(self):

        book = Book(title='Introduction to Finance')
        self.assertEqual(str(book.title), 'Introduction to Finance')


