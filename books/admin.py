from django.contrib import admin
from books.models import Author, Book, BookHasAuthor, Category, BookHasCategory

class AuthorInline(admin.StackedInline):
    model = Author
    ordering = ('-name',)
    
class AuthorAdmin(admin.ModelAdmin):
    inlines = [AuthorInline]
    list_display = ['name', 'slug']
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)


class BookHasAuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'author', 'book')
    list_display = ('name', 'slug', 'author', 'book')
admin.site.register(BookHasAuthor, BookHasAuthorAdmin)

class BookHasCatgoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'category', 'book')
    list_display = ('title', 'slug', 'category', 'book')

admin.site.register(BookHasCategory, BookHasCatgoryAdmin)

