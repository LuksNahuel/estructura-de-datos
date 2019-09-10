#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

def sumaTotal(vector, pos = 0):
    suma = 0
    if pos == len(vector) - 1:
        suma = vector[pos]
    else:
        suma = vector[pos] + sumaTotal(vector, pos + 1)
    return suma

# Ejercicio 2 #
vectorsin = np.array([1,2,3,4,5])

def productoTotal(vector, pos = 0):
    producto = 0
    if pos == len(vector) - 1:
        producto = vector[pos]
    else:
        producto = vector[pos] * productoTotal(vector, pos + 1)
    return producto

print(productoTotal(vectorsin))