#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Resuelva el calculo de la suma de dos numeros enteros de muchos digitos (N digitos), haciendo uso de dos pilas
en las que almacena solo los digitos. Tenga en cuenta que debe utilizar una tercera pila en la que ira cargando los resultados parciales.
Definir el tamaño de la pila resultado, al sumar, como maximo en la pila resultante le queda de tamaño N+1 y suponer que se posee implementado
el TDA Pila, con las operaciones: push, pop, top, invertir, etc.'''

import stack 

numN = stack.Stack(4)
numM = stack.Stack(4)

def sumaDePilas(n, m):
    res = stack.Stack(n.getSize(), n.dtype())
    auxN = n.clone()
    auxM = m.clone()
    carry = 0
    while not auxN.isEmpty():
       numero = auxN.pop() + auxM.pop() + carry
       res.push(numero % 10)
       carry = numero // 10
    
    res.push(carry)
    
    return res.invertir()
    

numN.push(1)
numN.push(2)
numN.push(3)
numN.push(4)

numM.push(1)
numM.push(2)
numM.push(3)
numM.push(4)

suma = sumaDePilas(numN, numM)

print(suma)