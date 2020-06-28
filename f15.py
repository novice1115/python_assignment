list1 = [60, 13, 12, 71, 64, 3, 5, 120]
print("Original list: ", list1)
divisibleBy3 = list(filter(lambda x: x % 3 == 0, list1))
print("List of numbers divisible only by 3 is:", divisibleBy3)



