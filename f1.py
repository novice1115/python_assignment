def maxNumber(a, b, c):
    if (a > b) and (a > c):
        largestNumber = a
    elif (b > a) and (b > c):
        largestNumber = b
    else:
        largestNumber = c
        return largestNumber
print("Largest Number is:\n", maxNumber(10, 60, 90))
