# -*- coding: utf-8 -*-
import complejo
import fracciones

c1 = complejo.Complejo(3.5, 5.6)
real = c1.obtenerParteReal()
imag = c1.obtenerParteImaginaria()

c1.modificarParteReal(3.5)

c2 = complejo.Complejo(4.2, 2.13)

c3 = c1.suma(c2)


f1 = fracciones.Fraccion(2, 3)
f2 = fracciones.Fraccion(3, 5)

f3 = f1.suma(f2)
f4 = f1.resta(f2)
f5 = fracciones.Fraccion(4, 8)
f7 = fracciones.Fraccion(8, 16)
