# custom_filters.py

from django import template
from Inventory.models import Item

register = template.Library()


@register.filter(name='calculate_total_cost')
def calculate_total_cost(code_input):
    try:
        item = Item.objects.get(code=code_input)
        total_cost = item.purchase_cost + item.shipping_cost
    except Item.DoesNotExist:
        total_cost = 0  # Handle the case when the item with the given code does not exist

    return total_cost
