from django import template

register = template.Library()

@register.filter
def range_filter(value: int):
    return range(value)

@register.filter
def range_filter_for_dark_stars(value: int):
    return range(5 - value)