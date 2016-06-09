#my_tags.py
from django import template
from books.models import Category

register = template.Library()

@register.inclusion_tag('nav.html')
def get_nav_tag():
    categories = Category.objects.all()
    return {'categories' : categories}