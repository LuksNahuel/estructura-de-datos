# -*- coding: utf-8 -*-
import numpy as np
# EJERCICIO 10
'''Crear una matriz de tamaño 5x5 y rellenarla de la siguiente forma: la posición M[n,m]
debe contener n+m. Después se debe mostrar su contenido.'''

matriz = np.zeros(shape=(5,5), dtype = int)

def rellenarMatriz(m):
    for fila in range(len(m)):
        for columna in range(len(m[0])):
            m[fila][columna] = fila + columna

rellenarMatriz(matriz)
print(matriz)