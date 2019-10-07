#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:23:28 2019

@author: estruc-datos
"""
import cola
import numpy as np

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
    
    def getTipo(self):
        return self.tipoCausa
        
class Juzgado():
    def __init__(self, capacidad = 50):
        self.normales = cola.Cola(capacidad, dtype = Expediente)
        self.urgentes = cola.Cola(capacidad, dtype = Expediente)
    
    def recibirExpediente(self, exp):
        if exp.getPrioridad() == "normal":
            self.normales.queue(exp)
        else:
            self.urgentes.queue(exp)
    
    def primerExpedienteATratar(self):
        salida = None
        if not self.urgentes.isEmpty():
            salida = self.urgentes.top()
        else:
            salida = self.normales.top()
        return salida
    
    def cantidadDeExpedientes(self):
        return self.normales.getLen() + self.urgentes.getLen()
    
    def cantidadPorTipo(self, tipoExp):
        auxNormales = self.normales.clone()
        cantidadNormal = 0
        while not auxNormales.isEmpty():
            data = auxNormales.dequeue()
            if data.getTipo() == tipoExp:
                cantidadNormal += 1
        
        auxUrgentes = self.urgentes.clone()
        cantidadUrgente = 0
        while not auxUrgentes.isEmpty():
            data = auxUrgentes.dequeue()
            if data.getTipo() == tipoExp:
                cantidadUrgente += 1
        
        return np.array([cantidadNormal, cantidadUrgente])
    
    
    
    
    
    
    
    
def cantidadPorMeses(meses):
    salida = 0
    if meses <= 2:
        salida = 250
    elif meses % 2 == 0:
        salida = cantidadPorMeses(meses - 1) + cantidadPorMeses(meses - 2)
    else:
        salida = cantidadPorMeses(meses - 1) * 3 + 20
    return salida
    
    
    
    
    
    
    
    
    
    