def addString(a):
    lengthofString = len(a)
    if lengthofString > 2:
        if a[-3:] == 'ing':
            a += 'ly'
        else:
            a+= 'ing'
    return a
print(addString('abc'))
print(addString('string'))
