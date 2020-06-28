listElements = input("Enter the elements: ")
list = listElements.split()
product = 1
for num in list:
    product *= int(num)
print("Product of the elements in the list is: ", product)
