# Create a new Python file (e.g., templatetags/custom_filters.py) in your app directory.

from django import template

register = template.Library()

@register.filter
def is_even(value):
    """
    Returns True if the value is even, False otherwise.
    """
    return value % 2 == 0
