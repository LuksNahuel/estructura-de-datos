#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import listaRec
import ABB

def randomChar():
    return chr(random.randrange(97, 97 + 26))

def listaLaberinto(cantidadPasos, inicio, final):
    lista = listaRec.Lista()
    pasos = 0    
    lista.append(inicio)    
    while pasos < cantidadPasos:
        char = randomChar()
        if lista.search(char) == 0 and char != final:
            lista.append(char)
            pasos += 1    
    lista.append(final)    
    return lista

def llenarLaberinto(lista):
    arbol = ABB.ABB()    
    for i in range(lista.size()):
        arbol.insert(lista.getDato(i))    
    return arbol

def juegoLaberinto(pasos, inicio, cielo):
    lista = listaLaberinto(pasos, inicio, cielo)
    laberinto = llenarLaberinto(lista)
    
    actual = laberinto.root
    finalDelJuego = False
    
    while not finalDelJuego:
        if not actual.isLeaf():
            respuesta = input("¿Para dónde quiere mover? (i/d) ")
            if respuesta == 'i':
                if actual.hasLeft():
                    actual = actual.left
                else:
                    print("Sólo podes moverte a la derecha.")
            elif respuesta == 'd':
                if actual.hasRight():
                    actual = actual.right
                else:
                    print("Sólo podes moverte a la izquierda.")
            else:
                print("Ingresa un caracter válido.")
        else:
            if actual.data == cielo:
                print("Llegaste al cielo.")
            else:
                print("Llegaste al infierno.")
                
            print("El cielo era:", cielo)
            finalDelJuego = True
    
    laberinto.treePlot("juego")
    
            
juegoLaberinto(5, randomChar(), randomChar())