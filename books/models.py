from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(max_length=200, blank=True, unique=False)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super(Author, self).save(*args, **kwargs) 
            
    def get_absolute_url(self):
        return reverse('books:author_list', kwargs={'slug': self.slug})
    

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, blank=True, unique=False)
    year = models.CharField(max_length=10)
    pages = models.CharField(max_length=10)
    filesize = models.CharField(max_length=20)
    file_format = models.CharField(max_length=20)
    pdf = models.FileField(upload_to='pdfs/' )
    image = models.FileField(upload_to='images/')
    authors = models.ManyToManyField(Author, through='BookHasAuthor')
    published = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-published',)
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Book, self).save(*args, **kwargs)        
    
    def get_absolute_url(self):
        return reverse('books:detail_view', kwargs={'slug': self.slug})

    
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, blank=True, unique=False)
    books = models.ManyToManyField(Book, through='BookHasCategory')
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Category, self).save(*args, **kwargs) 
          

class BookHasAuthor(models.Model):
    name = models.CharField(max_length=45, blank=True, unique=False)
    slug = models.SlugField(max_length=200, blank=True, unique=False)
    author = models.ForeignKey(Author)   
    book = models.ForeignKey(Book)
      
    class Meta:
        unique_together = ['author', 'book']
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug or self.name:
            self.name = self.author.name
            self.slug = slugify(self.name)
            super(BookHasAuthor, self).save(*args, **kwargs)
            
    
class BookHasCategory(models.Model):
    title = models.CharField(max_length=45, blank=True, unique=False)
    slug = models.SlugField(max_length=200, blank=True, unique=False)
    book = models.ForeignKey(Book)   
    category = models.ForeignKey(Category)
    
        
    class Meta:
        unique_together = ['book', 'category']
        verbose_name_plural = 'Book has categories'
        
    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.title = self.category.title
            self.slug = slugify(self.title)
            super(BookHasCategory, self).save(*args, **kwargs)
    
    
