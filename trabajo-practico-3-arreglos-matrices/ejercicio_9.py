# -*- coding: utf-8 -*-
import numpy as np

# EJERCICIO 9 
# Crear y cargar dos matrices de tamaño 3x3, sumarlas y mostrar su suma.

matrizA = np.zeros(shape = (3,3), dtype = int)
matrizB = np.zeros(shape = (3,3), dtype = int)

def llenarMatriz(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            data = int(input("Dame el número a ser ingresado en la posición %s, %s: " % (fila, columna)))
            matriz[fila][columna] = data

def sumarMatriz(matriz):
    total = 0
    for fila in matriz:
        for value in fila:
            total += value
    return total

def matrizSuma(matriz):
    total = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            total += matriz[fila][columna]
    return total

def sumaDeMatrices(m1, m2):
    mAux = np.zeros(shape=(len(m1), len(m1[0])), dtype = m1.dtype)
    for fila in range(len(mAux)):
        for columna in range(len(mAux[0])):
            suma = m1[fila][columna] + m2[fila][columna]
            mAux[fila][columna] = suma
    return mAux





if __name__ == "__main__":    
    print("Llenar la primer matriz")
    llenarMatriz(matrizA)
    print(matrizA)
    
    print("Llenar la segunda matriz")
    llenarMatriz(matrizB)
    print(matrizB)

