from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from books.models import Book, Author, Category
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from books.forms import DataForm
    

    
class BookListView(ListView):
    Model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books_list'
    queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    

     
class BookDetailView(View): 
     
    def get(self, request, slug=None, *args, **kwargs):
        template = 'books/book_detail.html'
        authors = None
        category = None
        
        try:
            book = get_object_or_404(Book, slug=slug)
                     
        except Book.MultipleObjectsReturned:
            book = Book.objects.filter(slug=slug)

        # authors
        queryset = Book.objects.get(slug=slug)
        authors = queryset.authors.all()
        
        # Book's category
        qset = Book.objects.get(slug=slug)
        category = qset.category_set.all()
       
        context = {'book': book, 'authors': authors, 'category': category}
       
        return render(request, template, context)
  
  
class AuthorView(View): 
      
    def get(self, request, slug=None, *args, **kwargs):
        template = 'books/author_list.html'
        author = Author.objects.get(slug=slug)
        queryset = author.book_set.all()
        context = {'authorbooks': queryset, 'author': author}
        return render(request, template, context)
 
    
class CategoryBookView(View):
    def get(self, request, slug=None, *args, **kwargs):
        template = 'categories/category_book_list.html'
        category = Category.objects.get(slug=slug)
        queryset = category.books.all()
        context = {'category':queryset, 'category_name': category}
        return render(request, template, context)
    
    
class DataFormView(FormView):
    template_name = 'books/csv_upload.html'
    form_class = DataForm
    success_url = 'books/book_list.html'

    def form_valid(self, form):
        form.process_data()
        return super().form_valid(form) 
     

    
    