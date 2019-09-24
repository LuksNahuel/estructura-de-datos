# -*- coding: utf-8 -*-
import stack

def llenarPila(pila):
    while(not pila.isFull()):
        entero = int(input("Ingrese el entero a apilar: "))
        pila.push(entero)
        
def torresHanoi(n, origen, auxiliar, destino):
  if n == 1:
      destino.push(origen.pop())
  else:
      torresHanoi(n-1, origen, destino, auxiliar)
      destino.push(origen.pop())
      torresHanoi(n-1, auxiliar, origen, destino)



origen = stack.Stack(5)
auxiliar = stack.Stack(5)
destino = stack.Stack(5)

llenarPila(origen)

#torresHanoi(5, origen, auxiliar, destino)      

