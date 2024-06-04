# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:02:42 2024

@author: moise
"""

# METODO DE ORDENAMIENTO NATURAL MERGING (MERGE SORT)
# El "Natural Merging" es una variante del Merge Sort utilizada en ordenamiento externo. 
# En este método, se identifican y fusionan secuencias ya ordenadas (runs) en lugar de dividir 
# el archivo en bloques de tamaño fijo. Aquí tienes una implementación básica y simplificada de 
# "Natural Merging" en Python para ilustrar cómo funcionaría este proceso en un entorno limitado 
# por la memoria principal.

def identificar_runs(nombre_archivo):
    runs = []
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        run_actual = [lineas[0]]
        
        for i in range(1, len(lineas)):
            if lineas[i] >= lineas[i - 1]:
                run_actual.append(lineas[i])
            else:
                runs.append(run_actual)
                run_actual = [lineas[i]]
        runs.append(run_actual)  # Añadir el último run

    for i, run in enumerate(runs):
        with open(f'run_{i}.txt', 'w') as archivo_run:
            archivo_run.writelines(run)

# Ejemplo de uso
identificar_runs('datos.txt')
