#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
class Complejo:
    def __init__(self, r = 0, i = 0):
        self.parteReal = r
        self.parteImaginaria = i
    def obtenerParteReal(self):
        return self.parteReal
    def obtenerParteImaginaria(self):
        return self.parteImaginaria
    def modificarParteReal(self, r):
        self.parteReal = r
    def modificarParteImaginaria(self, i):
        self.parteImaginaria = i
    def mostrar(self):
        if self.parteImaginaria >= 0:
            print("%s + %s i" % (self.parteReal, self.parteImaginaria))
        else:
            print("%s - %s i" % (self.parteReal, abs(self.parteImaginaria)))   
        #print(self.parteReal, "+ i", self.parteImaginaria)
    def suma(self, complejo):
        pR = self.parteReal + complejo.parteReal
        pI = self.parteImaginaria + complejo.parteImaginaria
        return Complejo(pR, pI)
    def resta(self, complejo):
        pR = self.parteReal - complejo.parteReal
        pI = self.parteImaginaria - complejo.parteImaginaria
        return Complejo(pR, pI)
    def multiplicacion(self, complejo):
        pR = (self.parteReal * complejo.parteReal) - (self.parteImaginaria * complejo.parteImaginaria)
        pI = (self.parteReal * complejo.parteImaginaria) + (self.parteImaginaria * complejo.parteReal)
        return Complejo(pR, pI)
    def modulo(self):
        return math.sqrt(self.parteReal**2 + self.parteImaginaria**2)
    def fase(self):
        return math.atan(self.parteImaginaria / self.parteReal)
    def conjugado(self):
        return Complejo(self.parteReal, self.parteImaginaria * (-1))
    def division(self, complejo):
        nuevo = self.multiplicacion(complejo.conjugado())
        nuevo.parteReal = nuevo.parteReal / (complejo.modulo() ** 2)
        nuevo.parteImaginaria = nuevo.parteImaginaria / (complejo.modulo() ** 2)
        return nuevo