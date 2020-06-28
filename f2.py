listElements = input("Enter the elements: ")
list = listElements.split()
sum = 0
for num in list:
    sum += int(num)
print("Sum: ",sum)
