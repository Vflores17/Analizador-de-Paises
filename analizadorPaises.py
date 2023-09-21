######################################################
#  Elaborado por: Vidal Flores y Luis Aguilar       ##
#  Fecha de Creación: 19/09/2023 14:31              ##
#  Fecha de última Modificación: 19/09/2023 14:31   ##
#  Versión: 3.10.4                                  ##
######################################################

#importación de librerías
from funcionesPaises import *


def opcionCrearEstructura():
    return

def opcionGenerarXML():
    return

def opcionGenerarHTML():
    return  


#función para el manejo del menú.
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado.
    """
    print ("""
**************************************************************\n
    ¡Bienvenido al analizador de paises!\n
    By: Vidal Flores & Luis Aguilar\n

    Opciones a elegir.\n
    1. Crear estructura.\n
    2. Generar XML.\n
    3. Generar un HTML.\n
    4. Salir del programa
    """)
    opcion = int (input ("Escoja una opción: "))
    if opcion >=0 and opcion <=4:
        if opcion == 1:
            opcion
        elif opcion == 2:
            opcion
        elif opcion == 3:
            opcion
        else:
            print("""---------\nDescubre más sobre el mundo cada vez que utilices
nuestro analizador de países. ¡Hay tantos datos interesantes por explorar!\n

        *************** FIN DEL PROGRAMA ******************************
        """)
            
            return
    else:
        print ("Opción inválida")
    menu()

#inicio del Programa Principal
menu()