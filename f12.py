def func(n):
  return lambda a : a * n
tripledValue = func(3)
print(tripledValue(11))

