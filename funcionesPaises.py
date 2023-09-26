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
    lista=[]
    with open('paises.txt', encoding='utf-8') as archivo:  
        lector = csv.reader(archivo)
        for fila in lector:
            if "'" in fila[6]:
                fila[6]=fila[6].replace("'"," '' ")
                lista.append(fila)
            else:
                lista.append(fila)
    return crearListaString(lista)


def crearListaString(lista):
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

def generarPaisesContinente(paises):

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

        
        ordenarPais = sorted(paises, key=lambda x: x[0])

        for pos, pais in enumerate(ordenarPais):
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

    print(f"Archivo HTML 'paises por continente.html' creado con " + str(len(ordenarPais)) + " registros.")

# Función para generar el archivo HTML
def generarPaisesPoblacion(paises):
    # Ordenar la lista de países por población de mayor a menor
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
    # Ordenar la lista de países por área en metros cuadrados de mayor a menor
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
    # Filtrar los países especificados
    paisesEspecificados = ["United States", "Costa Rica", "Italy", "Greece", "Japan"]

    paises_filtrados = [pais for pais in paises if pais[0] in paisesEspecificados]
    
    paises_filtrados=sorted(paises_filtrados, key=lambda x: int(x[1][4]))
    
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

        for pos,pais in enumerate(paises_filtrados):
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

    print(f'Archivo HTML "paises zonas azules.html" creado con {len(paises_filtrados)} registros.')

def extraerIdiomas(lista):
    idiomas = []
    for pais in lista:
        idiomasPais = pais[7]  
        idiomas.append(idiomasPais)
    return dividirPaises(idiomas,True)

def dividirPaises(idiomas,boolean):
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
    idiomas=[]
    for idioma in idiomasDivididos: 
        if "-" in idioma:
            idiomas.append(idioma[:2])  
        else:
            idiomas.append(idioma)
    return eliminarRepetidos(idiomas)

def eliminarRepetidos(idiomas):
    idiomasDivididos=[]
    for idioma in idiomas:
        if idioma not in idiomasDivididos:
            idiomasDivididos.append(idioma)

    return idiomasDivididos

def extraerIdiomasNombre(lista,nombre):
    idiomas=[]
    for pais in lista:
        if nombre == pais[0]:
            idiomas=dividirPaises(pais[7],False)
    return idiomas


def generarPaisesIdiomas(paises):
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

def extraerInfo(listaStrings,opcion):
    moneda=[]
    buscar=""
    for pais in listaStrings:
        if opcion == 1:
            buscar=pais[2]
        elif opcion == 2:
            buscar=pais[5][0]
        elif opcion == 3:
            buscar=pais[0]
        if buscar not in moneda:
            moneda.append(buscar)
    return moneda
    

def generarMismaMoneda(nombre,listaStrings):
    infoHtml=[]
    for pais in listaStrings:
        if nombre == pais[2]:
            infoHtml.append(pais[5][0],pais[0],pais[4],pais[7])
    
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

