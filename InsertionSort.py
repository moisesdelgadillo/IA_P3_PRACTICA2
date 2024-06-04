# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:02:42 2024

@author: moise
"""

# METODO DE ORDENAMIENTO (INSERTION SORT)
# Insertion Sort construye la lista ordenada de uno en uno, insertando cada nuevo elemento en su 
# posición correcta.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Ejemplo de uso
lista = [12, 11, 13, 5, 6, 3, 1,  25, 35, 22, 66, 108, 99, 199]
print("Lista desordenada:", lista)
lista_ordenada = insertion_sort(lista)
print("Lista ordenada:", lista_ordenada)
