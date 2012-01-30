from django import template

register = template.Library()

@register.filter(name='my_cut')
def my_cut(value, arg):
    return value.replace(arg, '')

#register.filter('my_cut', my_cut)
