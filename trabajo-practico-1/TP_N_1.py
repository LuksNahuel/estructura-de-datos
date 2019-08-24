#EJERCICIO 2
def tablaDeMultiplicar():
    num = int(input("Dame un número: "))
    for i in range(1, 13):
        print(num, 'X', i, '=', num * i)
#EJERCICIO 6
def cualEsMenor(num1, num2):
    if num1 == num2:
        print('Son iguales')
    elif num1 > num2:
        print(num2, ' es más chico')
    else:
        print(num1, ' es más chico')
#EJERCICIO 7
def parImpar(num):
    if(num % 2 == 0):
        print(num, ' es par.')
    else:
        print(num, ' es impar.')
#EJERCICIO 10
def numerosDivisiblesPor2Y3 ():
    for num in range(1,101):
        if(num % 2 == 0 and num % 3 == 0):
            print(num)
#EJERCICO 9
def numerosConWhile ():
    i = 1
    while(i<101):
        print(i)
        i += 1
def numerosConFor():
    for num in range(1,101):
        print(num)
#Ejercicio 12
def numeroTriangular():
    num = int(input("Dame un índice y te diré el número triangular correspondiente: "))
    i = 1
    while(i<=num):
        print(i, "-", ((i*(i+1)) // 2))
        i+=1
#EJERCICIO 13 - EST� MAL
def sumaPrimerosNumerosPares():
    num = int(input("Dame un número: "))
    contador = 0
    while(num != 0):
        num -= 1
        if(num % 2 ==0):
            contador += num
    print(contador)
#EJERCICIO 15
def paresEntreDosNumeros():
    primerNumero = int(input("Dame el primer numero: "))
    segundoNumero = int(input("Dame el segundo numero: "))
    for num in range(primerNumero, segundoNumero):
        if(num%2==0):
            print(num)
#EJERCICIO 16
def cuantasCifras():
    num = int(input("Ingrese un numero: "))
    cantidadDeCifras = 0
    while(num != 0):
        num = num // 10
        cantidadDeCifras += 1
    print(cantidadDeCifras)
#EJERCICIO 17 - ESTA MAL
def primo():
    num = int(input("Dame un numero y te digo si es primo: "))
    if num > 1:
        for i in range(2, num//2):
            if(num % i == 0):
                print(num, ' no es un numero primo')
                break
            else:
                print(num, ' es un numero primo')
    else:
        print(num, ' no es un numero primo')
import math
def esNumeroPrimo():
    num = int(input("Dame un numero y te digo si es primo: "))
    raiz = round(math.sqrt(num))
    if(num % 2 == 0):
        print("No es primo")
    else:
        for i in range(2, raiz + 1):
            if(num % i == 0):
                print("No es primo")
                break
            else:
                print("Es primo")
#EJERCICIO 19
def factorialDeUnNumero():
    num = int(input("Dame un numero: "))
    inicial = 1
    for i in range(inicial, num + 1):
        inicial = inicial * i
    print(inicial)
def factorial(num):
    inicial = 1
    for i in range(inicial, num + 1):
        inicial = inicial * i
    return inicial
#EJERCICIO 20
def combinatoria(m, n):
    aux = m - n
    print(factorial(m) // (factorial(n) * factorial(aux)))
#EJERCICIO 18







