from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag(takes_context=True)
def productCard(context):
    # Implement your logic here to fetch product data and render the HTML for the card
    # For demonstration purposes, let's assume you have a list of products
    products = [
        {'name': 'Product 1', 'description': 'Description of Product 1', 'price': 10},
        {'name': 'Product 2', 'description': 'Description of Product 2', 'price': 20},
        {'name': 'Product 3', 'description': 'Description of Product 3', 'price': 30},
    ]
    return render_to_string('product_card_template.html', {'card_collection': products})
