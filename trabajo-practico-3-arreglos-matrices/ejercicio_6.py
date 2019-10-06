# -*- coding: utf-8 -*-

import numpy as np

# Ejercicio 6 #
'''Desarrollar una función que elimine el elemento que ocupa una determinada posición
de un arreglo de enteros. Al eliminar se debe mantener la continuidad, es decir, los
elementos a la derecha del eliminado, deben desplazarse a la izquierda un lugar.'''

def eliminarPosicion(arr, pos):
    arr[pos] = 0
    for index in range(pos + 1, len(arr)):
        aux = arr[index]
        arr[index] = arr[index - 1]
        arr[index - 1] =  aux

vector = np.array([1,2,3,4,5,6,7,8])
print(vector)

eliminarPosicion(vector, 5)
print(vector)

'''Desarrollar una función que elimine la primera aparición de un elemento determinado
de un arreglo de enteros. IMPLEMENTARLO CON WHILE '''

def primerAparicion(arr, e):
    pos = 0
    while arr[pos] != e:
        pos += 1
    #arr[pos] = 0
    eliminarPosicion(arr, pos)
        
array = np.array([1, 2, 3, 4, 5, 6, 8, 5, 2])
print(array)

primerAparicion(array, 5)
print(array)            

'''Desarrollar una función que elimine todas las apariciones de un determinado
elemento de un arreglo de enteros.'''

def eliminarTodos(arr, e):
    for i in range(len(arr)):
        if arr[i] == e:
            eliminarPosicion(arr, i)

vectorsin = np.array([1, 2, 3, 4, 1, 1, 8])
print(vectorsin)

eliminarTodos(vectorsin, 1)
print(vectorsin)