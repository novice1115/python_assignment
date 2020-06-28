#program for removing nth index character from the nonempty string
def removeCharacter(string, n):
    a = string[:n]
    b = string[n + 1:]
    return a + b
#removing the 4th character from the word 'workshop'
print(removeCharacter("Workshop", 4))

