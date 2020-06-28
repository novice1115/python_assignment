# for intersection of the arrays
array1 = [100, 200, 300, 400]
array2 = [1, 2, 3, 400,100, 20, 200]
print(array1)
print(array2)
result = list(filter(lambda x: x in array1, array2))
print("Intersection of the arrays: ", result)
