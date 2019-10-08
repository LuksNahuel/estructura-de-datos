#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:23:28 2019

@author: estruc-datos
"""


def esCausaValida(causa):
    return causa == "civil" or causa == "penal" or causa == "criminal"
def esPrioridadValida(prioridad):
    return prioridad == "normal" or prioridad == "urgente"


class Expediente():
    def __init__(self, num_id, tipoCausa, prioridad):
        self.numExpediente = num_id
        
        if esCausaValida(tipoCausa):
            self.tipoCausa = tipoCausa
        else:
            raise Exception("No es un tipo de causa válida.")
        
        if esPrioridadValida(prioridad):
            self.prioridad = prioridad
        else:
            raise Exception("No es un tipo de prioridad válida.")
    
    def __repr__(self):
        return str((self.numExpediente, self.tipoCausa, self.prioridad))
        #salida = str(self.numExpediente) + ", " + self.tipoCausa + ", " + self.prioridad
        #return salida
    
    def getPrioridad(self):
        return self.prioridad
    
    def getTipo(self):
        return self.tipoCausa
        
    def getNum(self):
        return self.numExpediente
    
    def cambiarPrioridad(self):
        if self.prioridad == "normal":
            self.prioridad = "urgente"
        else:
            self.prioridad = "normal"

    
    
    
    
    
    
    
    
    