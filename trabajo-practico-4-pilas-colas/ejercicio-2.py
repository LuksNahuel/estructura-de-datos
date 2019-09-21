#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:44:13 2019

@author: estruc-datos
"""

import stack 

'''Realizar un programa que muestre la cantidad de elementos de una pila de enteros.
Mostrar y desapilar 2 elementos y volver a imprimir el tamaño de la pila.'''

pila = stack.Stack(4)
pila.push(2)
pila.push(4)
pila.push(6)
pila.push(8)

pila.imprimir()
print("La pila tiene", pila.getSize(), "elementos")
print("Desapilamos los elementos", pila.pop(), "y", pila.pop())
print("El nuevo tamaño es", pila.getSize())