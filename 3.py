def replaceCharacter(a):
    char = a[0]
    a = a.replace(char, "$")
    a = char + a[1:]
    return a
print(replaceCharacter("restart"))
# print(replaceCharacter("pythonprogramming"))


