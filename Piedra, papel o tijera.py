#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Ej Difícil:
"""
Script que simula el juego de piedra, papel o tijera. Juega un usuario
contra la computadora. Primero, se debe pedir la cantidad de rondas del 
juego. Tras terminarlas, se debe indicar el score final y el ganador.
Se puede usar random.choices() para elegir un elemento al azar dentro
de una lista
"""
   
def menu():
    return """
    Menu de opciones:
    1. Jugar contra la PC
    2. Salir

    """
    
def ingresar_rondas():
    while True:
        rondas = input("\nIngrese la cantidad de rondas: ")
        if rondas.isdigit() and int(rondas) > 0:
            rondas = int(rondas)
            return rondas
        else:
            print("\n\t\tError en el ingreso de la cantidad de rondas")
    
def jugar(rondas):
    import random
    pts_usuario = 0
    pts_compu = 0
    opciones = ["piedra","papel","tijera"]
    
    for ronda in range(rondas):
        print(f"\nRonda {ronda+1}")
        while True:
            opc_usuario = input("\nSeleccione su opción (piedra, papel o tijera): ")
            if opc_usuario.lower() in opciones:
                break
            else:
                print("Opción incorrecta")
        opc_compu = random.choice(opciones)
        print(f"\nPC eligió {opc_compu}")
        
        gana_usuario = (opc_usuario == "papel" and opc_compu == "piedra") or \
              (opc_usuario == "tijera" and opc_compu == "papel") or \
              (opc_usuario == "piedra" and opc_compu == "tijera")
        
        
        if opc_compu == opc_usuario:
            pts_usuario += 0  # pts_usuario = pts_usuario + 1
            pts_compu += 0
            print("Ronda empatada")
    
                          
        elif gana_usuario:
            pts_usuario += 1
            print("Ronda ganada por: usuario")
            
        else:
            pts_compu += 1
            print("Ronda ganada por: PC")
                  
    return f"Score final: Usuario {pts_usuario} - PC {pts_compu}"
  
 
######## main ##############
print("""
    Piedra, papel o tijera
    ======================    
""")
while True:
    print(menu())
    opcion = input("Elija su opción: ")
    
    if opcion == "1":
        rondas = ingresar_rondas()
        print(jugar(rondas))
        
    elif opcion == "2":
        print("\n\t\tGracias por jugar con nosotros...")
        break
        
    else:
        print("Opción incorrecta...")