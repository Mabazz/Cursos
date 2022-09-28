import statistics
 
# notas = [9, 5, 3, 7.5, 2, 8.6, 6, 4.5, 1]
notas = input("Ingrese las notas separadas por espacios: ")
# El map() convierte a float() cada una de las notas separadas
# por espacios.
notas = map(float, notas.split())
 
notas_aprobadas = []
notas_desaprobadas = []
 
for nota in notas:
    if nota >= 4:
        notas_aprobadas.append(nota)
    else:
        notas_desaprobadas.append(nota)
 
# El asterisco y el sep="\n" es para que aparezcan todas las notas
# en líneas distintas.
print("Notas aprobadas:", *notas_aprobadas, sep="\n")
print("Promedio de aprobadas:", statistics.mean(notas_aprobadas))
print("Notas desaprobadas:", *notas_desaprobadas, sep="\n")
print("Promedio de desaprobadas:", statistics.mean(notas_desaprobadas))

# OTRAS FORMAS:
# Para resolver con for:
 
# El programa tiene que imprimir:
# Notas aprobadas:
# 9
# 5
# 7.5
# 8.6
# 6
# 4.5
# Notas desaprobadas:
# 3
# 2
# 1

# print("Notas aprobadas")
# for nota in notas:
#     if nota >= 4:
#         print(nota)

# print("Valor de nota: ", nota)

# print("Notas desaprobadas")
# for nota in notas:
#     if nota <= 4.0:
#         print(nota)