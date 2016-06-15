from haystack import indexes
from .models import Book, Author, Category


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    year = indexes.CharField(model_attr='year')
    
    def get_model(self):
        return Book
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

