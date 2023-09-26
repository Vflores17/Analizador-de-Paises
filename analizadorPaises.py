######################################################
#  Elaborado por: Vidal Flores y Luis Aguilar       ##
#  Fecha de Creación: 19/09/2023 14:31              ##
#  Fecha de última Modificación: 19/09/2023 14:31   ##
#  Versión: 3.10.4                                  ##
######################################################

#importación de librerías
from funcionesPaises import *


#Definición de funciones
def submenuCodigos(continente,listaStrings):
    """
    Funcionamiento: Esta función muestra un menú que permite al usuario seleccionar un continente y luego 
        genera códigos de países que pertenecen a ese continente a partir de la lista de datos proporcionada.
    Entradas:
    -(str) continente: El continente seleccionado para el menú de códigos de países.
    -(list) listaStrings: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero genera códigos de países del continente seleccionado."""
    while True:
        i=1
        paisesMenu=[]
        for pais in listaStrings:
            if pais[5][0] == continente:
                paisesMenu.append(pais[0])
        print("""
        ******* Submenú códigos de un determinado país. *******
        Escoja una opción:\n""")
        for i,continente in enumerate(paisesMenu,start=1):
            print("      " + str(i) + ". "+continente)
        print("      " + str(len(paisesMenu)+1) + ". Salir del menú\n")
        try:
            opcion=int(input("Escoja una opción: "))
            if 1<=opcion<=len(paisesMenu):
                generarCodigosPais(paisesMenu[opcion-1],listaStrings)
                return
            elif opcion == len(paisesMenu)+1:
                print("""
                    ***** Has salido del submenú de códigos de un determinado país. *****
                        """)
                break
            else:
                print("\nOpcion inválida.")
                break
        except:
            print("\nDebe ingresar solamente valores númericos.")
            break

    return


def opcionMenuContinentes(listaStrings,camino):
    """
    Funcionamiento: Esta función muestra un menú de continentes disponibles y permite al usuario seleccionar un continente. 
        Dependiendo de la opción de "camino" proporcionada (1 o 2), la función puede generar una lista de países por continente o abrir el menú de códigos de un país para el continente seleccionado.
    Entradas:
    -(list) listaStrings: Una lista de datos de países en formato especial.
    -(int) camino: Un valor que indica si el usuario eligió generar países o códigos de países.
    Salidas:
    -(NA) No tiene salidas directas, pero permite al usuario seleccionar un continente y realizar operaciones según la opción elegida.
    """
    while True:
        continentes=extraerInfo(listaStrings,2)
        i=1
        print("""
        ******* Submenú de los continentes disponibles. *******
        Escoja una opción:\n""")
        for i,continente in enumerate(continentes,start=1):
            print("      " + str(i) + ". "+continente)
        print("      " + str(len(continentes)+1) + ". Salir del menú\n")
        try:
            opcion=int(input("Escoja una opción: "))
            if 1<=opcion<=len(continentes):
                if camino == 1:
                    generarPaisesContinente(continentes[opcion-1],listaStrings)
                else:
                    submenuCodigos(continentes[opcion-1],listaStrings)
            elif opcion == len(continentes)+1:
                print("""
                    ***** Has salido del submenú de los continentes. *****
                        """)
                break
            else:
                print("\nOpcion inválida.")
        except:
            print("\nDebe ingresar solamente valores númericos.")

    return




def opcionPagoMismaMoneda(listaStrings):
    """
    Funcionamiento: Esta función muestra un menú de monedas utilizadas en países y permite al usuario seleccionar una moneda. 
        Luego, genera información sobre los países que utilizan la misma moneda a partir de la lista de datos proporcionada.
    Entradas:
    -(list) listaStrings: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero permite al usuario seleccionar una moneda y generar información sobre los países que utilizan la misma moneda.
    """
    while True:
        monedas=extraerMoneda(listaStrings)
        i=1
        print("""
        ******* Submenú países con la misma moneda. *******
        Escoja una opción:\n""")
        for i,moneda in enumerate(monedas,start=1):
            if moneda[1]>=3:
                print("      " + str(i) + ". "+moneda[0])
        print("      " + str(len(monedas)+1) + ". para salir menú")
        try:
            opcion=int(input("Escoja una opción: "))
            if 1<=opcion<=len(monedas):
                generarMismaMoneda(monedas[opcion-1][0], listaStrings)
            elif opcion == len(monedas)+1:
                print("""
                    ***** Has salido del submenú de países con la misma moneda. *****
                        """)
                break
            else:
                print("\nOpcion inválida.")
        except:
            print("\nDebe ingresar solamente valores númericos.")

    return

def opcionCrearEstructura():
    """
    Funcionamiento: Esta función carga una lista de datos de países desde un archivo y la devuelve como resultado. 
        Antes de utilizar otras funciones que dependen de estos datos, se debe llamar a esta función para cargar la estructura.
    Entradas:
    -(NA) No tiene entradas.
    Salidas:
    -(list) listaStrings: Una lista de datos de países en formato especial.
    """
    listaStrings=leerArchivo()
    print("\n***** Se han cargado " + str(len(listaStrings)) + " registros. *****\n")
    return listaStrings

def opcionGenerarXml(listaStrings):
    """
    Funcionamiento: Esta función toma la lista de datos de países y genera un archivo XML a partir de estos datos. 
        El archivo XML contendrá información sobre los países.
    Entradas:
    -(list) listaStrings: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero genera un archivo XML a partir de los datos proporcionados.
    """
    if crearXml(listaStrings):
        print("""
     *****  Archivo XML generado exitosamente.  ******""")
        return


def opcionGenerarHtml(listaStrings):
    """
    Funcionamiento: Esta función muestra un menú que permite al usuario seleccionar una opción para generar contenido HTML relacionado con los datos de los países.
    Entradas:
    -(list) listaStrings: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero permite al usuario seleccionar una opción y generar contenido HTML relacionado con los datos de los países.
    """
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
        try:
            opcion=int(input("Escoja una opción: "))
            if opcion>=1 and opcion<=9:
                if opcion == 1:
                    opcionMenuContinentes(listaStrings,1)
                elif opcion == 2:
                    generarPaisesPoblacion(listaStrings)
                elif opcion == 3:
                    generarTamannoPaises(listaStrings)
                elif opcion == 4:
                    generarZonasAzules(listaStrings)  
                elif opcion == 5:
                    generarPaisesIdiomas(listaStrings)
                elif opcion == 6:
                    opcionPagoMismaMoneda(listaStrings)
                elif opcion == 7:
                    opcionMenuContinentes(listaStrings,2)
                elif opcion == 8:
                    generarHablantesIdioma(listaStrings)
                else:
                    print("""
            *************** Has salido del submenú ******************************
                        """)
                
                    break 
            else:
                print("\nOpción inválida") 
        except:
            print("\nDebes ingresar solamente valores númericos.")


def menu():
    """
    Funcionamiento: Esta función proporciona un menú principal para que el usuario elija entre varias opciones, como crear estructura, generar XML, generar HTML o salir del programa.
    Entradas:
    -(NA) No tiene entradas.
    Salidas:
    -(NA) No tiene salidas directas, pero permite al usuario interactuar con el programa y realizar diversas operaciones relacionadas con datos de países.
    """
    listaStrings = [] 

    while True:
        print("""
**************************************************************\n
    ¡Bienvenido al analizador de paises!
    By: Vidal Flores & Luis Aguilar\n

    Opciones a elegir.
    1. Crear estructura.
    2. Generar XML.
    3. Construir HTML.
    4. Salir del programa
    """)
        try:
            opcion = int(input("Escoja una opción: "))

            if opcion == 1:
                listaStrings = opcionCrearEstructura()
            elif opcion == 2 and listaStrings!=[]:
                opcionGenerarXml(listaStrings)  
            elif opcion == 3 and listaStrings!=[]:
                opcionGenerarHtml(listaStrings) 
            elif opcion == 2 or opcion == 3 and listaStrings==[]:
                print("\nPrimero debes crear la estructura.")
            elif opcion == 4:
                print("""
    ～●～●～●～●～●～●～●～～●～●～●～●～●～●～●～●～●～●～～●～●～●～●～●～●～●～●～●～●～
                        
        Descubre más sobre el mundo cada vez que utilices nuestro analizador de países. 
                ¡Hay tantos datos interesantes por explorar!\n

    ～●～●～●～●～●～●～●～～●～●～●～●～●～●～●～●～●～●～～●～●～●～●～●～●～●～●～●～●～
                        
    *************** FIN DEL PROGRAMA ******************************
            """)
                break
            else:
                print("\nOpción inválida")
        except:
            print("\nDebe ingresar solamente valores númericos.")

#Inicio del Programa Principal
menu()