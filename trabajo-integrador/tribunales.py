# -*- coding: utf-8 -*-
import numpy as np
import juzgado

class Tribunales:
    def __init__(self, pisos = 0, oficinasPorPiso = 0):
        self.edificio = np.empty(shape = (pisos, oficinasPorPiso), dtype = juzgado.Juzgado)
    
    def cantidadDeJuzgadosComplicados(self, piso):
        cantidad = 0
        for oficina in self.edificio[piso]:
            if oficina != None:
                if oficina.estaComplicado():
                    cantidad += 1
        return cantidad
        
    def establecerJuzgadoEn(self, piso, oficina, juzgado):
        self.edificio[piso][oficina] = juzgado
        
    def juzgadoMasRecargado(self, piso):
        juzgado = None
        maxExpedientes = 0
        
        for oficina in self.edificio[piso]:
            if oficina != None:
                expedientesAux = oficina.cantidadDeExpedientes()
                if expedientesAux > maxExpedientes:
                    juzgado = oficina
                    maxExpedientes = expedientesAux
        return juzgado
    
    def recorrerOficinas(self):
        juzgados = np.empty(shape = len(self.edificio), dtype = juzgado.Juzgado)
        pos = 0
        for piso in range(len(self.edificio) - 1, -1, -1):
            for oficina in range(len(self.edificio[0]) - 1, -1, -1):
                if piso == oficina:
                    juzgados[pos] = self.edificio[piso][oficina]
                    pos += 1
        return juzgados
    
    def subirEdificio(self):
        juzgados = np.empty(shape = len(self.edificio), dtype = juzgado.Juzgado)
        oficina = 0
        pos = 0
        for piso in range(len(self.edificio) - 1, -1, -1):
            juz = self.edificio[piso][oficina]
            if juz != None:
                if juz.cantidadDeExpedientes() > 0:
                    juzgados[pos] = juz
                    pos += 1
            oficina += 1
        return juzgados