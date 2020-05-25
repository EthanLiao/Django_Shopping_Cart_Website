# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product ,Navbar
import random,string

'''function control area'''

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


'''views control area'''

def navbars_list(request):
    navbars = Navbar.objects.all()
    return render(request,
                  'shop/product/base.html',
                  {'navbars':navbars,})


def product_search(request,navbar_slug=None,cache_query=None):
    navbars = Navbar.objects.all()
    if (not cache_query) :
        query = request.GET.get('Keyword',None)
    else :
        query = cache_query

    if (not query) or (query==' '):
        query = randomString()
    # product search
    search_result = Product.available_product.general_search(query=query)
    products = search_result
    if navbar_slug:
        products=[]
        for s in search_result:
            if s.category.navbar.slug == navbar_slug:
                products.append(s)

    #   products=search_result.filter(category.navbar.slug=navbar_slug)
    mess_navs=[]
    for r in search_result:
        mess_navs.append(r.category.navbar)
    ordered_navs = list(set(mess_navs)) # make all the navbar be ordered
    return render(request,
                  'shop/product/search.html',
                  {"query":query,
                    "navbars":navbars,
                    "ordered_navs":ordered_navs,
                    "search_result":search_result,
                    "products":products
                  }
                 )
def product_list(request, category_slug=None , navbar_slug=None ,category_id=0):        # get the category_slug parameter from the shop/urls.py
    category = None
    products = Product.objects.filter(available=True) # get the product which is availabe
    #categories = Category.objects.all()               # get all the category
    categories = None               # get all the category
    navbar = None
    navbars= Navbar.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if navbar_slug:
        navbar = get_object_or_404(Navbar,slug=navbar_slug)
        categories = Category.objects.filter(navbar=navbar)
        if categories :
            category =  list(categories)[0]
            products = Product.objects.filter(category=category)
        if not categories:
            products = None
        #navbars = Navbar.objects.all()
    if navbar_slug and category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'navbars':navbars,
                   'navbar':navbar
                   })

def product_detail(request,category_slug,navbar_slug,product_id,slug,product_price=0,product_kilometers=0):
    navbar = get_object_or_404(Navbar,slug=navbar_slug)
    categories = Category.objects.filter(navbar=navbar)
    category = get_object_or_404(Category,slug=category_slug)
    product = get_object_or_404(Product,
                                id=product_id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    navbars= Navbar.objects.all()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'navbars':navbars,
                   'category':category,
                   'categories':categories,
                   'navbar':navbar})
