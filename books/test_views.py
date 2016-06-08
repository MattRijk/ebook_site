from django.test import TestCase
from books.models import Book, Author, BookHasAuthor
from django.core.files import File


class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        
    def test_one_book(self):
#         author = Author.objects.create(name='Scott', slug='Meyers')
        image = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.jpg', mode="rb"))
        pdf = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.pdf', mode="rb"))
        Book.objects.create(title='Corporate Finance', pages='272', image=image, pdf=pdf, year='2003', filesize='1.62 MB', file_format='PDF')
        response = self.client.get('/books/')
        self.assertContains(response, 'Corporate Finance')
        self.assertContains(response, '2003')
        
#     def test_two_books(self):
#         Book.objects.create(title='1-title', body='1-body', author=)
#         Book.objects.create(title='2-title', body='2-body', author=)
#         response = self.client.get('/')
#         self.assertContains(response, '1-title')
#         self.assertContains(response, '1-body')
#         self.assertContains(response, '2-title')