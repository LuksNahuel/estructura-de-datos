import numpy as np

def mergeSort(arr, inicio, final):
    if inicio != final:
        mitad = (inicio + final) // 2
        mergeSort(arr, inicio, mitad)
        mergeSort(arr, mitad + 1, final)
        merge(arr, inicio, final)

def merge(arr, inicio, final):
    
    mitad = (inicio + final) // 2
    
    aux = np.zeros(shape=len(arr), dtype = arr.dtype)
    
    i = j = 0
    
    
    
vector = np.array([1, 8, 4, 2, 5])
mergeSort(vector, 0, len(vector) - 1)