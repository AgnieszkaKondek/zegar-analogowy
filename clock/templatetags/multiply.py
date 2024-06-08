from django import template

register = template.Library()

@register.filter(name='multiply')
def times(value, arg):
    return value * arg
