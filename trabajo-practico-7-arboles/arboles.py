#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NodoArbol:
    def __init__(self, dato = None):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
        
    def preOrder(self):
        print(self.dato)
        if self.tieneIzquierdo():
            self.izquierdo.preOrder()
        if self.tieneDerecho():
            self.derecho.preOrder()
            
    def inOrder(self):
        if self.tieneIzquierdo():
            self.izquierdo.inOrder()
        print(self.dato)
        if self.tieneDerecho():
            self.derecho.inOrder()
    
    def postOrder(self):
        if self.tieneIzquierdo():
            self.izquierdo.postOrder()
        if self.tieneDerecho():
            self.derecho.postOrder()
        print(self.dato)
    
    def insertar(self, nodo):
        if nodo.dato < self.dato:
            if self.tieneIzquierdo():
                self.izquierdo.insertar(nodo)
            else:
                self.izquierdo = nodo
        elif nodo.dato > self.dato:
            if self.tieneDerecho():
                self.derecho.insertar(nodo)
            else:
                self.derecho = nodo
        else:
            print("Dato existente.")
            
    def grado(self):
        if self.esHoja():
            return 0
        else:
            if self.tieneDerecho() and self.tieneIzquierdo():
                return 2
            else:
                return 1
    
    def esHoja(self):
        return self.izquierdo == None and self.derecho == None
            
    def tieneIzquierdo(self):
        return self.izquierdo != None

    def tieneDerecho(self):
        return self.derecho != None

class ArbolBB:
    def __init__(self):
        self.raiz = None
        
    def insertar(self, dato):
        nuevo = NodoArbol(dato)
        if self.isEmpty():
            self.raiz = nuevo
        else:
            self.raiz.insertar(nuevo)
    
    def preOrder(self):
        if not self.isEmpty():
            self.raiz.preOrder()
    
    def inOrder(self):
        if not self.isEmpty():
            self.raiz.inOrder()
            
    def vaciar(self):
        self.raiz = None
    
    def postOrder(self):
        if not self.isEmpty():
            self.raiz.postOrder()
    
    def isEmpty(self):
        return self.raiz == None
        

