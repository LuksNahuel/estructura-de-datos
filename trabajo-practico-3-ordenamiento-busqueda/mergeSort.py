# -*- coding: utf-8 -*-
import numpy as np
#def mergeSort(vector, inicio, final):
#    if inicio + final > 1:
#        centro = (inicio + final) // 2
#        mergeSort(vector, inicio, centro)
#        mergeSort(vector, centro + 1, final)
#        merge(vector, inicio, final)
#
#def merge(vector, inicio, final):
#    

def mergeSort(arr):
    if len(arr) > 1:
        final = (len(arr) - 1)
        centro = (0 + final // 2)
        izq = arr[0:centro]
        der = arr[centro+1:final]
        
        mergeSort(izq)
        mergeSort(der)
        
        sort(izq, der)
    
def sort(v1, v2):
    largo = len(v1) + len(v2)
    aux = np.zeros(shape=(largo), dtype=v1.dtype)
    
    pos = 0
    i = 0
    j = 0
 
    while i<len(v1) and j<len(v2):
        if v1[i] < v2[j]:
            aux[pos] = v1[i]
            i += 1
        else:
            aux[pos] = v2[j]
            j += 1
        pos += 1
    
    if i == len(v1):    
        menor = v2[j]
        for index in range(j+1, len(v2)):
            if v2[index] < menor:
                aux[pos] = v2[index]
                j = index + 1
            else:
                aux[pos] = menor
            pos += 1
            aux[pos] = v2[j]
    
   
        
         
    
    
    return aux

vec = np.array([1, 3])
vec2 = np.array([4, 5])

ordenado = sort(vec, vec2)