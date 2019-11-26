#!/usr/bin/python3

class NodoLista:
    def __init__(self, dato = None):
        self.dato = dato
        self.siguiente = None
    
    def travel(self):
        if self.siguiente != None:
            self.siguiente.travel()

    def append(self, nuevo):
        if self.siguiente == None:
            self.siguiente = nuevo
        else:
            self.siguiente.append(nuevo)

    def size(self):
        size = 1
        if self.siguiente != None:
            size = 1 + self.siguiente.size()
        return size

    def insert(self, nuevo, inspos, actpos = 0):
        if actpos == inspos-1 or self.siguiente == None:
            nuevo.siguiente = self.siguiente
            self.siguiente = nuevo
        else:
            self.siguiente.insert(nuevo, inspos, actpos+1)

    def delete(self, delpos, actpos = 0):
        if actpos == delpos-1:
            self.siguiente = self.siguiente.siguiente
        else:
            self.siguiente.delete(delpos, actpos+1)
    
    def getDato(self, getpos, actpos = 0):
        dato = None
        if actpos == getpos:
            dato = self.dato
        else:
            dato =  self.siguiente.getDato(getpos, actpos+1)
        return dato

    def replace(self, dato, reppos, actpos = 0):
        if actpos == reppos:
            self.dato = dato
        else:
            self.siguiente.replace(dato, reppos, actpos+1)

    def clone(self, outlist):
        outlist.append(self.dato)
        if self.siguiente != None:
            self.siguiente.clone(outlist)

    def extend(self, outlist):
        outlist.append(self.dato)
        if self.siguiente != None:
            self.siguiente.extend(outlist)

    def deleteAll(self, dato):
        cont = 0
        if self.siguiente != None:
            if self.siguiente.dato == dato:
                self.siguiente = self.siguiente.siguiente
                cont = 1 + self.deleteAll(dato)
            else:
                cont = self.siguiente.deleteAll(dato)
        return cont

    def search(self, dato):
        cant = 0
        if self.dato == dato:
            if self.siguiente != None:
                cant = 1 + self.siguiente.search(dato)
            else:
                cant = 1
        elif self.siguiente != None:
            cant = self.siguiente.search(dato)
        return cant

    def repr(self, out):
        out = out + " -> " + str(self.dato)
        if self.siguiente != None:
            aux = ""
            out = out + self.siguiente.repr(aux)
        else:
            out = out + " -|"
        return out
    
    def insertarOrdenado(self, nuevo):
        if nuevo.dato <= self.siguiente.dato or self.siguiente.siguiente == None:
            if self.siguiente.siguiente == None:
                self = self.siguiente
            nuevo.siguiente = self.siguiente
            self.siguiente = nuevo
        else:
            self.siguiente.insertarOrdenado(nuevo)

class Lista:
    def __init__(self):
        self.primero = None

    def isEmpty(self):
        return self.primero == None

    def travel(self):
        if not self.isEmpty():
            self.primero.travel()
        else:
            print("Lista vacia")

    def size(self):
        size = 0
        if not self.isEmpty():
            size = self.primero.size()
        return size
    
    def append(self, dato = None):
        nuevo = NodoLista(dato)
        if self.isEmpty():
            self.primero = nuevo
        else:
            self.primero.append(nuevo)

    def insert(self, dato = None, pos = 0):
        if pos >= 0:
            nuevo = NodoLista(dato)
            if self.isEmpty():
                self.primero = nuevo
            elif pos == 0:
                nuevo.siguiente = self.primero
                self.primero = nuevo
            else:
                self.primero.insert(nuevo, pos)
        else:
            raise Exception("Posicion incorrrecta.")

    def delete(self, pos = 0):
        if not self.isEmpty() and pos >= 0 and pos < self.size():
            if pos == 0:
                self.primero = self.primero.siguiente
            else:
                self.primero.delete(pos)
        else:
            if self.isEmpty():
                raise Exception("Lista vacia.")
            else:
                raise Exception("Posicion incorrecta.")

    def getDato(self, pos = 0):
        if pos < self.size() and pos >= 0:
            return self.primero.getDato(pos)
        else:
            raise Exception("La posicion no existe en la lista.")

    def replace(self, dato = None, pos = 0):
        if pos >= 0 and pos < self.size() and not self.isEmpty():
            self.primero.replace(dato,pos)
        else:
            if self.isEmpty():
                raise Exception("Lista vacia.")
            else:
                raise Exception("Posicion incorrrecta.")

    def clone(self, outlist):
        outlist.primero = None
        if not self.isEmpty():
            self.primero.clone(outlist)

    def change2First(self):
        if self.getLen() >= 2:
            aux = self.primero
            self.primero = aux.siguiente
            aux.siguiente = self.primero.siguiente
            self.primero.siguiente = aux
        else:
            raise Exception("Lista con longitud insuficiente.")

    def extend(self, otherlist):
        if not otherlist.isEmpty():
            otherlist.primero.extend(self)

    def deleteAll(self, dato = None):
        cont = 0
        if not self.isEmpty():
            while not self.isEmpty() and self.primero.dato == dato:
                cont += 1
                self.primero = self.primero.siguiente
            if not self.isEmpty():
                cont = cont + self.primero.deleteAll(dato)
        return cont
    
    def search(self, dato = None):
        cant = 0
        if not self.isEmpty():
            cant = self.primero.search(dato)
        return cant

    def __repr__(self):
        out = "primero"
        if self.isEmpty():
            out = out + "-|"
        else:
            aux = ""
            out = out + self.primero.repr(aux)
        return out

    def insertarOrdenado(self, dato):
        nuevo = NodoLista(dato)
        if self.isEmpty():
            self.primero = nuevo
        elif dato <= self.primero.dato:
            nuevo.siguiente = self.primero
            self.primero = nuevo
        else:
            self.primero.insertarOrdenado(nuevo)