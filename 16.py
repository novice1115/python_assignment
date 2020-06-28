listElements = input("Enter the elements in the list:\n ")
list = listElements.split()
sum = 0
for num in list:
    sum += int (num)
print("Sum of the elements in the list is:\n", sum)
