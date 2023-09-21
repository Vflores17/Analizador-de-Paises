######################################################
#  Elaborado por: Vidal Flores y Luis Aguilar       ##
#  Fecha de Creación: 20/09/2023 17:18              ##
#  Fecha de última Modificación: 20/09/2023 :   ##
#  Versión: 3.10.4                                  ##
######################################################

#importación de librerías
import csv

def leerArchivo():
    with open('paises.txt', encoding='utf-8') as File:  
        reader = csv.reader(File)
        for row in reader:
            print(row)
    return

leerArchivo()

