#multiplying all the items in the dictionary
dictionary = {"apple":4, "mango": 5, "orange": 6}
product = 1
for key in dictionary:
    product = product * dictionary[key]
print("Product is:", product)

