products=eval(input("enter the dictionary"))
sort_by=input("key/price:").strip().upper()
if sort_by=='KEY':
    sorted_dict=dict(sorted(products.item()))
elif sort_by=="PRICE":
    sorted_dict=dict(sorted(products.items(),key=lambda item:item[1]))
else:
    sorted_dict=products
    print("Invalid sort option")
    print("Sorted Dictionary:",sorted_dict)