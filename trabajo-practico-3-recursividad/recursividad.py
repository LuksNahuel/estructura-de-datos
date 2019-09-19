#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# EJERCICIO 2 #
'''Una canilla de una casa pierde agua de forma que todos los dias pierde dos
gotas mas que el dia anterior. Escribir una función recursiva que calcule
cuantas gotas perdera la canilla luego de N días, sabiendo que el primer dia
solo perdia 2 gotas.'''

def aguaPerdida(n):
    agua = 0
    if n == 1:
        agua = 2
    else:
        agua = 2 + aguaPerdida( n - 1 ) 
    return agua

def aguaPerdida_v2(n):
    try:
        a = 0
        if n == 1:
            a = 2
        else:
            a = 2 + aguaPerdida(n-1)
        return a
    except:
        print("Error. El día tiene que ser positivo.")

# EJERCICIO 3 #
'''Si se colocase sobre un tablero de ajedrez, un grano de trigo en el primer casillero,
dos en el segundo, cuarto en el tercero y asi sucesivamente, doblando la cantidad de
granos en cada casilla ¿Cuantos granos de trigo habria en el tablero al final?
Resolver el problema con una función recursiva.'''

def granosCasillero(n):
    granos = 0
    if n == 1:
        granos = 1
    else:
        granos = 2 * granosCasillero(n - 1)
    return granos

def totalTablero(n):
    granos = 0
    if n == 1:
        granos = granosCasillero(1)
    else:
        granos = granosCasillero(n) + totalTablero(n - 1)
    return granos

# EJERCICIO 4 #
'''Escribir un programa que pida por teclado un numero natural N y devuelva los
primeros N números de la serie de Fibonacci. Implementar la serie de Fibonacci de
forma recursiva.'''

def fibonacci(n):
    f = 0
    if(n <= 2):
        f = 1
    else:
        f = fibonacci(n - 2) + fibonacci(n - 1)
    return f

#def serieFibo(n):

# EJERCICIO 5 #
'''Escribir una funcion recursiva que calcule el numero triangular de indice N (Suma de
los primeros N números enteros). Recordar que: T(N) = N + T(N - 1)'''

def numeroTriangular(n):
    t = 0
    if n == 1:
        t = 1
    else:
        t = n + numeroTriangular(n - 1)
    return t

def combinatorio(n, m):
    c = 0
    if m == 1:
        c = n
    elif n == m:
        c = 1
    elif n>m and m>1:
        c = combinatorio(n-1, m-1) + combinatorio(n-1, m)
    return c

# EJERCICIO 7 #
'''Escribir una función recursiva que pase un numero decimal a base 2.'''

def binario(n):
    if n < 2:
        print(n)
    else:
        binario(n//2)
        print(n%2)

# EJERCICIO 8 #
'''Escribir una función recursiva que reciba un numero positivo N y calcule la cantidad
de digitos que tiene.'''

def digitos(n):
    d = 0
    if n < 10:
        d = 1
    else:
        d = 1 + digitos(n//10)
    return d

# EJERCICIO 9 #

'''def esPotencia(n, b):
    if n == 0:
        return True
    else:'''
            


















