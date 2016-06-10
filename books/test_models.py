from django.test import TestCase
from django.core.files import File
from books.models import Book, Author, Category

class BookModelTest(TestCase):

    def test_string_representation(self):
        book = Book(title='Introduction to Finance')
        self.assertEqual(str(book.title), 'Introduction to Finance')
        
    
    def test_get_absolute_url(self):
        image = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.jpg', mode="rb"))
        pdf = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.pdf', mode="rb"))
        book = Book.objects.create(title='Corporate Finance', pages='272', image=image, pdf=pdf, year='2003', filesize='1.62 MB', file_format='PDF')
        self.assertIsNotNone(book.get_absolute_url())
        
class AuthorModelTest(TestCase):

    def test_string_representation(self):
        author = Author(name='John Smith')
        self.assertEqual(str(author.name), 'John Smith')
        
        
class CategoryModelTest(TestCase):

    def test_string_representation(self):
        category = Category(title='Quant Investing')
        self.assertEqual(str(category.title), 'Quant Investing')
        

        
        
        


