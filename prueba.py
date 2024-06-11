#crear csv e ingrsar una lista de parametros
# import csv
# data=[
#     ['nombre','edad','mes'],
#     ['estiven',25,'abril'],
#     ['juanes',63,'diciembre'],
#     ['julian',14,'agosto']
# ]

# nombre_arhivo='generar_excel.csv'

# with open(nombre_arhivo, mode='w', newline='') as file :
#     escritorcsv= csv.writer(file, delimiter=',')
#     for fila in data:
#         escritorcsv.writerow(fila)

# print("Archivo csv se creo correctamente.")
#para ingresar nuevas filas en csv 

# nuevos_datos=[ 
# ['erika',22,'abril'],
# ['emiliano',5,'septiembre'],
# ['cesar',34,'junio'],
# ['sebas',24,'enero']
# ]

# with open(nombre_arhivo,mode='a', newline='')as file:
#     escritorcsv=csv.writer(file, delimiter=',')
#     for fila in nuevos_datos:
#         escritorcsv.writerow (fila)

# print("Se actualizo con exito el CSV")

#para crear json y ingresarle un  diccionario
import json
 
datos={
  "nombre": "julian",
  "edad": 20,
  "mes": "mayo"
}
nombre_arhivo = "datos.json"

with open(nombre_arhivo,"w") as archivo:
    json.dump(datos,archivo, indent=4)

# valores = list(datos.values())
# cadena_json= json.dumps(valores,indent=4)

print("Archivo JSON ha sido creado con exito ")
with open(nombre_arhivo,"r") as archivo:
    datos=json.load(archivo)
#actualizar en json agregando una nueva llave:valor
datos ["perro"]=("luks")

with open(nombre_arhivo, "w") as archivo:
    json.dump(datos,archivo, indent=4)

print("Archivo JSON ha sido actualizado con exito: ", nombre_arhivo)



