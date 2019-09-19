# -*- coding: utf-8 -*-
class Fraccion:
    def __init__(self, n = 1, d = 1):
        self.numerador = n
        self.denominador = d
    def obtenerNumerador(self):
        return self.numerador
    def obtenerDenominador(self):
        return self.denominador
    def modificarNumerador(self, n):
        self.numerador = n
    def modificarDenominador(self, d):
        self.denominador = d
    def suma(self, fraccion):
        if self.denominador == fraccion.denominador:
            return Fraccion(self.numerador + fraccion.numerador, self.denominador)
        else:
            mcm = minimoComunMultiplo(self.denominador, fraccion.denominador)
            numerador = ((mcm//self.denominador) * self.numerador) 
            + ((mcm//fraccion.denominador) * fraccion.numerador)
            return Fraccion(numerador, mcm)
    def resta(self, fraccion):
        if self.denominador == fraccion.denominador:
            return Fraccion(self.numerador - fraccion.numerador, self.denominador)
        else:
            numerador = (self.numerador * fraccion.denominador) - (self.denominador * fraccion.numerador)
            denominador = self.denominador * fraccion.denominador
            return Fraccion(numerador, denominador)
    def multiplicar(self, fraccion):
        return Fraccion(self.numerador * fraccion.numerador, self.denominador * fraccion.denominador)
    def dividir(self, fraccion):
        return Fraccion(self.numerador * fraccion.denominador, self.denominador * fraccion.numerador)
    def simplificar(self):
        divisor = maximoComunDivisor(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor
    def esIgual(self, fraccion):
        a = Fraccion(self.numerador, self.denominador)
        b = Fraccion(fraccion.numerador, fraccion.denominador)
        a.simplificar()
        b.simplificar()
        return a.numerador == b.numerador and a.denominador == b.denominador

def minimoComunMultiplo(d1, d2):
    A = max(d1, d2)
    B = min(d1, d2)
    while B > 0:
        mcd = B
        B = A % B
        A = mcd
    return (d1 * d2) // mcd

def maximoComunDivisor(d1, d2):
    A = max(d1, d2)
    B = min(d1, d2)
    while B > 0:
        mcd = B
        B = A % B
        A = mcd
    return mcd
