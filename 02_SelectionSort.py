# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:02:42 2024

@author: moise
"""

# METODO DE ORDENAMIENTO (SELECTION SORT)
# Selection Sort divide la lista en dos partes: una sublista de elementos ya ordenados y una sublista 
# de elementos por ordenar. En cada iteración, selecciona el elemento más pequeño de la sublista desordenada y 
# lo intercambia con el primer elemento de la sublista desordenada.

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ejemplo de uso
lista = [64, 25, 12, 22, 11]
print("Lista desordenada:", lista)
lista_ordenada = selection_sort(lista)
print("Lista ordenada:", lista_ordenada)
