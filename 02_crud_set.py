set_countries = {"col", "mex", "bol"}

#tamaño del conjunto
size = len(set_countries)
print(size)

#para comprobar si esta en un conjunto
print('col' in set_countries)
print('pe' in set_countries)

#añadir elementos
set_countries.add('pe') ##agrega a peru
print(set_countries)

# update  añade varios elementos
set_countries.update({'arg', 'ecua'})
print(set_countries)

#remove

set_countries.remove('col')
print(set_countries)

#discard lo que hace es que si no esta en el conjunto no lo elimina y el codigo continua
set_countries.discard('arg')
print(set_countries)

#clear -> remove all 
set_countries.clear()
print(set_countries)
print(len(set_countries))
