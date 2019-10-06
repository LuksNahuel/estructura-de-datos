# -*- coding: utf-8 -*-

'''Crear el TDA "Electrodomestico" con los siguientes componentes: precio base, color
consumo energetico (letras entre A y F) y tamaño. A su vez, el tamaño esta compuesto 
por tres valores: alto, ancho y profundidad. Escribir el constructor y una operación
denominada "calculaPrecioVenta", que devuelve el precio de venta a partir del precio base
y un porcentaje de ganancia determinado.
Escribir un programa principal en el cual se crea una variable de tipo "Electrodomestico"
y se muestra por pantalla su precio de venta con un 35% de ganancia.'''


def consumoEsValido(consumo):
    return consumo == "A" or consumo == "B" or consumo == "C" or consumo == "D" or consumo == "E" or consumo == "F"

class Tamanio:
    def __init__(self, alto = 0, ancho = 0, profundidad = 0):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad


class Electrodomestico:
    def __init__(self, precioBase = 0, color = "", consumo = "", tamanio = None):
        self.precioBase = precioBase
        self.color = color
        self.tamanio = tamanio
        if consumoEsValido(consumo):
            self.consumo = consumo
        else:
            raise Exception("No es un valor válido.")
    def calcularPrecioVenta(self, porcentaje):
        return self.precioBase * (1 + porcentaje/100)
