# -*- coding: utf-8 -*-
import ABB

arbol = ABB.ABB()

arbol.insert(25)
arbol.insert(10)
arbol.insert(33)
arbol.insert(5)
arbol.insert(22)
arbol.insert(1)


buscado = arbol.search(54)

maximo = arbol.maximum()

minimo = arbol.minimum()

