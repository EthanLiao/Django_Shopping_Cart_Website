# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from .task import order_created
from MQTT.MQTT_sub import mqtt_run
TRANS_CHOICES = [(1,'貨到付款'),(2,'匯款')]

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            trans_method = int(form.cleaned_data.get("transportationMethod"))
            for choice in TRANS_CHOICES:
                if trans_method in choice:
                    trans_method=choice[1]
            order.transportationMethod = trans_method
            # order = form.save()
            # order = form.save(commit=False)
            # order.transportationMethod = trans_method
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            order_created(order.id)
            request.session['order_id'] = order.id
            # redirect to the payment
            return redirect('payment:process')
        else:
            return render(request,
                          'orders/order/create.html',
                          {'cart': cart, 'form': form})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
