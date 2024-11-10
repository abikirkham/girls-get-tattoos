from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified item (product or consultation) to the shopping bag """

    try:
        product = Product.objects.get(pk=item_id)
        item_type = 'product'
    except Product.DoesNotExist:
        product = None
        item_type = 'consultation'
        consultation = get_object_or_404(Consultation, pk=item_id)  # Assuming you have a Consultation model
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_type == 'product':
        item = product
    else:
        item = consultation

    # Adding the item to the bag
    if item_id in list(bag.keys()):
        bag[item_id]['quantity'] += quantity
        messages.success(request, f'Updated {item.name} quantity to {bag[item_id]["quantity"]}')
    else:
        bag[item_id] = {'quantity': quantity, 'type': item_type}
        messages.success(request, f'Added {item.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified item (product or consultation) in the bag"""

    bag = request.session.get('bag', {})
    item_type = bag.get(item_id, {}).get('type')

    if item_type == 'product':
        item = Product.objects.get(pk=item_id)
    else:
        item = get_object_or_404(Consultation, pk=item_id)

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
