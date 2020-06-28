#merging the dictionaries
dict1 = {"apple": 100, "orange": 200}
dict2 = {"cherry": 300, "mango": 200}
dictionary = dict1.copy()
dictionary.update(dict2)
print(dictionary)
