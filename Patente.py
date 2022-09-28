#verificar que la sentencia este correcta. en numeros y letras.
print ("los formatos validos de patentes son: ")
print ("Ej XYZ123 auto primera generacion")
patente = input('Ingrese la patente, por favor: ')
 
# XYZ 123 auto
# 123 ZYZ moto
# patenteautov2 = ("xx123xx")
# patentemotov2 = ('x123xyz')
 
letras_validas = "abcdefghijk"  # completar
 
if len(patente) == 6:
    primeraparte = patente[0:3]
    segundaparte = patente[3:6]
    print('imprime la primera parte de la patente ',primeraparte)
    print("imprime la segunda parte de la patente ",segundaparte)
    if primeraparte.isdecimal():
        if (segundaparte[0] in letras_validas and
            segundaparte[1] in letras_validas and
            segundaparte[2] in letras_validas):
            print('es una moto y la matricula es ',patente)
        else:
            print("Patente de moto inválida.")
    else:
        if (primeraparte[0] in letras_validas and
            primeraparte[1] in letras_validas and
            primeraparte[2] in letras_validas):
            print('es un auto y la matricula es ',patente) 
        else:
            print("Patente de auto inválida.")
elif len(patente) == 7:
    print("La patente es de 7 caracteres")
    terceraparte = patente[2:5]
    cuartaparte = patente[1:4]
    print('imprime',terceraparte)
    print("imprime",cuartaparte)
    if cuartaparte.isdecimal():
        print ("ees una moto y la matricula es ",patente)
    else:
        print ("es un auto y la matricula es ",patente)
else:
    print("Error no es una patente valida, es un avion :P" )