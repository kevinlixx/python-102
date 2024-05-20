import random
countries = ['col', 'mex', 'bol', 'per']  

population_v2 = { country:random.randint(1,100) for country in countries}
print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population > 50}
print(result) #lo que hace esto es que solo devuelve los paises que tienen mas de 50 habitantes

text = ' Hola soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou'} # lo que esto es que devuelve solo las vocales de un texto en mayusculas
print(unique)