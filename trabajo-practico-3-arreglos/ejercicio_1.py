#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import funciones as fn

# Ejercicio 1 #
'''Escribir un programa que le pida al usuario que ingrese N números naturales (primero
uno, luego otro, y así hasta que el usuario ingrese N numeros). Al final, el programa
debe imprimir los números que fueron ingresados en orden inverso, la suma total de
los valores y el promedio.'''

cantidad = int(input("¿Cuántos números quiere ingresar? "))
vector = np.zeros(shape = (cantidad), dtype = int)

fn.llenarArray(vector)
fn.imprimirVectorAlReves(vector)

print("La suma del vector es ", fn.sumaElementosArray(vector))
print("El promedio del vector es ", fn.promedioArray(vector))