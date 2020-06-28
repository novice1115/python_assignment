#sorting the list of tuples
fruits = [("Apple", 100), ("Orange", 20), ("Mango", 190)]
print("List of Fruits:", fruits)
fruits.sort(key = lambda x: x[1])
print("After sorting the list of fruits:", fruits)