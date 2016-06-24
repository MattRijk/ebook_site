import io
import csv
from django.utils import timezone
from django.utils.text import slugify
from django.core.files import File
from django import forms
from books.models import Category, Author, Book, BookHasCategory, BookHasAuthor

class SearchForm(forms.Form):
    query = forms.CharField()

class DataForm(forms.Form):
    data_file = forms.FileField()

    def process_data(self):
        f=io.TextIOWrapper(self.cleaned_data['data_file'].file)
        reader = csv.DictReader(f)

            
        for cursor in reader:
            a1 = Author.objects.create(name=cursor['name1'])
            a2 = Author.objects.create(name=cursor['name2'])
            
            c = Category.objects.get(slug=cursor['slug'])
            now = timezone.now()
        
            b1 = Book.objects.create(title=cursor['title'], year=cursor['year'], pages=cursor['pages'], filesize=cursor['filesize'], file_format=cursor['file_format'], pdf=File(open(cursor['pdf'], mode="rb")), image=File(open(cursor['image'], mode="rb")), published=now)  
            
            
            BookHasAuthor.objects.create(author=a1, book=b1)
            BookHasAuthor.objects.create(author=a2, book=b1)
            
   
            BookHasCategory.objects.create(book=b1, category=c)
               
            
          


        
            