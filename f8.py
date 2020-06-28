def newList(list):
  x = []
  for a in list:
    if a not in x:
      x.append(a)
  return x
print("New list:\n", newList([1,2,3,3,3,3,4,5]))

