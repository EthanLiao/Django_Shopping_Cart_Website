# -*- coding: UTF-8 -*-
from django.db import models
from shop.models import Product
from django.core.exceptions import ValidationError
import calendar

MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=1024)
    phone_num = models.CharField(max_length=20)
    # city = models.CharField(max_length=100)
    city = models.CharField(max_length=10)
    country = models.CharField(max_length=10,blank=True)
    transportationMethod = models.CharField(max_length=10,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    #order = models.ForeignKey(Order,on_delete=models.SET('items'))
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    #product = models.ForeignKey(Order,on_delete=models.SET('order_items '))
    # 台灣價錢都是整數，所以可以設定 decimal_places=0
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
