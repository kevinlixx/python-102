import sys #el modulo sys el cual nos permite acceder a las variables de entorno del sistema operativo
print(sys.path)

import re #el modulo re nos permite utilizar expresiones regulares 

text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte es 3'
result = re.findall('[0-9]+', text)#el re findall ayuda a buscar un patron de texto dentro de un string
print(result)

import time #el modulo time n
os permite manejar fechas y horas

timestamp = time.time()
print(timestamp) #formato unix

local= time.localtime()
result = time.asctime(local) #el asctime nos permite convertir una fecha de formato unix a una fecha legible
print(result)

import collections #el modulo collections nos permite manejar listas
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers) #el counter nos permite contar la frecuencia de un elemento en una lista
print(counter)
