#removing duplicates from the list
list1 = ["bag", "bag", "apple", "orange", "camp", "camp"]
list1 = list(dict.fromkeys(list1))
print(list1)