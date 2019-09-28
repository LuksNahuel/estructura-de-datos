#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# EJERCICIO 1 #
'''Implementar una funcion que calcule el factorial de un numero de forma recursiva.'''

def factorial(n):
    salida = 0
    if n < 2:
        salida = 1
    else:
        salida = n * factorial(n-1)
    return salida

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

# EJERCICIO 6 # 
'''Escribir una función recursiva que calcule las combinaciones de N elementos tomados
de a M'''

def combinatoria(n, m):
    c = 0
    if m == 1:
        c = n
    elif n == m:
        c = 1
    elif n>m and m>1:
        c = combinatoria(n-1, m-1) + combinatoria(n-1, m)
    return c

# EJERCICIO 7 #
'''Escribir una función recursiva que pase un numero decimal a base 2.'''

def pasarABinario(n):
    if n < 2:
        print(n, end="")
    else:
        pasarABinario(n//2)
        print(n%2, end="")
    

# EJERCICIO 8 #
'''Escribir una función recursiva que reciba un numero positivo N y calcule la cantidad
de digitos que tiene.'''

def cantidadDigitos(n):
    d = 0
    if n < 10:
        d = 1
    else:
        d = 1 + cantidadDigitos(n//10)
    return d

# EJERCICIO 9 #
'''Escribir un programa que reciba dos enteros positivos n y b y devuelva True si n es
potencia de b y False en caso contrario'''

def esPotencia(n, b):
    salida = None
    if n == 1:
        salida = True
    elif n < 1 or b == 1:
        salida = False
    else:
        salida = esPotencia(n/b, b)
    return salida

# EJERCICIO 10 #
'''El triangulo de pascal es un arreglo triangular de numeros que se define de la
siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los
valores de cada columna, se enumeran desde k = 0, de izquierda a derecha. Los
valores de los bordes del triangulo son siempre igual a 1. Cualquier otro valor se
calcula sumando los dos valores contiguos de la fila de arriba. Escribir la funcion
recursiva pascal(n , k), que calcula el valor que se encuentra en la fila n columna k.
Por ejemplo: pascal(5 , 2) = 10'''

def pascal(n,k):
    numero = None
    if k == 0 or n == k:
        numero = 1
    else:
        numero = pascal(n-1, k-1) + pascal(n-1, k)
    return numero
    


















