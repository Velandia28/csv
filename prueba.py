import csv
data=[
    ['nombre','edad','mes'],
    ['estiven',25,'abril'],
    ['juanes',63,'diciembre'],
    ['julian',14,'agosto']
]

nombre_arhivo='generar_excel.csv'

with open(nombre_arhivo, mode='w', newline='') as file :
    escritorcsv= csv.writer(file, delimiter=',')
    for fila in data:
        escritorcsv.writerow(fila)

print("Archivo csv se creo correctamente.")

nuevos_datos=[
['erika',22,'abril'],
['emiliano',5,'septiembre'],
['cesar',34,'junio'],
['sebas',24,'enero']
]

with open(nombre_arhivo,mode='a', newline='')as file:
    escritorcsv=csv.writer(file, delimiter=',')
    for fila in nuevos_datos:
        escritorcsv.writerow (fila)

print("Se actualizo con exito el CSV")

