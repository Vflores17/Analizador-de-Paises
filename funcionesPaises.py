######################################################
#  Elaborado por: Vidal Flores y Luis Aguilar       ##
#  Fecha de Creación: 20/09/2023 17:18              ##
#  Fecha de última Modificación: 20/09/2023 :   ##
#  Versión: 3.10.4                                  ##
######################################################

#importación de librerías
import csv

#Función para leer un archivo csv

def leerArchivo():
    with open('paises.txt', encoding='utf-8') as archivo:  
        lista = csv.reader(archivo)
    return lista



