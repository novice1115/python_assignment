#adding an item in a tuple
tuple1 = [10, 20, 30, 40]
list1 = list(tuple1)
print("Without adding items:\n",list1)
list1.append(50)
tuple1 = tuple(list1)
print("Adding new items:\n", tuple1)
