# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:02:42 2024

@author: moise
"""

# METODO DE ORDENAMIENTO (BUBBLE SORT)
# El algoritmo Bubble Sort compara elementos adyacentes y los intercambia si están en el orden incorrecto. 
# Este proceso se repite hasta que la lista esté ordenada.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista desordenada:", lista)
lista_ordenada = bubble_sort(lista)
print("Lista ordenada:", lista_ordenada)