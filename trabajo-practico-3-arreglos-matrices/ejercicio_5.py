# -*- coding: utf-8 -*-

import numpy as np
import ejercicio_4 as ej4

# Ejercicio 5 #
'''Desarrollar una función que inserte un elemento en un arreglo de enteros ordenado
en forma ascendente, de forma de no alterar el orden.'''

vector = np.array([1, 3, 5, 8])

def sortArrInsert(arr, e):
    pos = 0
    while arr[pos] <= e:
        pos += 1
    ej4.insertarElementoEnArreglo(arr, pos, e)