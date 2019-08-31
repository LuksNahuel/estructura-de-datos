# -*- coding: utf-8 -*-
import complejo

c1 = complejo.Complejo(3.5, 5.6)
real = c1.obtenerParteReal()
imag = c1.obtenerParteImaginaria()

c1.modificarParteReal(3.5)

c2 = complejo.Complejo(4.2, 2.13)

c3 = c1.suma(c2)


