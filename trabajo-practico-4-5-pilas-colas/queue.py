# -*- coding: utf-8 -*-
import numpy as np

def shift(queue, last):
    for i in range(1, last+1):
        queue[i-1] = queue[i] 


class Queue:
    def __init__(self, size, dtype = int):
        self.vector = np.zeros(shape = (size), dtype = dtype)
        self.last = None
    
    def isFull(self):
        return self.last == len(self.vector) - 1
    
    def isEmpty(self):
        return self.last == None
    
    def queue(self, data):
        if not self.isFull():
            if self.isEmpty():
                self.last = -1
            self.vector[self.last + 1] = data
            self.last += 1
        else:
            raise Exception("La cola está llena.")
            
    def deQueue(self):
        salida = None
        if not self.isEmpty():
            salida = self.vector[0]
            if self.last == 0:
                self.last = None
            else:
                shift(self.vector, self.last)
                self.last -= 1
        else:
            raise Exception("La cola está vacía.")
        return salida
    
    


