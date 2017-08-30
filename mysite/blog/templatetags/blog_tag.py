from django import template

register = template.Library()
from django.template.defaultfilters import stringfilter

@register.filter(name="rq")
def rq(value):
    return str(value.pub_date.year)+"-"+str(value.pub_date.month)+"-"+str(value.pub_date.day)


@register.filter(name="size")
def size(value):
    return len(value)


