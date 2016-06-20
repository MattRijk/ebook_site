from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from books.models import Book, Author, Category
from django.views.generic.list import ListView
from django.views.generic import FormView
from books.forms import DataForm
from django.utils.text import slugify
from django.core.context_processors import csrf
from .forms import SearchForm
from haystack.query import SearchQuerySet
from django.core.paginator import Paginator, EmptyPage, InvalidPage



def book_list(request):
    
    cd = None
    results = None
    total_results = None
    
    query_list = Book.objects.all()
    
    paginator = Paginator(query_list, 4)
    
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
        
    try:
        books = paginator.page(page)
    except(EmptyPage, InvalidPage):
        books = paginator.page(paginator.num_pages)

    # search 
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Book).filter(content=cd['query']).load_all()
            # count total results
            total_results = results.count() 
    
    args = {}
    args.update(csrf(request))
    args['book_list'] = books
    args['form'] = form
    args['cd'] = cd
    args['results'] = results
    args['total_results'] = total_results
    
  
    return render(request, 'books/index.html', args)



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
     

    
    