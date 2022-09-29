
# Resuelto en clase

origen = input("Ingrese el archivo de origen: ")
destino = input("Ingrese el archivo de destino: ")

print("Copiando los datos de", origen, "a", destino, "...")

f = open(origen)
contenido = f.read()
f.close()

f = open(destino, "w")
f.write(contenido)
f.close()

print("¡Datos copiados!")



# Método 1: sin importar y sin loops

origen = input("Ingrese el archivo de origen: ")
destino = input("Ingrese el archivo de destino: ")

archivo_origen = open(origen)
archivo_destino = open(destino, "w")

archivo_destino.write(archivo_origen.read())

archivo_origen.close()
archivo_destino.close()

print(f"Copiando los datos de {origen} a {destino} ...")
print("¡Datos copiados!")



# Método 2: importando shutil

import shutil

origen = input("Ingrese el archivo de origen: ")
destino = input("Ingrese el archivo de destino: ")

shutil.copyfile(origen, destino)    # Encontré esto (follow_symlinks=True) que suena a que si sabes usarlo sos pro.

print(f"Copiando los datos de {origen} a {destino} ...")
print("¡Datos copiados!")



# Método 3: usando loop 'for'

origen = input("Ingrese el archivo de origen: ")
destino = input("Ingrese el archivo de destino: ")

archivo_origen = open(origen)
archivo_destino = open(destino, "w")

for line in archivo_origen:
    archivo_destino.write(line)

archivo_origen.close()
archivo_destino.close()

print(f"Copiando los datos de {origen} a {destino} ...")
print("¡Datos copiados!")