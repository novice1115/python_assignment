def wordCount(string):
    counts = dict()
    words = string.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( wordCount("There is a black bag near the black table."))
