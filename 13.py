#entering the comma separated sequence of words to print the unique words in sorted form
words= input("Enter the comma separated sequence of words:\n")
result = [word for word in words.split(",")]
print(",".join(sorted(list(set(result)))))
