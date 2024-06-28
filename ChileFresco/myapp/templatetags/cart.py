# templatetags/cart.py
from django import template

register = template.Library()

@register.filter
def cart_quantity(product, cart):
    return cart.get(str(product.id), 0)

@register.filter
def price_total(product, cart):
    return product.price * cart.get(str(product.id), 0)

@register.filter
def total_cart_price(products, cart):
    return sum(product.price * cart.get(str(product.id), 0) for product in products)
