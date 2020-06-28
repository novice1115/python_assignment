#removing the odd value from the string
def removeOddValues(string):
  result = ''
  for i in range(len(string)):
    if i % 2 == 0:
      result = result + string[i]
  return result

print(removeOddValues("Insight"))
print(removeOddValues("workshop"))
