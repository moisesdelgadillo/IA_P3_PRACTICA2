# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:02:42 2024

@author: moise
"""

# METODO DE ORDENAMIENTO STRAIGHT MERGING (MERGE SORT)
# Merge Sort es un algoritmo de divide y vencerás que divide la lista en sublistas más pequeñas 
# hasta que cada sublista contiene un solo elemento, y luego las combina (mezcla) de manera ordenada.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encuentra el punto medio para dividir el array en dos mitades
        izquierda = arr[:mid]  # Crea la mitad izquierda
        derecha = arr[mid:]  # Crea la mitad derecha

        # Ordena cada mitad recursivamente
        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        # Copia los datos en los arrays temporales izquierda[] y derecha[]
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Verifica si queda algún elemento
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista desordenada:", lista)
merge_sort(lista)
print("Lista ordenada:", lista)
