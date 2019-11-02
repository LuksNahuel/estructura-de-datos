#!/usr/bin/python3

from graphviz import Digraph

class NodoArbol:
    def __init__(self, dato = None):
        self.data = dato
        self.left = None
        self.right = None
    
    def treePlot(self, dot):
        if self.hasLeft():
            dot.node(str(self.left.data), str(self.left.data))
            dot.edge(str(self.data), str(self.left.data))
            self.left.treePlot(dot)
        if self.hasRight():
            dot.node(str(self.right.data), str(self.right.data))
            dot.edge(str(self.data), str(self.right.data))
            self.right.treePlot(dot)
    
    def preOrder(self):
        print(self.data)
        if self.hasLeft():
            self.left.preOrder()
        if self.hasRight():
            self.right.preOrder()
            
    def inOrder(self):
        if self.hasLeft():
            self.left.inOrder()
        print(self.data)
        if self.hasRight():
            self.right.inOrder()
    
    def postOrder(self):
        if self.hasLeft():
            self.left.postOrder()
        if self.hasRight():
            self.right.postOrder()
        print(self.data)
    
    def insert(self, nodo):
        if nodo.data < self.data:
            if self.hasLeft():
                self.left.insert(nodo)
            else:
                self.left = nodo
        elif nodo.data > self.data:
            if self.hasRight():
                self.right.insert(nodo)
            else:
                self.right = nodo
        else:
            print("Dato existente.")
    
    def grade(self):
        if self.isLeaf():
            return 0
        elif self.hasRight() and self.hasLeft():
            return 2
        else:
            return 1
    
    def isLeaf(self):
        return self.left == None and self.right == None
    
    def hasLeft(self):
        return self.left != None

    def hasRight(self):
        return self.right != None
    
class ABB:
    def __init__(self):
        self.root = None

    def treePlot(self, fileName='tree'):
        if not self.isEmpty():
            treeDot = Digraph()
            treeDot.node(str(self.root.data), str(self.root.data))
            self.root.treePlot(treeDot)
            treeDot.render(fileName, view=True)
    
    def isEmpty(self):
        return self.root == None
    
    def insert(self, data):
        new = NodoArbol(data)
        if self.isEmpty():
            self.root = new
        else:
            self.root.insert(new)
    
    def preOrder(self):
        if not self.isEmpty():
            self.root.preOrder()
    
    def inOrder(self):
        if not self.isEmpty():
            self.root.inOrder()
            
    def postOrder(self):
        if not self.isEmpty():
            self.root.postOrder()
    
    def empty(self):
        self.root = None
    
    def search(self, data):
        if self.root == data:
            return True
        else:
            self.root.search(data)