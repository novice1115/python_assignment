def largestNumber(list ):
    max = list[ 0 ]
    for n in list:
        if n > max:
            max = n
    return max
print(largestNumber([100, 82, 56, 20]))
