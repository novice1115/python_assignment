#removing an item from a tuple
tuple1 = (2, 20, 200, 2000)
list1 = list(tuple1)
print(list1)
list1.pop(3)
tuple1 = tuple(list1)
print(tuple1)
