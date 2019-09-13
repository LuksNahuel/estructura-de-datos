# -*- coding: utf-8 -*-
import numpy as np

# Ejercicio 4 #
'''Desarrollar una función que inserte un elemento en un arreglo de enteros, dada la
posición de inserción, al insertar un elemento en una posición, se produce un
desplazamiento a la derecha, si el arreglo estaba lleno, el ultimo elemento se pierde.'''

def insertarElementoEnArreglo(arr, pos, e):
    aux = arr[pos]
    arr[pos] = e
    for index in range(pos + 1, len(arr)):
        aux2 = arr[index]
        arr[index] = aux
        aux = aux2
        
vector = np.array([1, 2, 3, 4, 5, 6, 7])
print(vector)

insertarElementoEnArreglo(vector, 0, 8)
print(vector)

