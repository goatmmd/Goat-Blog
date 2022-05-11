from articles.models import Category
from django import template

register = template.Library()


@register.simple_tag
def get_all_category():
    return Category.objects.all()
