# -*- coding: utf-8 -*-

'''Escribir un programa que pida por teclado una lista de N numeros y los imprima en
forma inversa, es decir, que muestre por pantalla, al finalizar en ingreso de los N
numeros, desde el ultimo hasta el primero. Implementarlo con una funcion recursiva.'''

cantidad = int(input("Ingrese una cantidad de números a ingresar: "))

def imprimirAlReves(cantidad):    
    if cantidad != 0:
        numero = int(input("Dame un número: "))
        imprimirAlReves(cantidad - 1)
        print(numero)


imprimirAlReves(cantidad)