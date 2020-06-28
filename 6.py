string1 = input("Enter a string: ")
findNot = string1.find('not')
findPoor = string1.find('poor')
if findPoor > findNot:
    string1 = string1.replace(string1[findNot:(findPoor + 4)], 'good')
print(string1)
