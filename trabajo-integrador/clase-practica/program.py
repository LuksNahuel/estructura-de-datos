#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:19:52 2019

@author: estruc-datos
"""

import electrodomestico as electro

electrodomestico = electro.Electrodomestico(15000, "blanco", "B", electro.Tamanio(1.8, 0.7, 0.7))

print(electrodomestico.calcularPrecioVenta(35))