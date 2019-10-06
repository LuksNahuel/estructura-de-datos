# -*- coding: utf-8 -*-

# EJERCICIO 12
'''Desarrollar una función para que, dada una matriz cuadrada de enteros de orden N,
obtenga la traza de la misma (sumatoria de los elementos de la diagonal principal). Lo
mismo pero con la diagonal secundaria. Ambas funciones debes ser recursivas.'''

import numpy as np

def traza(matriz, fila = 0, columna = 0):
    total = 0
    if fila == len(matriz) - 1 and columna == len(matriz[0]) - 1:
        total = matriz[fila][columna]
    else:
        total = matriz[fila][columna] + traza(matriz, fila + 1, columna + 1)
    return total

def diagonalSecundaria(matriz, fila, columna):
    total = 0
    if fila == len(matriz) - 1 and columna == 0:
        total = matriz[fila][columna]
    else:
        total = matriz[fila][columna] + diagonalSecundaria(matriz, fila + 1, columna - 1)
    return total

matriz = np.array([[1, 4, 2, 8], [2, 3, 1, 2], [2, 3, 1, 4], [2, 2, 3, 7]])

print(diagonalSecundaria(matriz, 0, len(matriz) - 1))