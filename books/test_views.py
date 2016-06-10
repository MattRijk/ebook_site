from django.test import TestCase, testcases
from django.core.files import File
from django.template import Template, Context
from django.core.urlresolvers import reverse, resolve
from books.models import Book, Author, BookHasAuthor, Category
from books.templatetags import navtags




class BookListViewTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_one_book(self):
#         author = Author.objects.create(name='Scott', slug='Meyers')
        image = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.jpg', mode="rb"))
        pdf = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.pdf', mode="rb"))
        Book.objects.create(title='Corporate Finance', pages='272', image=image, pdf=pdf, year='2003', filesize='1.62 MB', file_format='PDF')
        response = self.client.get('/')
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
        
        response = self.client.get('/')

        self.assertContains(response, 'Corporate Finance')
        self.assertContains(response, '2003')
        self.assertContains(response, 'Scott Meyer')
        self.assertContains(response, 'Sarah Green')
        
        self.assertContains(response, 'Applied Quantitative Finance')
        self.assertContains(response, '2009')
        self.assertContains(response, 'Jennifer Rose')
        self.assertContains(response, 'Jose Rogers')
        self.assertContains(response, 'Scott Meyer')
        
    def test_book_get_absolute_url(self):
        image = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.jpg', mode="rb"))
        pdf = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.pdf', mode="rb"))
        book =  Book.objects.create(title='Corporate Finance', pages='272', image=image, pdf=pdf, year='2003', filesize='1.62 MB', file_format='PDF')
        response = self.client.get(book.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        
    def test_author_get__url(self):
        author = Author.objects.create(name = 'Scott Meyer')
        image = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.jpg', mode="rb"))
        pdf = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.pdf', mode="rb"))
        book =  Book.objects.create(title='Corporate Finance', pages='272', image=image, pdf=pdf, year='2003', filesize='1.62 MB', file_format='PDF')
         
        BookHasAuthor.objects.create(book=book, author=author)
#          response = self.client.get('author/%s/' % author.slug)
        author= resolve('/author/scott-meyer/')
        self.assertEqual(author.kwargs['slug'], 'scott-meyer')
        
    def test_author_url(self):
        author = Author.objects.create(name = 'Scott Meyer')
        image = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.jpg', mode="rb"))
        pdf = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.pdf', mode="rb"))
        book =  Book.objects.create(title='Corporate Finance', pages='272', image=image, pdf=pdf, year='2003', filesize='1.62 MB', file_format='PDF')
         
        BookHasAuthor.objects.create(book=book, author=author)
        response = self.client.get('/author/%s/' % (author.slug,))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/author_books.html')
        
        
class BookDetailViewTest(TestCase):
    
    def book_detail_page(self):
        image = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.jpg', mode="rb"))
        pdf = File(open(r'C:\Users\matt\Desktop\temp\corporate_finance_theory_and_practice.pdf', mode="rb"))
        book =  Book.objects.create(title='Corporate Finance', pages='272', image=image, pdf=pdf, year='2003', filesize='1.62 MB', file_format='PDF')
        response = self.client.get(book.get_absolute_url())
        self.assertEqual(response.status_code, 200)


class CategoryNavTagTest(TestCase):
    TEMPLATE = Template("{% load navtags %} {% get_nav as categories %}")

    def test_category_shows_up(self):
        category = Category.objects.create(title="Stock Trading")
        categories = navtags.get_nav()
        rendered = [category.title for category in categories]
        self.assertIn(category.title, rendered)
        
class CategoryDetailViewTest(TestCase):
    pass

         
       
   
        
 