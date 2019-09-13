#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

from funciones import llenarArray

# Ejercicio 3 #
'''Crear un programa que lea por teclado N números enteros y los desplace una
posición hacia la derecha: el primero pasa a ser el segundo, el segundo pasa a ser el
tercero y así sucesivamente. El último pasa a ser el primero. Guardar los numeros
ingresados en un arreglo en el orden original y luego correrlos dentro del mismo
arreglo. Mostrarlos antes y despues por pantalla.'''

def desplazarHaciaDerecha(arr):
    aux = arr[0]
    for index in range(1, len(arr)):
        aux2 = arr[index]
        arr[index] = aux
        aux = aux2
    arr[0] = aux

def desplazarHaciaDerecha_(arr):
    aux = arr[len(arr) - 1]
    for index in range(len(arr) - 1, 0, -1):
        arr[index] = arr[index - 1]
    arr[0] = aux
    
cantidad = int(input("¿Cuántos números quiere ingresar? "))
vector = np.zeros(shape = (cantidad), dtype = int)

llenarArray(vector)
print(vector)

desplazarHaciaDerecha(vector)
print(vector)



