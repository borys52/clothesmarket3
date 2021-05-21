from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET
from main_clothesmarket.models import Product
from .cart import Cart



@require_GET
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart_clothesmarket:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    product.available = True
    product.save()

    cart.remove(product)
    return redirect('cart_clothesmarket:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})
