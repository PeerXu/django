from django import templates

register = template.Library()

def my_cut(value, arg):
    return value.replace(arg, '')
