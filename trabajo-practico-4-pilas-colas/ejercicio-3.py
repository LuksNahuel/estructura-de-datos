#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Escriba un programa que permita el ingreso de N numeros enteros y los guarde en
una pila. Luego al terminar, muestre por pantalla (al ser desapilados), los numeros
ingresados.'''

import stack

cantidad = int(input("Ingrese la cantidad de enteros que quiere apilar: "))
pila = stack.Stack(cantidad)

while(not pila.isFull()):
    entero = int(input("Ingrese el entero a apilar: "))
    pila.push(entero)

while(not pila.isEmpty()):
    print(pila.pop())