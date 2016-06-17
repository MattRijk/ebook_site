from haystack import indexes
from books.models import Book

class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
  

    def get_model(self):
        return Book
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
    
    
