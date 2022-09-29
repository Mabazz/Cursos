
origen = input("Ingrese el archivo de origen: ")
destino = input("Ingrese el archivo de destino: ")

print("Copiando los datos de", origen, "a", destino, "...")

f = open(origen, "rb")
contenido = f.read()
f.close()

f = open(destino, "wb")
f.write(contenido)
f.close()

print("¡Datos copiados!")