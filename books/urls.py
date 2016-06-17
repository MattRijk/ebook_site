from django.conf.urls import include, url
from books.views import  BookDetailView,  \
    DataFormView, AuthorDetailView, CategoryDetailView


urlpatterns = [


    url(r'^book/(?P<slug>[\w-]+)/$', BookDetailView.as_view(), name='detail_view'),
    #url(r'^detail/(?P<slug>[-\w]+)/$', BookDetailView.as_view(), name='detail_view'),   
    url(r'^author/(?P<slug>[\w-]+)/$', AuthorDetailView.as_view(), name='author_view'),
    url(r'^category/(?P<slug>[\w-]+)/$', CategoryDetailView.as_view(), name='book_category'),
    url(r'^data-upload/', DataFormView.as_view(), name='data_upload'), 
    
]