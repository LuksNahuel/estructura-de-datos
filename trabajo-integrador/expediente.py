#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:23:28 2019

@author: estruc-datos
"""
import cola

def esCausaValida(causa):
    return causa == "civil" or causa == "penal" or causa == "criminal"
def esPrioridadValida(prioridad):
    return prioridad == "normal" or prioridad == "urgente"


class Expediente():
    def __init__(self, num_id = None, tipoCausa = "penal", prioridad = "normal"):
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
        #return str((self.numExpediente, self.causa, self.prioridad))
        salida = str(self.numExpediente) + ", " + self.tipoCausa + ", " + self.prioridad
        return salida
    
    def getPrioridad(self):
        return self.prioridad
    
class Juzgado():
    def __init__(self, capacidad = 50):
        self.normales = cola.Cola(capacidad, dtype = Expediente)
        self.urgentes = cola.Cola(capacidad, dtype = Expediente)
    
    def recibirExpediente(self, exp):
        if exp.getPrioridad() == "normal":
            self.normales.queue(exp)
        elif exp.getPrioridad() == "urgente":
            self.urgentes.queue(exp)
    
    def primerExpedienteATratar(self):
        salida = None
        if not self.urgentes.isEmpty():
            salida = self.urgentes.top()
        else:
            salida = self.normales.top()
        return salida