# -*- coding: UTF-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.product_list,
        name='product_list'),
    url(r'^search/$',
        views.product_search,
        name='product_search'),
    url(r'^search/(?P<navbar_slug>[-\w]+)/(?P<cache_query>[-\w]+)/$',
        views.product_search,
        name='product_list_by_search'),
    url(r'^(?P<navbar_slug>[-\w]+)/$',
        views.product_list,
        name='category_list_by_navbars'),
    url(r'^(?P<category_slug>[-\w]+)/(?P<navbar_slug>[-\w]+)/(?P<category_id>\d+)/$',
        views.product_list,
        name='product_list_by_category'),

    url(r'^(?P<category_slug>[-\w]+)/(?P<navbar_slug>[-\w]+)/(?P<product_id>\d+)/(?P<slug>[-\w]+)/(?P<product_price>\d+)/(?P<product_kilometers>\d+)/$',
        views.product_detail,
        name='product_detail'),

    ]
