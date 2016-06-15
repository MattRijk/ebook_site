from haystack import indexes
from .models import Book, Category


class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    year = indexes.CharField(model_attr='year')
#     authors = indexes.CharField(model_attr='authors')
        
    def get_model(self):
        return Book
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()


# class CategoryIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     
#     def get_model(self):
#         return Category
#     
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()