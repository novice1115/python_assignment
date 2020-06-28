#checking if the dictionary in the list is empty or not 
list1 = [{},{},{}]
list2= [{1,2},{},{}]
print(all(not d for d in list1))
print(all(not d for d in list2))
