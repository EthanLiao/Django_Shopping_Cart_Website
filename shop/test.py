from shop.models import Product

search_result = Product.available_product.general_search(query=haha)
mess_navs=[]
for r in search_result:
    mess_navs.append(r.category.navbar.name)

ordered_navs= list(set(mess_navs))
print(ordered_navs.len())
for o in ordered_navs:
    print(o)
