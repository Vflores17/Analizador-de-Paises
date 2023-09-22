######################################################
#  Elaborado por: Vidal Flores y Luis Aguilar       ##
#  Fecha de Creación: 19/09/2023 14:31              ##
#  Fecha de última Modificación: 19/09/2023 14:31   ##
#  Versión: 3.10.4                                  ##
######################################################

#importación de librerías
from funcionesPaises import *


def opcionCrearEstructura():
    listaStrings=leerArchivo()
    print("""
    ***** Se han leído los datos del archivo exitosamente. *****
    """)
    return listaStrings

def opcionGenerarXML(listaStrings):
    print(listaStrings)
    return ""


def opcionGenerarHTML():
    return  


#función para el manejo del menú.
def menu():
    listaStrings = [] 

    while True:
        print("""
**************************************************************\n
    ¡Bienvenido al analizador de paises!
    By: Vidal Flores & Luis Aguilar\n

    Opciones a elegir.
    1. Crear estructura.
    2. Generar XML.
    3. Generar un HTML.
    4. Salir del programa
    """)
        opcion = int(input("Escoja una opción: "))

        if opcion == 1:
            listaStrings = opcionCrearEstructura()  # Almacena la lista devuelta
        elif opcion and listaStrings!=[]:
            opcionGenerarXML(listaStrings)  # Pasa la lista como parámetro
        elif opcion and listaStrings!=[]:
            opcionGenerarHTML(listaStrings)  # Pasa la lista como parámetro
        elif opcion == 2 or opcion == 3 and listaStrings==[]:
            print("\nPrimero debes crear la estructura.")
        elif opcion == 4:
            print("""
---------\nDescubre más sobre el mundo cada vez que utilices
nuestro analizador de países. ¡Hay tantos datos interesantes por explorar!\n

        *************** FIN DEL PROGRAMA ******************************
        """)
            break
        else:
            print("Opción inválida")

#inicio del Programa Principal
menu()