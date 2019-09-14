# -*- coding: utf-8 -*-

import numpy as np

vector = np.array([1, 4, 5, 8, 9])

def binSearch(vector, inicio, final, dato):
    res = False
    centro = (inicio + final) // 2
    if vector[centro] == dato:
        res = True
    elif inicio < final:
        if dato < vector[centro]:
            res = binSearch(vector, inicio, centro - 1, dato)
        elif dato > vector[centro]:
            res = binSearch(vector, centro + 1, final, dato)
    return res

print(binSearch(vector, 0, len(vector) - 1, 2))

def insertSort(arr):
    for pos in range(1, len(arr)):
        posAux = pos
        while posAux > 0 and arr[posAux] < arr[posAux - 1]:
            aux = arr[posAux - 1]
            arr[posAux - 1] = arr[posAux]
            arr[posAux] = aux
            posAux = posAux - 1
            
vectorsin = np.array([12, 8, 7, 4, 3, 1, 2])

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
            