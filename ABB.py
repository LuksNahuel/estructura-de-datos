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
            
    def isLeaf(self):
        return self.left == None and self.right == None
    
    def hasLeft(self):
        return self.left != None

    def hasRight(self):
        return self.right != None
    
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
    
    def insert(self, node):
        if node.data < self.data:
            if self.hasLeft():
                self.left.insert(node)
            else:
                self.left = node
        elif node.data > self.data:
            if self.hasRight():
                self.right.insert(node)
            else:
                self.right = node
        else:
            print("Dato existente.")
    
    def search(self, data):
        output = None
        if self.data == data:
            output = self
        elif data < self.data:
            if self.hasLeft():
                output = self.left.search(data)
        else:
            if self.hasRight():
                output = self.right.search(data)
        return output
        
    def grade(self):
        output = 0
        if self.hasRight() and self.hasLeft():
            output = 2
        elif self.hasRight() or self.hasLeft():
            output = 1
        return output
        
    def maximum(self):
        output = None
        if not self.hasRight():
            output = self
        else:
            output = self.right.maximum()
        return output
        
    def minimum(self):
        output = None
        if not self.hasLeft():
            output = self
        else:
            output = self.left.minimum()
        return output

    def predecessor(self):
        output = None
        if self.hasLeft():
            output = self.left.maximum()
        return output
    
    def sucessor(self):
        output = None
        if self.hasRight():
            output = self.right.minimum()
        return output
    
    def height(self):
        height = 0
        if self.grade() == 2:
            height = 1 + max(self.left.height(), self.right.height())
        elif self.hasLeft():
            height = 1 + self.left.height()
        elif self.hasRight():
            height = 1 + self.right.height()
        return height
    
    def delete(self, data):
        if data < self.data:
            if self.hasLeft():
                if self.left.data == data:
                    if self.left.grade() == 2:
                        pred = self.left.predecessor()
                        self.left.delete(pred.data)
                        pred.left = self.left.left
                        pred.right = self.left.right
                        self.left = pred
                    elif self.left.hasLeft():
                        self.left = self.left.left
                    elif self.left.hasRight():
                        self.left = self.left.right
                    else:
                        self.left = None
                else:
                    self.left.delete(data)
        else:
            if self.hasRight():
                if self.right.data == data:
                    if self.right.grade() == 2:
                        pred = self.right.predecessor()
                        self.right.delete(pred.data)
                        pred.left = self.right.left
                        pred.right = self.right.right
                        self.right = pred
                    elif self.right.hasLeft():
                        self.right = self.right.left
                    elif self.right.hasRight():
                        self.right = self.right.right
                    else:
                        self.right = None
                else:
                    self.right.delete(data)
                    
    def weight(self):
        peso = 1
        if self.grade() == 2:
            peso = self.left.weight() + self.right.weight()
        elif self.hasLeft():
            peso = peso + self.left.weight()
        elif self.hasRight():
            peso = peso + self.right.weight()
        return peso
        
#        output = 1
#        if self.hasLeft():
#            output = output + self.left.weight()
#        if self.hasRight():
#            output = output + self.right.weight()
#        return output
    
    def searchPath(self, path, index = 0):
        output = False
        if path[index] == self.data:
            if index + 1 < len(path):
                if path[index + 1] < self.data:
                    if self.hasLeft():
                        output = self.left.searchPath(path, index + 1)
                else:
                    if self.hasRight():
                        output = self.right.searchPath(path, index + 1)
            else:
                output = True
        return output
    
    def toList(self, orderList):
        if self.hasLeft():
            self.left.toList(orderList)
        orderList.append(self.data)
        if self.hasRight():
            self.right.toList(orderList)
        return orderList
    
    def sumaTotal(self):
#        suma = 0
#        if self.grade() == 2:
#            suma = self.data + self.left.promedioTotal() + self.right.promedioTotal()
#        elif self.hasLeft():
#            suma = self.data + self.left.promedioTotal()
#        elif self.hasRight():
#            suma = self.data + self.right.promedioTotal()
#        else:
#            suma = self.data
#        return suma
        suma = self.data
        if self.hasLeft():
            suma += self.left.promedioTotal()
        if self.hasRight():
            suma += self.right.promedioTotal()
        return suma

    def sumaHojas(self):
        suma = 0
        if self.grade() == 2:
            suma = self.left.sumaHojas() + self.right.sumaHojas()
        elif self.hasLeft():
            suma = self.left.sumaHojas()
        elif self.hasRight():
            suma = self.right.sumaHojas()
        else:
            suma = self.data
        return suma
    
#        suma = 0
#        if self.hasLeft():
#            suma = suma + self.left.sumaHojas()
#        if self.hasRight():
#            suma = suma + self.right.sumaHojas()
#        if self.isLeaf():
#            suma = self.data
#        return suma
    
    def leafs(self):
        leafs = 0
        if self.grade() == 2:
            leafs = self.left.leafs() + self.right.leafs()
        elif self.hasLeft():
            leafs = leafs + self.left.leafs()
        elif self.hasRight():
            leafs = leafs + self.left.leeafs()
        else:
            leafs = 1
        return leafs

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
    
    def maximum(self):
        if not self.isEmpty():
            return self.root.maximum()
        else:
            raise Exception("El árbol está vacío.")
    
    def minimum(self):
        if not self.isEmpty():
            return self.root.minimum()
        else:
            raise Exception("El árbol está vacío.")
    
    def search(self, data):
        output = False
        if not self.isEmpty() and self.root.search(data) != None:
            output = True
        return output
    
    def weight(self):
        output = 0
        if not self.isEmpty():
            output = self.root.weight()
        return output
    
    def delete(self, data):
        if not self.isEmpty() and self.search(data):
            if self.root.data == data:
                pred = self.root.predecessor()
                self.root.delete(pred.data)
                pred.left = self.root.left
                pred.right = self.root.right
                self.root = pred
            else:
                self.root.delete(data)
        else:
            raise Exception("El dato no existe o el árbol está vacío.")
            
    def searchPath(self, path):
        output = False
        if not self.isEmpty():
            output = self.root.searchPath(path)
        return output
    
    def promedio(self, tipo = 0):
        promedio = 0
        if not self.isEmpty():
            if tipo == 0:
                promedio = self.root.sumaTotal() / self.weight()
            elif tipo == 1:
                promedio = self.root.sumaHojas() / self.leafs()
            else:
                raise Exception("No es un tipo válido.")
        return promedio
    
    def toList(self):
        lista = []
        if not self.isEmpty():
            self.root.toList(lista)
        return lista

def ordenaParaAnalizar(lista):
    pesosOrdenados = ABB()
    for peso in lista:
        pesosOrdenados.insert(peso)
    return pesosOrdenados

def promedioDeCarga(arbol):
    return arbol.promedio(0)

def rangoDinamicoDeCarga(arbol):
    return arbol.maximum() - arbol.minimum()

def impuestoACobrar(arbol, corte, impuesto):
    listaImpuestos = []
    listaArbol = arbol.toList()
    
    for peso in listaArbol:
        if peso > corte:
            listaImpuestos.append((peso - corte) * impuesto)
    return listaImpuestos
    