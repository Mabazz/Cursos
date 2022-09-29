
# Resuelto en clase

origen = input("Ingrese el archivo de origen: ")
destino = input("Ingrese el archivo de destino: ")

print("Copiando los datos de", origen, "a", destino, "...")

f = open(origen, "rb")
while 1:
    contenido = f.read()
    if not contenido:
        break
    print(contenido)
# with open(origen, "rb") as f:
#     for contenido in f:
#         print(contenido)
f.close()

f = open(destino, "wb")
f.write(contenido)
f.close()

print("¡Datos copiados!")