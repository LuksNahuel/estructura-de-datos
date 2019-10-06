# -*- coding: utf-8 -*-

#EJERCICIO 11

'''Desarrollar una función para que, dada una matriz cuadrada de reales de orden N,
obtenga la sumatoria de los elementos que están por encima de la diagonal principal
(excluida ésta).'''


def imprimirTraza(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if fila == columna:
                print(matriz[fila][columna])
                
def sumaSobreDiagonal(matriz):
    total = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if fila != columna and not fila > columna:
                total += matriz[fila][columna]
    return total


def llenarMatriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            data = int(input("Dame el número a ser ingresado en la posición %s, %s: " % (fila, columna)))
            matriz[fila][columna] = data
            
import numpy as np

matriz = np.zeros(shape = (3, 3), dtype = int)