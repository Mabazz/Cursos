# modo (segundo argumento)
# "r" (read)  --  modo lectura
# "w" (write) --  modo escritura (si el archivo no existe, se crea automáticamente)

f = open("noexiste.txt", "w", encoding="utf8")
 
# No puedo: lo abrí como escritura.
# print(f.read())
 
f.write("Hola desde el programa de Python")
 
f.close()