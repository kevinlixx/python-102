for i in range(1,11):
  print(i)
# un iterable es un objeto que puede ser iterado, es decir, que puede ser recorrido.
my_iter = iter(range(1,4)) #iterador
print(my_iter)
print(next(my_iter)) #esto l oque permite es que el iterador se va actualizando manualmente es decir por cada next se va obteniendo el siguiente valor 