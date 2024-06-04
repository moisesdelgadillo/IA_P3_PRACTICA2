# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:02:42 2024

@author: moise
"""

# METODO DE ORDENAMIENTO (QUICK SORT)
# Quick Sort es un algoritmo de divide y vencerás que selecciona un "pivote" y reordena los elementos 
# de la lista de manera que todos los elementos menores que el pivote se colocan antes que este, y 
# todos los elementos mayores se colocan después. Luego, se aplica recursivamente el mismo proceso a 
# las sublistas.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Ejemplo de uso
lista = [3, 6, 8, 10, 1, 2, 1]
print("Lista desordenada:", lista)
lista_ordenada = quick_sort(lista)
print("Lista ordenada:", lista_ordenada)