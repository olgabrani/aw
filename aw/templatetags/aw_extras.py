from django import template

register = template.Library()


@register.simple_tag
def sample_tag(v):
    return v+'a'

@register.filter
def lookup(d,key):
    return d.get(key)
