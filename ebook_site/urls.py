

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from books import urls as books_urls

urlpatterns = [
#     url(r'^books/', include(books_urls, namespace='books')),     
    url(r'^$', include(books_urls, namespace='books')),      
    url(r'^admin/', include(admin.site.urls)),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
