print ('hola')

suma = lambda x,y: x + y 
assert suma(2,2) == 4 
#lo que ayuda el assert es que si no se cumple la condicion que se le pone, se genera un error

print ('hola 2')

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')
  