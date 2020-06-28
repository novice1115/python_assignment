#sorting the list of dictionaries
fruits = [{"name": "apple", "price":100} , {"name": "orange", "price":50} , {"name": "mango", "price": 80}, {"name": "cherry",
           "price": 105}]
print("List: ", fruits)
sortedList = sorted(fruits, key = lambda x: x["price"])
print("Sorting the List of dictionaries :", sortedList)


