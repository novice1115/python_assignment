def smallestNumber(list ):
    min = list[ 0 ]
    for n in list:
        if n < min:
            min = n
    return min
print(smallestNumber([100, 82, 56, 20]))
