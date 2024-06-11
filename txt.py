with open('archivo.txt','w') as archivo:
    archivo.write('hola mundo\n')
    archivo.write('tengo miedo\n')
    archivo.write('voy a filtro\n')

print('datos escritos correctamente en el archivo.txt')

with open('archivo.txt','a') as archivo:
    archivo.write('modificacion\n')
    archivo.write('12345\n')
print('se actualizo con exito el archivo.txt')
