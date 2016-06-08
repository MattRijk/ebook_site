from django.conf.urls import include, url
from books.views import  BookDetailView,  \
    BookListView, CategoryBookView, DataFormView, AuthorDetailView

urlpatterns = [

#     url(r'^$', BookListView.as_view(), name='book_list'),
    url(r'^book/(?P<slug>[\w-]+)/$', BookDetailView.as_view(), name='detail_view'),
    #url(r'^detail/(?P<slug>[-\w]+)/$', BookDetailView.as_view(), name='detail_view'),   
    url(r'^author/(?P<slug>[\w-]+)/$', AuthorDetailView.as_view(), name='author_view'),
    url(r'^category/(?P<slug>[\w-]+)/$', CategoryBookView.as_view(), name='category_detail'),
    
    url(r'^data-upload/', DataFormView.as_view(), name='data_upload'), 
    
]