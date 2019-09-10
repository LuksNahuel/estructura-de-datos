#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import funciones as fn

# Ejercicio 1 #

cantidad = int(input("¿Cuántos números quiere ingresar? "))
vector = np.zeros(shape = (cantidad), dtype = int)

fn.llenarArray(vector)
fn.imprimirVectorAlReves(vector)

print("La suma del vector es ", fn.sumaElementosArray(vector))
print("El promedio del vector es ", fn.promedioArray(vector))