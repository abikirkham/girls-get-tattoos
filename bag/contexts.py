from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, dict) and 'quantity' in item_data:
            quantity = item_data['quantity']
        else:
            quantity = item_data

        quantity = int(quantity)
        product = get_object_or_404(Product, pk=item_id)

        subtotal = quantity * product.price

        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'price': product.price,
            'image_url': product.image.url if product.image else None,
            'subtotal': subtotal,
        })

        total += subtotal
        product_count += quantity

    if total < Decimal(settings.FREE_DELIVERY_THRESHOLD):
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / Decimal('100')
        free_delivery_delta = Decimal(settings.FREE_DELIVERY_THRESHOLD) - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': Decimal(settings.FREE_DELIVERY_THRESHOLD),
        'grand_total': grand_total,
    }

    return context
