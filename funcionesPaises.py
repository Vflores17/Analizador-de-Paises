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

def crearHtml(nombre):
    with open(str(nombre)+'.html','w', encoding='utf-8') as archivoHTML:
        archivoHTML.write('<!DOCTYPE html>')
    return True

def agregarInfoHtml(lista,archivo):
    with open(archivo,encoding='utf-8') as archivoHtml:
        archivoHtml.write("<html lang="+str(es)+">")
        archivoHtml.write("<head>")
        archivoHtml.write("<title> Países azules del mundo </title>")
        archivoHtml.write("/title")
        archivoHtml.write("<body>")
        archivoHtml.write("<header>")
        archivoHtml.write("<h1> Países azules del mundo. By Vidal Flores & Luis Aguilar </h1>")
        archivoHtml.write("<section>")
        for i in range(len(lista)):
            archivoHtml.write(lista[i])
        print("archivo creado")
    return

def hacerPaisesAzules(lista):
    crearHtml("paisesAzules")
    for i in range (len(lista)):
        if "United States" in lista[i][1]:


    
    
        return