#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

# Ejercicio 1 #
'''En un edificio alto, las cucarachas se van distribuyendo por pisos de esta forma: en
    el primer piso hay una cucaracha, en los pisos pares el doble del número de piso (p.ej.
    en el piso 8 hay 16 cucarachas), en el resto hay la suma de las cucarachas de los dos
    pisos anteriores.
    Desarrollar un algoritmo que permita determinar la cantidad total de cucarachas en un
    edificio que tiene N pisos.
    Utilizar Recursividad.'''

def cucarachasPorPiso(piso):
    cucarachas = 0
    if piso == 1:
        cucarachas = 1
    elif piso % 2 == 0:
        cucarachas = 2 * piso
    else:
        cucarachas = cucarachasPorPiso(piso-1) + cucarachasPorPiso(piso-2)
    return cucarachas

def cucarachasEnEdificio(cantidadDePisos):
    cantidad = 0
    if cantidadDePisos == 1:
        cantidad = 1
    else:
        cantidad = cucarachasPorPiso(cantidadDePisos) + cucarachasEnEdificio(cantidadDePisos - 1)
    return cantidad

# Ejercicio 2 #
'''Se quiere implementar una función: distribucion(cadena):
La misma devuelve un vector de pares con un TAD de dos partes:
-Letra
-Ocurrencia
Es decir, para cada letra de la cadena, se guarda la cantidad de veces que aparece.'''

class Letras():
    def __init__(self, letra = None, ocurrencia = 0):
        self.letra = letra
        self.ocurrencia = ocurrencia
    def getLetra(self):
        return self.letra
    def getOcurrencia(self):
        return self.ocurrencia
    
def distribucion(cadena):
    vector = np.empty(shape=len(cadena), dtype=Letras)
    pos = 0
    for i in range(len(cadena)):
        if not estaEnVector(vector, cadena[i]):
            suma = 0
            for j in range(len(cadena)):
                if cadena[i] == cadena[j]:
                    suma += 1
            vector[pos] = Letras(cadena[i], suma)
            suma = 0
            pos += 1
    return vector

def estaEnVector(vector, char):
    estado = False
    for i in range(len(vector)):
        if vector[i] != None:
            if vector[i].getLetra() == char:
                estado = True
    return estado

# Ejercicio 3 #
    
def esCreciente(vector):
    salida = True
    for i in range(len(vector) - 1):
        if vector[i] > vector[i+1]:
            salida = False
    return salida

def esDecreciente(vector):
    salida = True
    for i in range(len(vector) - 1):
        if vector[i] < vector[i+1]:
            salida = False
    return salida

v = np.array([4, 3, 2])
print(esDecreciente(v))