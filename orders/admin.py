from django.contrib import admin

from .models import Order, OrderItem

import sys
import importlib
importlib.reload(sys)
#sys.setdefaultencoding("utf8")
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'phone_num', 'city','transportationMethod', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
