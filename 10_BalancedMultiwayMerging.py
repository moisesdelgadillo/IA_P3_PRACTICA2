# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:02:42 2024

@author: moise
"""

# METODO DE ORDENAMIENTO 

def dividir_en_runs(nombre_archivo, tamano_bloque):
    with open(nombre_archivo, 'r') as archivo:
        contador_bloque = 0
        while True:
            lineas = archivo.readlines(tamano_bloque)
            if not lineas:
                break
            with open(f'run_{contador_bloque}.txt', 'w') as bloque:
                bloque.writelines(sorted(lineas))
            contador_bloque += 1
    return contador_bloque  # Devuelve el número de bloques generados

# Ejemplo de uso
nombre_archivo = 'datos.txt'
tamano_bloque = 1000
num_bloques = dividir_en_runs(nombre_archivo, tamano_bloque)
