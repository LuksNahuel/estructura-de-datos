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

#EJERCICIO 8
def diaDeLaSemana(n):
    if n > 7 or n < 1:
        print("El número ingresado no está en el rango correcto")
    else: 
        if(n == 1):
            print("Lunes")
        if(n == 2):
            print("Martes")
        if(n == 3):
            print("Miércoles")
        if(n == 4):
            print("Jueves")
        if(n == 5):
            print("Viernes")
        if(n == 6):
            print("Sábado")
        if(n == 7):
            print("Domingo")

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

#EJERCICIO 11
def fichasDomino():
    fichaArriba = 0
    fichaAbajo = 0
    while fichaArriba <= 6:  
        print(fichaArriba, "|", fichaAbajo, "\n")
        fichaArriba += 1
        while fichaAbajo < 6 and not (fichaArriba > 6):
            fichaAbajo += 1
            if fichaArriba >= fichaAbajo:    
                print(fichaArriba, "|", fichaAbajo, "\n")
        fichaAbajo = 0

def dominoConFor():
    for i in range(0,7):
        for j in range(i, 7):
            print(i, "|", j)

def dominoMejor():
    primerNumero=0 
    while primerNumero<=6:  
        segundoNumero=0      
        while segundoNumero<=primerNumero:  
            print(primerNumero, "|", segundoNumero)
            segundoNumero+=1
        primerNumero+=1

#EJERCICIO 12
def numeroTriangular():
    num = int(input("Dame un índice y te diré el número triangular correspondiente: "))
    for i in range(1, num+1):
        print(i, "-", ((i*(i+1)) // 2))
        
def numeroTriangularConSumatoria():
    m = int(input("Ingrese un número: "))
    for n in range(1, m+1):
        triangular = 0
        for i in range(1, n+1):
            triangular += i
        print(n, "--", triangular)
        
#EJERCICIO 13
def sumandoLosPrimerosNumerosPares():
    num = int(input("Dame un número: "))
    print(num * (num + 1))

def sumaPrimerosNumerosPares():
    num = int(input("Dame un número: "))
    numerosPares = 2 
    suma = 0 
    cantidadPares = 1 
    while cantidadPares <= num:
        suma += numerosPares
        numerosPares += 2
        cantidadPares += 1
    print(suma, cantidadPares)

def sumaPrimeros ():
    num = int(input("Dame un número: "))
    cantidadDePares = 0 
    numero = 0 
    suma = 0 
    while cantidadDePares <= num:
        if(numero % 2 == 0):
            suma += numero
            cantidadDePares += 1
        numero += 1
    print(suma)

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

#EJERCICIO 17
def esPar(n):
    return n % 2 == 0
def esPrimo(n):
    if esPar(n) and n != 2:
        print("No es primo")
    elif n == 2:
        print("Es primo")
    else:
        for i in range(3, n):
            if(n % i == 0):
                print("No es primo")
                
            else:
                print("Es primo")
def es_Primo_(n):
    #n = int(input("Ingrese un número: "))
    if n <= 0:
        return False
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True               

#EJERCICIO 19
def factorialDeUnNumero():
    num = int(input("Dame un numero: "))
    inicial = 1
    for i in range(inicial, num + 1):
        inicial = inicial * i
    print(inicial)

def factorial(num):
    if(num > 0):
        inicial = 1
        for i in range(inicial, num + 1):
            inicial = inicial * i
        return inicial
    else:
        print("Debe ser un entero positivo")

#EJERCICIO 20
def combinatoria(m, n):
    aux = m - n
    print(factorial(m) // (factorial(n) * factorial(aux)))

#EJERCICIO 14
import math
import cmath
def raicesPolinomioSegundoGrado():
    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))
    c = float(input("Introduce el valor de c: "))
    
    discriminante = (b**2) - (4 * a * c)
    
    if discriminante < 0:
        x1 = (-1)*b - cmath.sqrt(discriminante) / (2 * a)
        x2 = (-1)*b + cmath.sqrt(discriminante) / (2 * a)
        print(x1, x2)
    else:
        x1 = (-1)*b - math.sqrt(discriminante) / (2 * a)
        x2 = (-1)*b + math.sqrt(discriminante) / (2 * a)
        print(x1, x2)

def raicesCuadratica():
    a = int(input("Introduce el valor de a: "))
    b = int(input("Introduce el valor de b: "))
    c = int(input("Introduce el valor de c: "))
    
    disc = (b**2) - (4 * a * c)
    
    if disc < 0:
        parteReal = (-1)*b / 2*a
        parteImg = math.sqrt(abs(disc)) / 2*a
        print(parteReal, "+i", parteImg)
      
#EJERCICIO 18
def cambioDeBases():
    for n in range(32, 65):
        for b in range(2, 17):
            #print("Resultado en base", b, "de", n)
            aux = n
            while aux >= b:
                r = aux%b
                aux = aux//b
                print(cambiarCaracter(r), end="")
            print(cambiarCaracter(aux), "\t", end="")
        print("\n")

def cambiarCaracter(num):
    if num == 10:
        return "A"
    if num == 11:
        return "B"
    if num == 12:
        return "C"
    if num == 13:
        return "D"
    if num == 14:
        return "E"
    if num == 15:
        return "F"
    else:
        return num

#def productoDe_Y_(num, exp):
        
























