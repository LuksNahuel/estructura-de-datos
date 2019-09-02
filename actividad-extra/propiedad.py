#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:21:07 2019


"""

""" Crear el TAD Propiedad 

-tipo (por defecto un ‘terreno’)
-calle
-altura
-año de construcción (por defecto 0, hasta que se construya)
-ancho del terrno
-largo del terreno
-superficie de construcción (este dato se completa al construir 
   una ‘casa’)

--------

Operaciones:
    
    * Las interfaces para obtener cada dato:  Get....
    * construir en un terreno. En ese momento se registra el año de la construcción,
        la superficie construida y el tipo de construcción (‘casa’ u ‘otro’).
    * Se desea saber para cada propiedad el sentido de circulación de la calle
        - O --> E
        - E --> O
    * Obtener el valor de la propiedad sabiendo que el mt2 tiene un valor de:
             $ 5.000 si es terreno
             $ 10.000 si es casa
             $ 8.000 si es “otro”
    * Indicar si al estar parado en una calle determinada, la propiedad:
            - Está hacia el NORTE, hacia el SUR
            - o en la misma calle
"""

class Propiedad:
    def __init__(self, tipo = 'terreno', calle = None, altura = None, anioDeConstruccion = 0, anchoTerreno = None, 
    largoTerreno = None, superficieConstruccion = None):
        self.tipo = tipo
        self.calle = calle
        self.altura = altura
        self.anioDeConstruccion = anioDeConstruccion
        self.anchoTerreno = anchoTerreno
        self.largoTerreno = largoTerreno
        self.superficieConstruccion = superficieConstruccion
    def getTipo(self):
        return self.tipo
    def getCalle(self):
        return self.calle
    def getAltura(self):
        return self.altura
    def getDireccion(self):
        return (self.calle, self.altura)
    def getAnioDeConstruccion(self):
        return self.anioDeConstruccion
    def getAnchoTerreno(self):
        return self.anchoTerreno
    def getLargoTerreno(self):
        return self.largoTerreno
    def getSuperficieConstruccion(self):
        return self.superficieConstruccion
    def construirEnUnTerreno(self, anioConstruccion, superficieConstruccion, tipo):
        if self.tipo == 'terreno':
            self.tipo = tipo
            self.anioDeConstruccion = anioConstruccion
            self.superficieConstruccion = superficieConstruccion
    def sentidoCirculacion(self):
        if self.calle % 2 == 0:
            return 'O --> E'
        else:
            return 'E --> O'
    def getValorPropiedad(self):
        if(self.tipo == 'terreno'):
            return (self.anchoTerreno * self.largoTerreno) * 5000
        elif(self.tipo == 'casa'):
            return self.superficieConstruccion * 10000
        else:
            return  self.superficieConstruccion * 8000
    
    def laPropiedadEstáAl(self, calle):
        if calle - self.calle > 0:
            return 'Sur'
        elif calle - self.calle < 0:
            return 'Norte'
        else:
            return 'Misma calle'