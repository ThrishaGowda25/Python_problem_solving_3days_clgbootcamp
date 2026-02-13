list_of_ids = input("enter list of id: ").split()
initial_set = set(list_of_ids)
duplicate_set = set()

for product in list_of_ids:
    if list_of_ids.count(product) > 1:
        duplicate_set.add(product)

result = initial_set - duplicate_set
print(result)
