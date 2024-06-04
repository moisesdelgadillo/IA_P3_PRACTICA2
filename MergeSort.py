# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:02:42 2024

@author: moise
"""

# METODO DE ORDENAMIENTO (MERGE SORT)
# Merge Sort es un algoritmo de divide y vencerás que divide la lista en sublistas más pequeñas 
# hasta que cada sublista contiene un solo elemento, y luego las combina (mezcla) de manera ordenada.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Ejemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista desordenada:", lista)
lista_ordenada = merge_sort(lista)
print("Lista ordenada:", lista_ordenada)
