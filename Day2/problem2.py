n=eval(input("enter the number"))
k=int(input)("enter the k value:")
product=1
for tup in tuple_lists:
    if k>len(tup):
        product=product*tup[k]

    else:
        print("invalid k value")
        break
else:
    print(product)