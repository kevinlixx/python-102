dict = {}

for i in range(1, 5):
  dict[i] = i * 2

print(dict)

dict_v2 = {i: i * 2
           for i in range(1, 5)
           }  # dict comprehension el cual es equivalente a la anterior
print(dict_v2)

import random
countries = ['col', 'mex', 'bol', 'per']  
population = {}
for country in countries:
  population[country] = random.randint(1,100)
print(population)
#dict comprehesion
population_v2 = { country:random.randint(1,100) for country in countries}
print(population_v2)

#ahora e quier unor estas dos listas en forma de diccionario
names = ['nico', ' zule', 'santi']
ages = [12, 56, 98]
#se quiere que quede de esta forma 
{
  'nico': 12,
  'zule': 56,
  'santi': 98
}

#para esto usaremos el atributo zip el cual nos devuelve una tupla de dos elementos
print(list(zip(names, ages)))#permite hacer una union de dos listas

#ahora para pasarlo a forma de diccionbario se hace de lasiguiente manera
new_dict = {name: age for (name, age) in zip(names, ages)}# esto lo que hace es que permite juntar dos listas en uno solo formando un diccionario
print(new_dict)

