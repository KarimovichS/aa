from django import template
import web1.views as views

register = template.Library()


@register.simple_tag(name='getcats')
def get_category():
    return views.cats_db


@register.inclusion_tag('web1/list_categories.html')
def show_categories(cats_selected=0):
    cats = views.cats_db
    return {'cats': cats, 'cats_selected': cats_selected}
