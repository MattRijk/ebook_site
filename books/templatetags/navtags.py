from django import template
from django.template import Context
from books.models import Category

register = template.Library()



# @register.inclusion_tag('nav.html')
@ register.assignment_tag
def get_nav():
    queryset = Category.objects.all()
    return queryset