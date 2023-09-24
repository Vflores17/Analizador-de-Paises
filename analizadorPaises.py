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

def opcionGenerarXml(listaStrings):
    if crearXml(listaStrings):
        print("""
     *****  Archivo XML generado exitosamente.  ******""")
        return


def opcionGenerarHtml(listaStrings):
    while True:
        print("""
        ***** Submenú para generar HTML. *************\n
        Escoja una opción:
            1. Países por continente.
            2. ¿Cuántos viven?
            3. De grandes a pequeños.
            4. Zonas Azules.
            5. Países con el mismo idioma.
            6. Pago con la misma moneda.
            7. Códigos de un determinado país.
            8. Hablantes por idioma.
            9. Salir del submenú.
        
        **********************************************
    """)
        opcion=int(input("Escoja una opción: "))
        if opcion>=1 and opcion<=9:
            if opcion == 1:
                generarPaisesContinente(listaStrings)
            elif opcion == 2:
                generarPaisesPoblacion(listaStrings)
            elif opcion == 3:
                generarTamannoPaises(listaStrings)
            elif opcion == 4:
                generarZonasAzules(listaStrings)  
            elif opcion == 5:
                print("Opcion 5")
            elif opcion == 6:
                print("Opción 6")
            elif opcion == 7:
                print("Opción 7")
            elif opcion == 8:
                print("Opción 8")
            else:
                print("""
        *************** Has salido del submenú ******************************
                      """)
            
                break 
        else:
            print("Opción inválida") 


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
            listaStrings = opcionCrearEstructura()
            print(listaStrings)  
        elif opcion == 2 and listaStrings!=[]:
            opcionGenerarXml(listaStrings)  
        elif opcion == 3 and listaStrings!=[]:
            opcionGenerarHtml(listaStrings) 
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