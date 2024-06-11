import csv

datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Juan', 25, 'Madrid'],
    ['Maria', 30, 'Barcelona'],
    ['Luis', 28, 'Sevilla']
]

# Nombre del archivo CSV que queremos crear
nombre_archivo = 'datos.csv'

# Abre el archivo en modo escritura ('w', de write) y crea un objeto escritor de CSV
with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    escritor_csv= csv.writer(archivo_csv, delimiter=',')
    
    # Escribe los datos en el archivo CSV fila por fila
    for fila in datos:
        escritor_csv.writerow(fila)

print("Archivo CSV creado exitosamente.")