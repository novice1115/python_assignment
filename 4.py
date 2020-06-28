
def replaceStrings(str1, str2):
    newString1 = str2[:2] + str1[2:]
    newString2 = str1[:2] + str2[2:]
    return newString1 + ' ' + newString2
print(replaceStrings('abc', 'xyz'))
