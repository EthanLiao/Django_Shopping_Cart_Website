from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.cart_detail,   #when use cart_detail in views.py we call the cart/views.py cart_detail function
        name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$',
        views.cart_add,     # pass the product_id get from the url and pass it to cart/views.py cart_add function
        name='cart_add'),   # we define cart_add api in this area , and then use it in the detail.html
    url(r'^remove/(?P<product_id>\d+)/$',
        views.cart_remove,
        name='cart_remove'),
]
