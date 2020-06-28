def evenNumbers(list):
    evennum = []
    for n in list:
        if n % 2 == 0:
            evennum.append(n)
    return evennum
print("Even numbers in the list:" ,evenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
