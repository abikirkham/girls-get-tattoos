from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

def view_bag(request):
    """ Display the shopping bag contents """
    bag = request.session.get('bag', {})
    items = []

    for item_id, item_data in bag.items():
        if item_data['type'] == 'product':
            product = get_object_or_404(Product, pk=item_id)
            items.append({
                'item': product,
                'quantity': item_data['quantity'],
                'type': 'product',
            })
    
    context = {
        'items': items,
    }

    return render(request, 'bag/bag.html', context)

def add_to_bag(request, item_id):
    """ Add a quantity of the specified item (product) to the shopping bag """
    try:
        product = Product.objects.get(pk=item_id)
        item_type = 'product'
        item = product

    except Product.DoesNotExist:
        return HttpResponse(status=404)

    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id]['quantity'] += quantity
        messages.success(request, f'Updated {item.name} quantity to {bag[item_id]["quantity"]}')
    else:
        bag[item_id] = {
            'quantity': quantity,
            'type': item_type,
            'name': item.name,
        }
        messages.success(request, f'Added {item.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified item (product) in the bag"""

    bag = request.session.get('bag', {})
    item_type = bag.get(item_id, {}).get('type')

    if item_type == 'product':
        item = Product.objects.get(pk=item_id)
    else:
        return HttpResponse(status=404)

    quantity = int(request.POST.get('quantity'))

    if quantity > 0:
        bag[item_id]['quantity'] = quantity
        messages.success(request, f'Updated {item.name} quantity to {bag[item_id]["quantity"]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {item.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = Product.objects.get(pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id, None)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
