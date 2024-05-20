with open('./text.txt', 'r+') as file: #con esta sintaxis no necesitamos cerrar el programa ya que se cierra automaticamente
  for line in file: #nos ayuda a ahorrar espacio en memoria
    print(line)
  file.write('Nuevas cosas en este archivo\n')

#con los permisos r+ podemos leer y escribir en el archivo
#con los permisos w+ podemos leer y sobreescribir en el archivo