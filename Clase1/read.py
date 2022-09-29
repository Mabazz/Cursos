import os

# Directorio actual de trabajo o Current working directory (cwd)
print(os.getcwd())

    # Ejemplo >>> C:\Users\marti\Documents\educacionit\Curso\Clase1



# ----- Entrada y salida de archivos: File I/O (Input/Output) ----- 
 
# Función open() (abrir)
# Abrir = adquiere el archivo.
# Leer  = carga el contenido de un archivo en una variable.
 
# Abre el archivo con el programa predeterminado.
os.startfile("hola.txt")
 
# Adquiere el archivo para poder leerlo.
f = open("read.txt", "r", encoding="utf8")

print(f)

contenido = f.read()

print(contenido)

# Librera el archivo.
f.close() 