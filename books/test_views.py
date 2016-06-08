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
        
    def test_two_books_with_authors(self):
        
        a1 = Author.objects.create(name = 'Scott Meyer')
        a2 = Author.objects.create(name = 'Sarah Green')
        a3 = Author.objects.create(name = 'Jennifer Rose')
        a4 = Author.objects.create(name = 'Jose Rogers')
        
        image1 = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.jpg', mode="rb"))
        pdf1 = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.pdf', mode="rb"))
        b1 = Book.objects.create(title='Corporate Finance', pages='272', image=image1, pdf=pdf1, year='2003', filesize='1.62 MB', file_format='PDF')
        image2 = File(open(r'C:\Users\matt\Desktop\temp\applied_quantitive_finance.jpg', mode="rb"))
        pdf2 = File(open(r'C:\Users\matt\Desktop\temp\applied_quantitive_finance.pdf', mode="rb"))
        b2 = Book.objects.create(title='Applied Quantitative Finance', pages='411', image=image2, pdf=pdf2, year='2009', filesize='2.25 MB', file_format='PDF')
        
        scott = BookHasAuthor.objects.create(book=b1, author=a1)
        sarah = BookHasAuthor.objects.create(book=b1, author=a2)
        
        jennifer = BookHasAuthor.objects.create(book=b2, author=a3)
        jose = BookHasAuthor.objects.create(book=b2, author=a4)
        scott = BookHasAuthor.objects.create(book=b2, author=a1)
        
        response = self.client.get('/books/')

        self.assertContains(response, 'Corporate Finance')
        self.assertContains(response, '2003')
        self.assertContains(response, 'Scott Meyer')
        self.assertContains(response, 'Sarah Green')
        
        self.assertContains(response, 'Applied Quantitative Finance')
        self.assertContains(response, '2009')
        self.assertContains(response, 'Jennifer Rose')
        self.assertContains(response, 'Jose Rogers')
        self.assertContains(response, 'Scott Meyer')
   
        
 