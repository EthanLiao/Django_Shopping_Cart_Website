# -*- coding: UTF-8 -*-s
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Navbar
# we define some cart manipulation api in this code

@require_POST
def cart_add(request, product_id):                       # get the product_id parameter from the cart/urls.py
    cart = Cart(request)                                 # get the specific user cart, you can view the "request" as user's id
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)              # get the add from the cart/forms.py
    if form.is_valid():                                  # we examing whehter the form data is_valid and cleaned
        cd = form.cleaned_data                           # if get a form from detail.html, we set it as a dictionary type then assign to cd
        cart.add(product=product,
                 quantity=cd['quantity'],                #quantity and update defined in the cart/forms.py
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')                  # redirect to the cart/templates/cart/detail.html file
                                                         # cart_detail defined in the cart/urls.py


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    navbars = Navbar.objects.all()
    # 使用 for in 的時候，他會開始迭代，並且呼叫 `__iter__`
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],                   #quantity and update defined in the cart/forms.py
                'update': True
            })
    return render(request, 'cart/detail.html', {'cart': cart,'navbars':navbars})
