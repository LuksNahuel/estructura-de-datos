#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NodeList:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)
    
class List:
    def __init__(self):
        self.head = None

    def __repr__(self):
        cadena = ""
        if self.isEmpty():
            cadena = "La lista está vacía."
        else:
            aux = self.head
            while aux != None:
                cadena = cadena + str(aux.data) + " -> "
                aux = aux.next
            cadena = cadena + "["
        return cadena
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        size = 0
        aux = self.head
        while aux != None:
            size += 1
            aux = aux.next
        return size
    
    def getElement(self, pos):
        node = None
        if not self.isEmpty() and pos < self.size():
            aux = self.head
            posAux = 0
            while posAux < pos:
                aux = aux.next
                posAux += 1
            node = aux
        else:
            raise Exception("La posición no existe.")
        return node
    
    def append(self, data = None):
        self.insert(self.size(), data)
    
    def insert(self, pos, data):
        nuevo = NodeList(data)
        if self.isEmpty():
            self.head = nuevo
        else:
            if pos == 0:
                nuevo.next = self.head
                self.head = nuevo
            else:
                aux = self.head
                cont = 0
                while cont < pos - 1 and aux.next != None:
                    aux = aux.next
                    cont += 1
                nuevo.next = aux.next
                aux.next = nuevo
      
    def delete(self, pos):
        if not self.isEmpty() and pos < self.size():
            if pos == 0:
                self.head = self.head.next
#            elif pos == self.size() - 1:
#                aux = self.head
#                while(aux.next != None):
#                    aux = aux.next
#                aux.next = None
            else:
                count = 0
                nodeAfter = self.head
                nodeToKill = self.head
                while(count < pos):
                    count += 1
                    nodeToKill = nodeToKill.next
                count = 0
                while(count < pos - 1): #capturar el nodo en el recorrido del otro
                    count += 1
                    nodeAfter = nodeAfter.next
                nodeAfter.next = nodeToKill.next
        else:
            raise Exception("La posición no existe o la lista está vacía")
        
        
    def replace(self, pos, data):
        count = 0
        nuevo = NodeList(data)
        if(pos == 0):
            nuevo.next = self.head.next
            self.head = nuevo
        else:
            nodeAfter = self.head
            nodeToReplace = self.head
            while(count < pos):
                count += 1
                nodeToReplace = nodeToReplace.next
            count = 0
            while(count < pos - 1):
                count += 1
                nodeAfter = nodeAfter.next
            nuevo.next = nodeToReplace.next
            nodeAfter.next = nuevo
            
    def clone(self):
        nueva_lista = List()
        aux = self.head
        while(aux != None):
            nueva_lista.append(aux)
            aux = aux.next
        return nueva_lista

    def interchangeFirstOnes(self):
        if(self.size() >= 2): 
            first = self.head
            second = self.head.next
            first.next = second.next
            second.next = self.head
            self.head = second
        else:
            raise Exception("No hay elementos suficientes.")
    
    def expand(self, linked_list):
        if(not linked_list.isEmpty()):
            aux = linked_list.head
            while(aux != None):
                self.append(aux)
                aux = aux.next
        else:
            raise Exception("La lista pasada por parámetros está vacía.")
    
    def ocurrenceOf(self, data):
        count = 0
        aux = self.head
        while(aux != None):
            if(aux.data == data):
                count += 1   
            aux = aux.next
        return count