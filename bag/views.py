from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages


def view_bag(request):
    """
    A view to render the bag template
    """

    context = {}

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """
    A view to add an item to the bag
    """

    product = Product.objects.get(pk=item_id)
    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')

    if item_id not in list(bag.keys()):
        bag[item_id] = item_id
        messages.success(
            request,
            f'{product.name} was successfully added to your bag!'
        )
    else:
        messages.info(request, f'{product.name} is already in your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_item(request, item_id):
    """
    A view to remove an item from the bag
    """

    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)

    if item_id in list(bag.keys()):
        del bag[item_id]
        messages.success(
            request,
            f'{product.name} was successfully removed from your bag!'
        )

    request.session['bag'] = bag
    return redirect('bag')
