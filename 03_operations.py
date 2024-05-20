set_a = {'col', ' mex', 'bol'}
set_b = {'pe', 'bol'}

# union
set_c = set_a.union(set_b) #opcion 1
print(set_c)
print(set_a |set_b)# opcion 2

#intercection
set_c = set_a.intersection(set_b) #opcion 1
print(set_c)
print(set_a & set_b) #opcion 2

#differece
set_c = set_a.difference(set_b) #opcion 1
print(set_c)
print(set_a - set_b) #opcion 2

#symmetric_difference
set_c = set_a.symmetric_difference(set_b) #opcion 1
print(set_c)
print(set_a ^ set_b) #opcion 2