# 3 tipos de instrucciones
#   (1) De memoria
#   (2) Aritméticas y lógicas
#   (3) Que alteran el flujo del código (condicional, bucles)
 
# Dos tipos de bucles:
#   (1) for
#   (2) while
 
cursos = ["Python", "Java", "SQL", "CSS", "JavaScript", "PHP"]
numeros_primos = [2, 3, 5, 7, 11, 13, 17, 23]
 
# print(cursos[0])
# print(cursos[1])
# print(cursos[2])
# print(cursos[3])
 
# 0 ... len(cursos) - 1
# Sintaxis:
# for variable in lista:
#   - lista tiene que ser una lista existente.
#   - variable puede no existir.
# En cada una de las ejecuciones (iteraciones) del bucle
# la variable (en este caso, curso) recibe uno de los 
# elementos de la lista (en el orden en que están en la lista).
for curso in cursos:
    print(curso)
 
for numero_primo in numeros_primos:
    if numero_primo != 11:
        cuadrado = numero_primo ** 2
        print("El cuadrado de", numero_primo, "es", cuadrado)
 
print("Fin de programa.")