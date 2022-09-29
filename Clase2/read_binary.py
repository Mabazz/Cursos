# modo (segundo argumento)
#   "r" (read)  --  modo lectura
#   "w" (write) --  modo escritura (si el archivo no existe, se crea automáticamente)
#   "a" (append)--  modo escritura al final de lo escrito

# para archivos que no contienen texto plano (no tiene relevancia el encode)
#   "rb" (read binary)
#   "wb" (write binary)
#   "ab" (append binary)

f = open("origen.txt", "r")
# El argumento de read() es la cantidad de bytes que quiero leer.
contenido = f.read(1024*1024*100)
print(contenido)
contenido = f.read(5)
print(contenido)
contenido = f.read(5)
print(contenido)
contenido = f.read(5)
print(contenido)
contenido = f.read(5)
print(contenido == "")
f.close()