#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

from funciones import llenarArray

def desplazarHaciaDerecha(arr):
    aux = arr[0]
    for index in range(1, len(arr)):
        aux2 = arr[index]
        arr[index] = aux
        aux = aux2
    arr[0] = aux

cantidad = int(input("¿Cuántos números quiere ingresar? "))
vector = np.zeros(shape = (cantidad), dtype = int)

llenarArray(vector)
print(vector)

desplazarHaciaDerecha(vector)
print(vector)



