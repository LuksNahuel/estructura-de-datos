 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NodeList:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def mostrar(self):
        print(self.data)
        if self.next != None:
            self.next.mostrar()
    
    def size(self):
        cantidad = 0
        if self.next == None:
            cantidad = 1
        else:
            cantidad = 1 + self.next.size()
        return cantidad
    
    def insert(self, nuevo = None, posInsert = 0, posAct = 0):
        if posAct == posInsert - 1 or self.next == None:
            nuevo.next = self.next
            self.next = nuevo
        else:
            self.next.insert(nuevo, posInsert, posAct + 1)
    
    def delete(self, posDelete, posAct = 0):
        if posAct == posDelete - 1:
            self.next = self.next.next
        else:
            self.next.delete(posDelete, posAct + 1)
        
    def append(self, node = None):
        if self.next == None:
            self.next = node
        else:
            self.next.append(node)
    
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
        cantidad = 0
        if not self.isEmpty():
            cantidad = self.head.size()
        return cantidad
    
    
    def printList(self):
        if not self.isEmpty():
            print(self.head)                
            if self.head.next != None:
                aux = List()
                aux.head = self.head.next
                aux.printList()

    def mostrar(self):
        if not self.isEmpty():
            self.head.mostrar()
            
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
        new_node = NodeList(data)
        if self.isEmpty():
            self.head = new_node
        else: 
            self.head.append(new_node)
    
    def insert(self, pos = 0, data = None):
        nuevo = NodeList(data)
        if self.isEmpty():
            self.head = nuevo
        else:
            if pos == 0:
                nuevo.next = self.head
                self.head = nuevo
            else:
                self.head.insert(nuevo, pos)
      
    def delete(self, pos):
        if not self.isEmpty() and pos < self.size() and pos >= 0:
            if pos == 0:
                self.head = self.head.next
            else:
                self.head.delete(pos)
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