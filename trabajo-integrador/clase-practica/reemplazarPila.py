#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:30:50 2019

@author: estruc-datos
"""
import stack

'''Escribir una funcion "reemplazar", que tiene como argumentos una pila de enteros y dos numeros enteros:
    "nuevo" y "viejo". La función debe tomar la pila que recibe por parametros y reemplazar cada ocurrencia del numero "viejo"
    por "nuevo". La funcion no debe retornar una nueva pila, sino que debe modificar la pila que recibe como parametro.
    Para escribir la funcion, se puede utilizar solo una estrcutura de datos auxiliar y se debe utilizar el TDA "Pila", 
    que posee las siguientes operaciones: apilar, desapilar, tope, estaVacia, estaLlena, tamanio, capacidad, clonar e invertir'''
    
def reemplazar(pila, viejo, nuevo):
    
    pilaAux = stack.Stack(pila.getSize(), pila.dtype())
    
    while(not pila.isEmpty()):
        dato = pila.pop()
        if dato == viejo:
            dato = nuevo
        pilaAux.push(dato)
    
    while(not pilaAux.isEmpty()):
        pila.push(pilaAux.pop())
    
pilaPrueba = stack.Stack(4)

pilaPrueba.push(1)
pilaPrueba.push(2)
pilaPrueba.push(3)
pilaPrueba.push(4)

reemplazar(pilaPrueba, 1, 7)