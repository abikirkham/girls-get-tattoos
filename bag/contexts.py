from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from consultations.models import Consultation, ConsultationAvailability

def bag_contents(request):
    bag_items = []
    consultation_items = []
    total = Decimal('0.00')
    product_count = 0
    consultation_count = 0
    bag = request.session.get('bag', {})
    consultations = request.session.get('consultations', {})

    # Handle product items
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
        })

        total += subtotal
        product_count += quantity

    # Handle consultation items
    for consultation_id, consultation_data in consultations.items():
        consultation = get_object_or_404(Consultation, pk=consultation_id)
        selected_date_id = consultation_data.get('selected_date')
        selected_date = get_object_or_404(ConsultationAvailability, pk=selected_date_id)

        quantity = int(consultation_data.get('quantity', 1))
        subtotal = quantity * consultation.price

        consultation_items.append({
            'consultation_id': consultation_id,
            'consultation': consultation,
            'selected_date': selected_date,
            'quantity': quantity,
        })

        total += subtotal
        consultation_count += quantity

    # Calculate delivery and thresholds
    if total < Decimal(settings.FREE_DELIVERY_THRESHOLD):
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / Decimal('100')
        free_delivery_delta = Decimal(settings.FREE_DELIVERY_THRESHOLD) - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')
    
    grand_total = delivery + total
    
    # Context for rendering
    context = {
        'bag_items': bag_items,
        'consultation_items': consultation_items,
        'total': total,
        'product_count': product_count,
        'consultation_count': consultation_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': Decimal(settings.FREE_DELIVERY_THRESHOLD),
        'grand_total': grand_total,
    }

    return context
