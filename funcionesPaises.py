######################################################
#  Elaborado por: Vidal Flores y Luis Aguilar       ##
#  Fecha de Creación: 19/09/2023 14:31              ##
#  Fecha de última Modificación: 19/09/2023 14:31   ##
#  Versión: 3.10.4                                  ##
######################################################

#importación de librerías
import csv

#Definición de funciones

def leerArchivo():
    """
    Funcionamiento: Esta función lee un archivo CSV llamado 'paises.csv' y procesa los datos, reemplazando las comillas simples (') 
        por dos comillas simples ('') si están presentes en el archivo. Luego, convierte los datos en una lista de cadenas y devuelve esa lista.
    Entradas:
    -(NA) No tiene entradas.
    Salidas:
    -(list) listaStrings: Una lista de datos de países en formato especial.
    """
    lista=[]
    with open('paises.csv', encoding='utf-8') as archivo:  
        lector = csv.reader(archivo)
        for fila in lector:
            if "'" in fila[6]:
                fila[6]=fila[6].replace("'"," '' ")
                lista.append(fila)
            else:
                lista.append(fila)
    return crearListaString(lista)


def crearListaString(lista):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y la reorganiza en una estructura diferente, 
        convirtiéndola en una lista de listas de cadenas.
    Entradas:
    -(list) lista: Una lista de datos de países en formato especial.
    Salidas:
    -(list) listaStrings: Una lista de listas de cadenas que representa los datos de países reorganizados.
    """
    listaStrings=[]
    fila=[]
    for i in range(1,len(lista)):
        fila.append(lista[i][1])
        fila.append([lista[i][0]]+[lista[i][4]]+[lista[i][5]]+[lista[i][11]]+[lista[i][12]])
        fila.append(lista[i][2])
        fila.append(lista[i][3])
        fila.append(lista[i][6])
        fila.append([lista[i][7]]+[lista[i][8]])
        fila.append(lista[i][9])
        fila.append([lista[i][10]])
        listaStrings.append(fila)
        fila=[]
    return listaStrings


def crearXml(lista):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y genera un archivo XML llamado 'paises.xml' a partir de estos datos. 
        El archivo XML contiene información sobre los países.
    Entradas:
    -(list) lista: Una lista de datos de países en formato especial.
    Salidas:
    -(bool) True: Indica que el archivo XML se ha generado con éxito.
    """
    with open('paises.xml', 'w',encoding='utf-8') as archivoXML:  
        archivoXML.write('<?xml version="1.0" encoding="UTF-8"?>')
        archivoXML.write('<paises>\n')
        for i in range(0,len(lista)):
            archivoXML.write('<pais>\n')
            archivoXML.write('\t<nombrePais>'+str(lista[i][0])+'</nombrePais>\n')
            archivoXML.write('\t<codigosPais>'+str(lista[i][1])+'</codigosPais>\n')
            archivoXML.write('\t<monedaPais>'+str(lista[i][2])+'</monedaPais>\n')
            archivoXML.write('\t<poblacionPais>'+str(lista[i][3])+'</poblacionPais>\n')
            archivoXML.write('\t<capitalPais>'+str(lista[i][4])+'</capitalPais>\n')
            archivoXML.write('\t<continentePais>'+str(lista[i][5])+'</continentePais>\n')
            archivoXML.write('\t<areaPais>'+str(lista[i][6])+'</areaPais>\n')
            archivoXML.write('\t<lenguajesPais>'+str(lista[i][7])+'</lenguajesPais>\n')
            archivoXML.write('</pais>\n')
        archivoXML.write('</paises>\n')
    return True

def generarPaisesContinente(continente,listaStrings):
    """
    Funcionamiento: Esta función toma un continente y una lista de datos de países en formato especial y genera un archivo HTML llamado 'paises por continente.html'. 
        El archivo HTML contiene información sobre los países que pertenecen al continente especificado.
    Entradas:
    -(str) continente: El continente seleccionado para generar el archivo HTML.
    -(list) listaStrings: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero genera un archivo HTML con la información de los países del continente seleccionado.
    """
    infoHtml=[]
    for pais in listaStrings:
        if continente == pais[5][0]:
            infoHtml.append(pais)
    with open("paises por continente.html", "w",encoding='utf-8') as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información sobre los países</title>
                           </head>
                           <body>
                               <h1>Países por continentes</h1>
                                <center>
                               <table border='1'>
                                   <tr bgcolor="0C9208">
                                       <th style="color: white;">Código del país</th>
                                       <th style="color: white;">Nombre del País</th>
                                       <th style="color: white;">Capital</th>
                                       <th style="color: white;">Población</th>
                                       <th style="color: white;">Área (m²)</th>
                                   </tr>\n''')

        
        infoHtml = sorted(infoHtml, key=lambda x: x[1])

        for pos, pais in enumerate(infoHtml):
            if pos%2==0:
                colorFila="D7BCE9"
            else:
                colorFila="CCFAF4"

            htmlfile.write(f'''<tr style= "background-color: {colorFila};">
                                <td align="center">{pais[1][0]}</td>
                                <td align="center">{pais[0]}</td>
                                <td align="center">{pais[4]}</td>
                                <td align="center">{pais[3]}</td>
                                <td align="center">{pais[6]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')

    print(f"Archivo HTML 'paises por continente.html' creado con " + str(len(infoHtml)) + " registros.")


def generarPaisesPoblacion(paises):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y genera un archivo HTML llamado 'cuantos Viven.html'. 
        El archivo HTML muestra información sobre la población de los países, ordenados de mayor a menor.
    Entradas:
    -(list) paises: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero genera un archivo HTML con información sobre la población de los países.
    """
    
    ordenarPais = sorted(paises, key=lambda x: int(x[3]), reverse=True)

    with open("cuantos Viven.html", "w",encoding='utf-8') as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información sobre los Países</title>
                           </head>
                           <body>
                               <h1>¿Cuántos viven?</h1>
                                <center>
                               <table border='1'>
                                   <tr bgcolor="0C9208">
                                       <th style="color: white;">Población</th>
                                       <th style="color: white;">isoAlpha3</th>
                                       <th style="color: white;">Nombre del País</th>
                                       <th style="color: white;">Área (m²)</th>
                                       <th style="color: white;">Nombre del Continente</th>
                                   </tr>\n''')

        for pos,pais in enumerate(ordenarPais):
            if pos%2==0:
                colorFila="D7BCE9"
            else:
                colorFila="CCFAF4"
            htmlfile.write(f'''<tr style= "background-color: {colorFila};">
                                <td align="center">{pais[3]}</td>
                                <td align="center">{pais[1][3]}</td>
                                <td align="center">{pais[0]}</td>
                                <td align="center">{pais[6]}</td>
                                <td align="center">{pais[5][0]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')

    print(f'Archivo HTML "¿cuántos Viven?.html" creado con {len(ordenarPais)} registros.')

def generarTamannoPaises(paises):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y genera un archivo HTML llamado 'De grandes a pequeños.html'. 
        El archivo HTML muestra información sobre el tamaño de los países, ordenados de mayor a menor en términos de área en metros cuadrados.
    Entradas:
    -(list) paises: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero genera un archivo HTML con información sobre el tamaño de los países.
    """
    
    ordenarPais = sorted(paises, key=lambda x: float(x[6]), reverse=True)

    with open("De grandes a pequeños.html", "w") as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información sobre los países</title>
                           </head>
                           <body>
                               <h1>De grandes a pequeños</h1>
                                <center>
                               <table border='1'>
                                   <tr bgcolor="0C9208">
                                       <th style="color: white;">Área en Metros Cuadrados</th>
                                       <th style="color: white;">Código FIPS</th>
                                       <th style="color: white;">Nombre del País</th>
                                       <th style="color: white;">Nombre del Continente</th>
                                   </tr>\n''')

        for pos, pais in enumerate(ordenarPais):
            if pos%2==0:
                colorFila="D7BCE9"
            else:
                colorFila="CCFAF4"
            htmlfile.write(f'''<tr style= "background-color: {colorFila};">
                                <td align="center">{pais[6]}</td>
                                <td align="center">{pais[1][1]}</td>
                                <td align="center">{pais[0]}</td>
                                <td align="center">{pais[5][0]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')

    print(f'Archivo HTML "De grandes a pequeños.html" creado con {len(ordenarPais)} registros.')

def generarZonasAzules(paises):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y genera un archivo HTML llamado 'paises zonas azules.html'. 
        El archivo HTML muestra información específica de los países que están en una lista predefinida.
    Entradas:
    -(list) paises: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero genera un archivo HTML con información sobre los países específicos de la lista.
    """
    
    paisesEspecificados = ["United States", "Costa Rica", "Italy", "Greece", "Japan"]

    paisesFiltrados = [pais for pais in paises if pais[0] in paisesEspecificados]
    
    paisesFiltrados=sorted(paisesFiltrados, key=lambda x: int(x[1][4]))
    
    with open("paises zonas azules.html", "w",encoding='utf-8') as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información sobre los Países</title>
                           </head>
                           <body>
                               <h1>Zonas azules</h1>
                                <center>
                               <table border='1'>
                                   <tr bgcolor="0C9208">
                                       <th style="color: white;">geonameId</th>
                                       <th style="color: white;">Nombre del País</th>
                                       <th style="color: white;">Código de moneda</th>
                                       <th style="color: white;">Lenguajes</th>
                                       <th style="color: white;">capital</th>
                                       <th style="color: white;">Población</th>
                                       <th style="color: white;">Área en Metros Cuadrados</th>
                                   </tr>\n''')

        for pos,pais in enumerate(paisesFiltrados):
            if pos%2==0:
                colorFila="D7BCE9"
            else:
                colorFila="CCFAF4"
            lenguajesTexto=', '.join(pais[7])
            htmlfile.write(f'''<tr  style= "background-color: {colorFila};">
                                <td align="center">{pais[1][4]}</td>
                                <td align="center">{pais[0]}</td>
                                <td align="center">{pais[2]}</td>
                                <td align="center">{lenguajesTexto}</td>
                                <td align="center">{pais[4]}</td>
                                <td align="center">{pais[3]}</td>
                                <td align="center">{pais[6]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')

    print(f'Archivo HTML "paises zonas azules.html" creado con {len(paisesFiltrados)} registros.')

def extraerInfo(listaStrings,opcion):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y una opción (1, 2 o 3) y 
        extrae información específica de los países en función de la opción seleccionada. Luego, devuelve una lista con la información extraída.
    Entradas:
    -(list) listaStrings: Una lista de datos de países en formato especial.
    -(int) opcion: La opción que determina qué información se debe extraer (1 para monedas, 2 para continentes, 3 para nombres de países).
    Salidas:
    -(list) info: Una lista con la información extraída según la opción seleccionada.
    """
    info=[]
    buscar=""
    for pais in listaStrings:
        if opcion == 1:
            buscar=pais[2]
        elif opcion == 2:
            buscar=pais[5][0]
        elif opcion == 3:
            buscar=pais[0]
        if buscar not in info:
            info.append(buscar)
    return info

def extraerIdiomas(lista):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y extrae los idiomas que se hablan en esos países. 
        Luego, devuelve una lista de los idiomas.
    Entradas:
    (list) lista: Una lista de datos de países en formato especial.
    Salidas:
    (list) idiomas: Una lista de idiomas extraídos de los países.
    """
    idiomas = []
    for pais in lista:
        idiomasPais = pais[7]  
        idiomas.append(idiomasPais)
    return dividirPaises(idiomas,True)

def dividirPaises(idiomas,boolean):
    """
    Funcionamiento: Esta función toma una lista de idiomas y, si es necesario, divide los idiomas separados por comas en elementos individuales. 
        Puede usarse para dividir los idiomas en cada país o para dividir una lista de idiomas.
    Entradas:
    -(list) idiomas: Una lista de idiomas o una lista de listas de idiomas.
    Salidas:
    -(list) idiomasDivididos: Una lista de idiomas divididos en elementos individuales.
    """
    idiomasDivididos=[]
    for lista in idiomas:
        if boolean:
            idiomasPais = lista[0]  
            if "," in idiomasPais:
                idiomasDivididos.extend(idiomasPais.split(","))  
            else:
                idiomasDivididos.append(idiomasPais)
        else:
            if "," in lista:
                idiomasDivididos.extend(lista.split(","))  
            else:
                idiomasDivididos.append(lista)
    return obtenerLenguaje(idiomasDivididos)


def obtenerLenguaje(idiomasDivididos):
    """
    Funcionamiento: Esta función toma una lista de idiomas divididos y, si es necesario, obtiene la versión de dos letras de cada idioma. 
        Puede usarse para obtener las versiones de dos letras de los idiomas de un país o de una lista de idiomas.
    Entradas:
    -(list) idiomasDivididos: Una lista de idiomas divididos.
    Salidas:
    -(list) idiomas: Una lista de versiones de dos letras de los idiomas.
    """
    idiomas=[]
    for idioma in idiomasDivididos: 
        if "-" in idioma:
            idiomas.append(idioma[:2])  
        else:
            idiomas.append(idioma)
    return eliminarRepetidos(idiomas)

def eliminarRepetidos(idiomas):
    """
    Funcionamiento: Esta función toma una lista de elementos y elimina los elementos duplicados, devolviendo una lista sin duplicados.
    Entradas:
    -(list) elementos: Una lista de elementos que pueden contener duplicados.
    Salidas:
    -(list) elementosDivididos: Una lista de elementos sin duplicados.
    """
    idiomasDivididos=[]
    for idioma in idiomas:
        if idioma not in idiomasDivididos:
            idiomasDivididos.append(idioma)

    return idiomasDivididos

def extraerIdiomasNombre(lista,nombre):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y un nombre de país y devuelve los idiomas que se hablan en ese país.
    Entradas:
    -(list) lista: Una lista de datos de países en formato especial.
    -(str) nombre: El nombre del país del cual se quieren extraer los idiomas.
    Salidas:
    -(list) idiomas: Una lista de idiomas hablados en el país especificado.
    """
    idiomas=[]
    for pais in lista:
        if nombre == pais[0]:
            idiomas=dividirPaises(pais[7],False)
    return idiomas


def generarPaisesIdiomas(paises):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y genera un archivo HTML llamado 'paises mismo idioma.html'. 
        El archivo HTML muestra información sobre los países que comparten el mismo idioma.
    Entradas:
    -(list) paises: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero genera un archivo HTML con información sobre los países que comparten el mismo idioma.
    """
    idiomas=extraerIdiomas(paises)
    infoHtml=[]
    for idioma in idiomas:
        cont=0
        paisesCont=[]
        continente=[]
        for pais in paises:
            idiomas=extraerIdiomasNombre(paises,pais[0])
            if idioma in idiomas:
                cont+=1
                paisesCont.append(pais[0])
                if pais[5][0] not in continente:
                    continente.append(pais[5][0])
        if cont>=3:
            infoHtml.append([idioma,cont,paisesCont,continente])

    with open("paises mismo idioma.html", "w",encoding='utf-8') as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información sobre los Países</title>
                           </head>
                           <body>
                               <h1>Países con el mismo idioma.</h1>
                                <center>
                               <table border='1'>
                                   <tr bgcolor="0C9208">
                                       <th style="color: white;">Idioma</th>
                                       <th style="color: white;">Cantidad de países</th>
                                       <th style="color: white;">Nombre de los Paises</th>
                                       <th style="color: white;">Nombre de los continentes</th>
                                   </tr>\n''')

        for pos,pais in enumerate(infoHtml):
            if pos%2==0:
                colorFila="D7BCE9"
            else:
                colorFila="CCFAF4"
            paisesTexto = ', '.join(pais[2])
            continenteTexto = ', '.join(pais[3])
            htmlfile.write(f'''<tr  style= "background-color: {colorFila};">
                                <td align="center">{pais[0]}</td>
                                <td align="center">{pais[1]}</td>
                                <td align="center">{paisesTexto}</td>
                                <td align="center">{continenteTexto}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')
    print(f'Archivo HTML "paises mismo idioma.html" creado con {len(infoHtml)} registros.')
    return

def extraerMoneda(listaStrings):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y extrae las monedas utilizadas en esos países, 
        contando cuántas veces se repite cada moneda.
    Entradas:
    (list) listaStrings: Una lista de datos de países en formato especial.
    Salidas:
    (list) menu: Una lista de monedas y su cantidad de ocurrencias, solo incluye las monedas que se repiten al menos 3 veces.
    """
    monedas=extraerInfo(listaStrings,1)
    opciones=[]
    for moneda in monedas:
        cont=0
        for pais in listaStrings:
            if moneda == pais[2]:
                cont+=1
        opciones.append([moneda,cont])
    menu=[]
    for opcion in opciones:
        if opcion[1]>=3:
            menu.append(opcion)
    return menu
    

def generarMismaMoneda(codigo,listaStrings):
    """
    Funcionamiento: Esta función toma un código de moneda y una lista de datos de países en formato especial y genera un archivo HTML llamado 'paises misma moneda.html'. 
        El archivo HTML muestra información sobre los países que utilizan la misma moneda.
    Entradas:
    -(str) codigo: El código de moneda para el cual se desea generar el archivo HTML.
    -(list) listaStrings: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero genera un archivo HTML con información sobre los países que utilizan la misma moneda.
    """
    infoHtml=[]
    for pais in listaStrings:
        if codigo == pais[2]:
            infoHtml.append([pais[5][0],pais[0],pais[4],pais[7]])
    
    with open("paises misma moneda.html", "w", encoding ="utf-8") as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <meta charset="UTF-8">
                               <title>Información sobre los Países</title>
                           </head>
                           <body>
                               <h1>Países con la misma moneda.</h1>
                                <center>
                               <table border='1'>
                                   <tr bgcolor="0C9208">
                                       <th style="color: white;">Nombre del continente.</th>
                                       <th style="color: white;">Nombre del país.</th>
                                       <th style="color: white;">Capital.</th>
                                       <th style="color: white;">Lenguajes.</th>
                                   </tr>\n''')

        for pos,pais in enumerate(infoHtml):
            if pos%2==0:
                colorFila="D7BCE9"
            else:
                colorFila="CCFAF4"
            lenguajesTexto=", ".join(pais[3])
            htmlfile.write(f'''<tr  style= "background-color: {colorFila};">
                                <td align="center">{pais[0]}</td>
                                <td align="center">{pais[1]}</td>
                                <td align="center">{pais[2]}</td>
                                <td align="center">{lenguajesTexto}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')
    print(f'Archivo HTML "paises misma moneda.html" creado con {len(infoHtml)} registros.')
    return


def generarCodigosPais(ppais,listaStrings):
    """
    Funcionamiento: Esta función toma el nombre de un país y una lista de datos de países en formato especial y genera un archivo HTML llamado 'paises codigo determinado.html'. 
        El archivo HTML muestra información sobre el país seleccionado, incluyendo sus códigos.
    Entradas:
    (str) ppais: El nombre del país para el cual se desea generar el archivo HTML.
    (list) listaStrings: Una lista de datos de países en formato especial.
    Salidas:
    (NA) No tiene salidas directas, pero genera un archivo HTML con información sobre el país seleccionado, incluyendo sus códigos.
    """
    infoHtml=[]
    for pais in listaStrings:
        if ppais == pais[0]:
            infoHtml.append(pais[5][0])
            infoHtml.append(pais[0])
            infoHtml.append(pais[1])
    with open("paises codigo determinado.html", "w", encoding ="utf-8") as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <meta charset="UTF-8">
                               <title>Información sobre los Países</title>
                           </head>
                           <body>
                               <h1>Códigos de un determinado país.</h1>
                                <center>
                               <table border='1'>
                                   <tr bgcolor="0C9208">
                                       <th style="color: white;">Nombre del continente.</th>
                                       <th style="color: white;">Nombre del país.</th>
                                       <th style="color: white;">Código de la moneda.</th>
                                       <th style="color: white;">Código fips.</th>
                                       <th style="color: white;">Isonumérico.</th>
                                       <th style="color: white;">isoAlpha3.</th>
                                       <th style="color: white;">geonameId.</th>
                                   </tr>\n''')

        colorFila="D7BCE9"
        htmlfile.write(f'''<tr  style= "background-color: {colorFila};">
                            <td align="center">{infoHtml[0]}</td>
                            <td align="center">{infoHtml[1]}</td>
                            <td align="center">{infoHtml[2][0]}</td>
                            <td align="center">{infoHtml[2][1]}</td>
                            <td align="center">{infoHtml[2][2]}</td>
                            <td align="center">{infoHtml[2][3]}</td>
                            <td align="center">{infoHtml[2][4]}</td>
                        </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')
    print(f'Archivo HTML "paises codigo determinado.html" creado con {str(1)} registro.')
    return

def generarHablantesIdioma(listaString):
    """
    Funcionamiento: Esta función toma una lista de datos de países en formato especial y genera un archivo HTML llamado 'hablantes por idioma.html'. 
        El archivo HTML muestra información sobre la cantidad de hablantes de cada idioma en función de la población de los países que lo hablan.
    Entradas:
    -(list) listaString: Una lista de datos de países en formato especial.
    Salidas:
    -(NA) No tiene salidas directas, pero genera un archivo HTML con información sobre la cantidad de hablantes de cada idioma.
    """
    idiomas=extraerIdiomas(listaString)
    infoHtml=[]
    for idioma in idiomas:
        cont=0
        for pais in listaString:
            idiomas=extraerIdiomasNombre(listaString,pais[0])
            if idioma in idiomas:
                cont+=int(pais[3])
        infoHtml.append([idioma,cont])

    with open("hablantes por idioma.html", "w",encoding='utf-8') as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información sobre los Países</title>
                           </head>
                           <body>
                               <h1>Hablantes por idioma.</h1>
                                <center>
                               <table border='1'>
                                   <tr bgcolor="0C9208">
                                       <th style="color: white;">Idioma</th>
                                       <th style="color: white;">Cantidad de hablantes</th>
                                   </tr>\n''')

        for pos,pais in enumerate(infoHtml):
            if pos%2==0:
                colorFila="D7BCE9"
            else:
                colorFila="CCFAF4"
            htmlfile.write(f'''<tr  style= "background-color: {colorFila};">
                                <td align="center">{pais[0]}</td>
                                <td align="center">{pais[1]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')
    print(f'Archivo HTML "hablantes por idioma.html" creado con {len(infoHtml)} registros.')
    return

