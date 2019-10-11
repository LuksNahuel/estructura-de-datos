import numpy as np

class Stack:
    def __init__(self, size, dtype = int):
        self.stack = np.zeros(shape=(size), dtype = dtype)
        self.top = None
    
    def getTop(self):
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            raise Exception("La pila está vacía.")
    
    def dtype(self):
        return self.stack.dtype
    
    def invertir(self):
        aux = self.clone()
        self.empty()
        while not aux.isEmpty():
            self.push(aux.pop())
    
    def getSize(self):
        salida = 0
        if not self.isEmpty():
            salida = self.top + 1
        return salida
    
    def printStack(self):
        if not self.isEmpty():
            for e in range(self.top, -1, -1):
                print(self.stack[e])
    
    def imprimir(self):
        if not self.isEmpty():
            print(self.stack[:self.top+1])
        else:
            raise Exception("La pila está vacía y no se puede imprimir.")
    
    def push(self, data):
        if not self.isFull():
            if self.isEmpty(): 
                self.top = -1
            self.stack[self.top + 1] = data
            self.top += 1
        else:
            raise Exception("No se puede apilar. La pila está llena.")
    
    def pop(self):
        salida = None
        if not self.isEmpty():
            salida =  self.stack[self.top]
            self.top -= 1
            if self.top == -1:
                self.top = None
        else:
            raise Exception("No se puede desapilar. La pila está vacía.")
        return salida
    
    def isEmpty(self):
        return self.top == None
    
    def isFull(self):
        return self.top == len(self.stack) - 1
    
    def empty(self):
        self.top = None
    
    def clone(self):
        nueva = Stack(len(self.stack), self.stack.dtype)
        if not self.isEmpty():    
            for i in range(self.top + 1):
                nueva.stack[i] = self.stack[i]
            nueva.top = self.top
        return nueva

