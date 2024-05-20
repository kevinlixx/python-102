file = open('./text.txt')

# print(file.read()) #lee todo el archivo
# print(file.readline()) #lee linea por linea


#file.close()#cierra el archivo y si limpia la memoria

with open('./text.txt') as file: #con esta sintaxis no necesitamos cerrar el programa ya que se cierra automaticamente
  for line in file: #nos ayuda a ahorrar espacio en memoria
    print(line)