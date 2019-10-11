# -*- coding: utf-8 -*-
import numpy as np
import expediente
import cola

class Juzgado():
    def __init__(self, nombre, capacidad = 50):
        self.normales = cola.Cola(capacidad, dtype = expediente.Expediente)
        self.urgentes = cola.Cola(capacidad, dtype = expediente.Expediente)
        self.nombre = nombre
        
    def __repr__(self):
        return str((self.nombre))
    
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
    
    def tratarPrimerExpediente(self):
        prioridad = self.primerExpedienteATratar().getPrioridad()
        salida = None
        if prioridad == "urgente":
            salida = self.urgentes.dequeue()
        else:
            salida = self.normales.dequeue()
        return salida
    
    def cantidadDeExpedientes(self):
        return self.normales.getLen() + self.urgentes.getLen()
    
    def estaComplicado(self):
        return self.cantidadDeExpedientes() > 50
    
    def cantidadPorTipo(self, tipoExp):
        return np.array([contadorDeTipos(self.normales, tipoExp), contadorDeTipos(self.urgentes, tipoExp)])
    
    def cambiaDeEstado(self, nroExp):
        if estaEnLaCola(self.normales, nroExp):
            self.urgentes.queue(tratarLaCola(self.normales, nroExp))
        elif estaEnLaCola(self.urgentes, nroExp):
            self.normales.queue(tratarLaCola(self.urgentes, nroExp))
        else:
           raise Exception("El expediente no está en ninguna de las colas.")

def contadorDeTipos(cola, tipo):
    aux = cola.clone()
    cantidadNormal = 0
    while not aux.isEmpty():
            data = aux.dequeue()
            if data.getTipo() == tipo:
                cantidadNormal += 1
    return cantidadNormal

def estaEnLaCola(cola, num):
    aux = cola.clone()
    salida = False
    while not aux.isEmpty():
        data = aux.dequeue()
        if data.getNum() == num:
            salida = True
    return salida

def tratarLaCola(expedientes, num):
    aux = cola.Cola(expedientes.getLen(), dtype = expediente.Expediente)
    dato = None
    while not expedientes.isEmpty():
        exp = expedientes.dequeue()
        if exp.getNum() == num:
            dato = exp
            dato.cambiarPrioridad()
        else:
            aux.queue(exp)
    while not aux.isEmpty():
        expedientes.queue(aux.dequeue())
    return dato