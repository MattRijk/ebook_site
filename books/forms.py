import io
import csv
from django.utils import timezone
from django.utils.text import slugify
from django.core.files import File
from django import forms
from books.models import Category, Author, Book, BookHasCategory, BookHasAuthor


class DataForm(forms.Form):
    data_file = forms.FileField()

    def process_data(self):
        f=io.TextIOWrapper(self.cleaned_data['data_file'].file)
        reader = csv.DictReader(f)

        
#         for cursor in reader:
#             a1 = Author.objects.create(name=cursor['name1'])
# #             a2 = Author.objects.create(name=cursor['name2'])
# #             a3 = Author.objects.create(name=cursor['name3'])
#             c = Category.objects.get(slug=cursor['slug'])
#             now = timezone.now()
#             b = Book.objects.create(title=cursor['title'], year=cursor['year'], pages=cursor['pages'], filesize=cursor['filesize'], file_format=cursor['file_format'], pdf=File(open(cursor['pdf'], mode="rb")), image=File(open(cursor['image'], mode="rb")), published=now)  
#             
# #             a.save()
# #             b.save()
#             
#             ba1 = BookHasAuthor(author=a1, book=b)
# #             ba2 =  BookHasAuthor(author=a2, book=b)
# #             ba3 = BookHasAuthor(author=a3, book=b)
#             bc = BookHasCategory(book=b, category=c)
#             
#             ba1.save()
# #             ba2.save()
# #             ba3.save()
#             bc.save()
            
            
        for cursor in reader:
            a1 = Author.objects.create(name=cursor['name1'])
            c = Category.objects.get(slug=cursor['slug'])
            now = timezone.now()
        
        
            b1 = Book.objects.create(title=cursor['title1'], year=cursor['year1'], pages=cursor['pages1'], filesize=cursor['filesize1'], file_format=cursor['file_format1'], pdf=File(open(cursor['pdf1'], mode="rb")), image=File(open(cursor['image1'], mode="rb")), published=now)  
            b2 = Book.objects.create(title=cursor['title2'], year=cursor['year2'], pages=cursor['pages2'], filesize=cursor['filesize2'], file_format=cursor['file_format2'], pdf=File(open(cursor['pdf2'], mode="rb")), image=File(open(cursor['image2'], mode="rb")), published=now)  
            b3 = Book.objects.create(title=cursor['title3'], year=cursor['year3'], pages=cursor['pages3'], filesize=cursor['filesize3'], file_format=cursor['file_format3'], pdf=File(open(cursor['pdf3'], mode="rb")), image=File(open(cursor['image3'], mode="rb")), published=now)  
        
        #             a.save()
        #             b.save()
            
            ba1 = BookHasAuthor(author=a1, book=b1)
            ba2 =  BookHasAuthor(author=a1, book=b2)
            ba3 = BookHasAuthor(author=a1, book=b3)
        
            bc1 = BookHasCategory(book=b1, category=c)
            bc2 = BookHasCategory(book=b2, category=c)
            bc3 = BookHasCategory(book=b3, category=c)
            
            ba1.save()
            ba2.save()
            ba3.save()
        
            bc1.save()
            bc2.save()
            bc3.save()
            
        
            