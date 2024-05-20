#set -> conjunts
#- Se pueden modificar
#- No tienen un orden
#- No pueden tener elementos duplicados

set_countries = {"col", "mex", "bol"}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 443, 23}
print(set_numbers)

set_types = {1, "hola",   False, 12 }
print(set_types)

set_from_string = set{"hoola"}
print(set_from_string)
#lo vuelve un conjunto dividendo cada palabra en un conjunto pero no repite la o

set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3]
set_numbers= set(numbers) #permite solo mostrar los numeros que hay sin necesidad de que se repitan tanto
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
