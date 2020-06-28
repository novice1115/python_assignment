def matchWords(words):
  counter = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      counter += 1
  return counter

print(matchWords(['abc', 'xyz', 'aba', '1221']))
