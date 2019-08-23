def tablaDeMultiplicar():
    num = int(input("Dame un número: "))
    for i in range(1, 13):
        print(num, 'X', i, '=', num * i)
#tablaDeMultiplicar()
numeroA = 100
numeroB = 500
def cualEsMenor(num1, num2):
    if num1 == num2:
        print('Son iguales')
    elif num1 > num2:
        print(num2, ' es más chico')
    else:
        print(num1, ' es más chico')
#cualEsMenor(numeroA, numeroB)
def parImpar(num):
    if(num % 2 == 0):
        print(num, ' es par.')
    else:
        print(num, ' es impar.')
#parImpar(1000)
def numerosPares ():
    for num in range(1,101):
        if(num % 2 == 0 and num % 3 == 0):
            print(num)
#numerosPares()
def numerosConWhile ():
    i = 1
    while(i<101):
        print(i)
        i += 1
#numerosConWhile()
#Ejercicio 12
def numeroTriangular():
    num = int(input("Dame un índice y te diré el número triangular correspondiente: "))
    i = 1
    while(i<=num):
        print(i, "-", ((i*(i+1)) // 2))
        i+=1
#numeroTriangular()
def sumaPrimerosNumerosPares():
    num = int(input("Dame un número: "))
    contador = 0
    while(num != 0):
        num -= 1
        if(num % 2 ==0):
            contador += num
    print(contador)
def resolvente(a, b, c):
    print()

        