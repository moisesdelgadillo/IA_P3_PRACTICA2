# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:02:42 2024

@author: moise
"""

# METODO DE ORDENAMIENTO POLYPHASE SORT
# El "Polyphase Sort" es un algoritmo de ordenamiento externo que organiza datos en múltiples 
# fases de mezcla, utilizando un conjunto de buffers (fases) para mezclar y ordenar los datos.  

import heapq
import os

def polyphase_sort(nombre_archivo, tamano_buffer):
    # Dividir el archivo original en fases
    with open(nombre_archivo, 'r') as archivo:
        fase = 0
        while True:
            lineas = archivo.readlines(tamano_buffer)
            if not lineas:
                break
            lineas.sort()
            with open(f'fase_{fase}.txt', 'w') as fase_archivo:
                fase_archivo.writelines(lineas)
            fase += 1
    
    # Mezclar fases hasta que quede una sola fase
    while fase > 1:
        nueva_fase = 0
        for i in range(0, fase, 2):
            archivo1 = open(f'fase_{i}.txt', 'r')
            archivo2 = open(f'fase_{i+1}.txt', 'r') if i+1 < fase else None
            nueva_fase_archivo = open(f'fase_{nueva_fase}.txt', 'w')
            linea1 = archivo1.readline().strip()
            linea2 = archivo2.readline().strip() if archivo2 else None

            while linea1 or linea2:
                if linea1 and (not linea2 or linea1 <= linea2):
                    nueva_fase_archivo.write(linea1 + '\n')
                    linea1 = archivo1.readline().strip()
                else:
                    nueva_fase_archivo.write(linea2 + '\n')
                    linea2 = archivo2.readline().strip() if archivo2 else None

            archivo1.close()
            if archivo2:
                archivo2.close()
            nueva_fase_archivo.close()
            nueva_fase += 1
        
        # Eliminar archivos de fases anteriores
        for i in range(fase):
            os.remove(f'fase_{i}.txt')

        fase = nueva_fase

    # Renombrar el archivo final
    os.rename(f'fase_0.txt', 'datos_ordenados.txt')

# Ejemplo de uso
nombre_archivo = 'datos.txt'
tamano_buffer = 1000
polyphase_sort(nombre_archivo, tamano_buffer)
