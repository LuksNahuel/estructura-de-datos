# -*- coding: utf-8 -*-
def llenarArray(arr):
    for i in range(len(arr)):
        num = int(input("Dame un número para ingresar: "))
        arr[i] = num    

def imprimirVectorAlReves(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])

def sumaElementosArray(arr):
    suma = 0
    for i in range(len(arr)):
        suma += arr[i]
    return suma

def promedioArray(arr):
    return sumaElementosArray(arr)/len(arr)
