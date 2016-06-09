

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from books import urls as books_urls
from books.views import BookListView

urlpatterns = [
    url(r'^', include(books_urls, namespace='books')),     
    url(r'^$', BookListView.as_view(), name='home'),      
    url(r'^admin/', include(admin.site.urls)),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
