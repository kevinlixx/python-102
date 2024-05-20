import functools

numbers = [1, 2, 3, 4]

# en modo de  funcion
def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

# en modo de lambda
result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)
