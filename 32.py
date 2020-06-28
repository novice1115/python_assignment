#generating and printing dictionary that contains numbers between 1 to n
number = int(input("Enter a number:"))
dictionary = dict()
for x in range(1 , number + 1):
    dictionary[x] = x * x
print(dictionary)
