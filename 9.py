def changeFirstLast(string):
    return string[-1:] + string[1:-1] + string[:1]
string = input("Enter the original string:")
print("String after the exchange of the first and last character:\t")
print(changeFirstLast(string))
