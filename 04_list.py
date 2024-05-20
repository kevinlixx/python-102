#ciclo
numbers = []
for element in range(1, 11):
  numbers.append(element)
  
print(numbers)


numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

#conditional
numbers = []
for i in range(1, 11):
  if i % 2 == 0: #guarda solo los pares
    numbers.append(i * 2)

print(numbers)

numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]