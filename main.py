import re
import os
import time
import datetime
import math
from pathlib import Path

inicio = time.time()

ruta = './Directorio'

patron = r'N\D{3}-\d{5}'

today = datetime.date.today()

numeros_encontrados = []
archivos_encontrados = []


def buscar_numero(ruta, patron):
    archivo = open(ruta, 'r')
    texto = archivo.read()
    
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''
    

def  crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), patron)
            if resultado != '':
                numeros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    
    print('')
    print('_' * 50)
    print(f'Fecha: {today.day}/{today.month}/{today.year}')
    print('')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('_____________\t\t__________')
    
    for a in archivos_encontrados:
        print(f'{a}\t\t{numeros_encontrados[indice]}')
        indice += 1
    print('')
    
    print(f'Numeros encontrados: {len(numeros_encontrados)}')
    
    fin = time.time()
    duracion = fin - inicio
    
    print(f'Duracion de la busqueda: {math.ceil(duracion)}s')
    
    print('_' * 50)


crear_listas()
mostrar_todo()