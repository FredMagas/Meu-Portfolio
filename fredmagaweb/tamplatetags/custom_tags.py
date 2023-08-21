from django import template

register = template.Library()

@register.filter
def split_technologies(technologies):
    return technologies.split(',')