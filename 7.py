#finding the length of the longest word from the list

def findLongestWord(words):
    length = []
    for a in words:
        length.append((len(a), a))
    length.sort()
    return length[-1][1]

print(findLongestWord(["Insight ", "Workshop", "Python", "Programming"]))