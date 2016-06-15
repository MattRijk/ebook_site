from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from books.models import Book, Author, Category
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from books.forms import DataForm
from django.utils.text import slugify
from .forms import SearchForm
from haystack.query import SearchQuerySet
from pip._vendor.requests.api import request


def book_search(request):
    cd = None
    results = None
    total_results = None
    
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Book).filter(content=cd['query']).load_all()
            # count total results
            total_results = results.count()
    return render(request, 'books/search.html', {'form': form,
                                                 'cd': cd,
                                                 'results': results,
   
                                                 
                                                 'total_results': total_results})
    
class BookListView(ListView):
    
    def get(self, request, *args, **kwargs):
        cd = None
        results = None
        total_results = None
        
        queryset = Book.objects.all()
        
        form = SearchForm()
        if 'query' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                cd = form.cleaned_data
                results = SearchQuerySet().models(Book).filter(content=cd['query']).load_all()
                # count total results
                total_results = results.count()
        return render(request, 'books/search.html', {'books_list': queryset, 
                                                     'form': form,
                                                     'cd': cd,
                                                     'results': results,
                                                     'total_results': total_results})

# class BookListView(ListView):
#     Model = Book
#     template_name = 'books/index.html'
#     context_object_name = 'books_list'
#     
#     def get_queryset(self):
#         return Book.objects.all()
 


class BookDetailView(DetailView): 
    Model = Book
    template_name = 'books/book_detail.html'
    context_name = 'book'
    
    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug is not None:
            try:
                book = get_object_or_404(Book, slug=slug)
            except Book.MultipleObjectsReturned:
                book = Book.objects.filter(slug=slug).order_by('-title').first()
        else:
            book = super(BookDetailView, self).get_object(*args, **kwargs)
        return book
    
  
class AuthorDetailView(DetailView):    
    Model = Author
    template_name = 'books/author_books.html'
    context_object_name = 'author'
    
    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug is not None:
            try:
                author = get_object_or_404(Author, slug=slug)
            except Author.MultipleObjectsReturned:
                author = Author.objects.filter(slug=slug).order_by('-name').first()
        else:
            author = super(AuthorDetailView, self).get_object(*args, **kwargs)
        return author
    
    
class CategoryDetailView(DetailView):
    Model = Category
    template_name = 'books/book_category.html'
    context_object_name = 'category'
      
    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug is not None:
            try:
                category = get_object_or_404(Category, slug=slug)
            except Category.MultipleObjectsReturned:
                category = Category.objects.filter(slug=slug).order_by('-title').first()
        else:
            category = super(CategoryDetailView, self).get_object(*args, **kwargs)
        return category
     

    
    
class CategoryListView(ListView):
    Model = Category
    template_name = 'nav.html'
    context_object_name = 'categories'
      
    def get_queryset(self):
        return Category.objects.all()
    


class DataFormView(FormView):
    template_name = 'help/csv_upload.html'
    form_class = DataForm
    success_url = 'books/book_list.html'

    def form_valid(self, form):
        form.process_data()
        return super().form_valid(form) 
     

    
    