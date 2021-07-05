from django import template

register = template.Library()

@register.filter()
def price_format(value):
  return 'AR$ {0:.2f}'.format(value)