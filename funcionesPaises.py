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

    with open("paisesPorContinente.html", "w",encoding='utf-8') as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información de Países</title>
                           </head>
                           <body>
                               <h1>Información de Países</h1>
                                <center>
                               <table border='1'>
                                   <tr>
                                       <th>aCódigo del país</th>
                                       <th>Nombre del País</th>
                                       <th>Capital</th>
                                       <th>Población</th>
                                       <th>Área (m²)</th>
                                   </tr>\n''')

        
        ordenarPais = sorted(paises, key=lambda x: x[0])

        for pais in ordenarPais:
            htmlfile.write(f'''<tr>
                                <td>{pais[1][0]}</td>
                                <td>{pais[0]}</td>
                                <td>{pais[4]}</td>
                                <td>{pais[3]}</td>
                                <td>{pais[6]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')

    print(f'Archivo HTML "paisesPorContinente.html" creado con {len(ordenarPais)} registros.')

# Función para generar el archivo HTML
def generarPaisesPoblacion(paises):
    # Ordenar la lista de países por población de mayor a menor
    ordenarPais = sorted(paises, key=lambda x: int(x[3]), reverse=True)

    with open("paisesPoblacion.html", "w",encoding='utf-8') as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información de Países</title>
                           </head>
                           <body>
                               <h1>Información de Países Ordenada por Población</h1>
                                <center>
                               <table border='1'>
                                   <tr>
                                       <th>Población</th>
                                       <th>isoAlpha3</th>
                                       <th>Nombre del País</th>
                                       <th>Área (m²)</th>
                                       <th>Nombre del Continente</th>
                                   </tr>\n''')

        for pais in ordenarPais:
            htmlfile.write(f'''<tr>
                                <td>{pais[3]}</td>
                                <td>{pais[1][3]}</td>
                                <td>{pais[0]}</td>
                                <td>{pais[6]}</td>
                                <td>{pais[5][0]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')

    print(f'Archivo HTML "paisesPoblacion.html" creado con {len(ordenarPais)} registros.')

def generarTamannoPaises(paises):
    # Ordenar la lista de países por área en metros cuadrados de mayor a menor
    ordenarPais = sorted(paises, key=lambda x: float(x[6]), reverse=True)

    with open("paisesPorArea.html", "w") as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Países por Área en Metros Cuadrados</title>
                           </head>
                           <body>
                               <h1>Países por Área en Metros Cuadrados</h1>
                                <center>
                               <table border='1'>
                                   <tr>
                                       <th>Área en Metros Cuadrados</th>
                                       <th>Código FIPS</th>
                                       <th>Nombre del País</th>
                                       <th>Nombre del Continente</th>
                                   </tr>\n''')

        for pais in ordenarPais:
            htmlfile.write(f'''<tr>
                                <td>{pais[6]}</td>
                                <td>{pais[1][1]}</td>
                                <td>{pais[0]}</td>
                                <td>{pais[5][0]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')

    print(f'Archivo HTML "paisesPorArea.html" creado con {len(ordenarPais)} registros.')

def generarZonasAzules(paises):
    # Filtrar los países especificados
    paisesEspecificados = ["United States", "Costa Rica", "Italy", "Greece", "Japan"]

    paises_filtrados = [pais for pais in paises if pais[0] in paisesEspecificados]
    paises_filtrados=sorted(paises, key=lambda x: int(x[1][4]))
    with open("paisesZonaAzul.html", "w",encoding='utf-8') as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información de Países Especificados</title>
                           </head>
                           <body>
                               <h1>Información de Países Especificados</h1>
                                <center>
                               <table border='1'>
                                   <tr>
                                       <th>geonameId</th>
                                       <th>Nombre del País</th>
                                       <th>currencyCode</th>
                                       <th>languages</th>
                                       <th>capital</th>
                                       <th>population</th>
                                       <th>areaInSqKm</th>
                                   </tr>\n''')

        for pais in paises_filtrados:
            htmlfile.write(f'''<tr>
                                <td>{pais[1][4]}</td>
                                <td>{pais[0]}</td>
                                <td>{pais[2]}</td>
                                <td>{pais[7]}</td>
                                <td>{pais[4]}</td>
                                <td>{pais[3]}</td>
                                <td>{pais[6]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </center>
                       </body>
                       </html>''')

    print(f'Archivo HTML "paisesZonaAzul.html" creado con {len(paises_filtrados)} registros.')
