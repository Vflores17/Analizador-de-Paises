import csv
from html import escape

# Leer el archivo
with open("paises.txt", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    paises = list(reader)

# Función para generar el archivo HTML
def generarPaisesPoblacion(paises):
    # Ordenar la lista de países por población de mayor a menor
    ordenarPais = sorted(paises, key=lambda x: int(x["population"]), reverse=True)

    with open("paisesPoblacion.html", "w") as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información de Países</title>
                           </head>
                           <body>
                               <h1>Información de Países Ordenada por Población</h1>
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
                                <td>{pais["population"]}</td>
                                <td>{pais["isoAlpha3"]}</td>
                                <td>{pais["countryName"]}</td>
                                <td>{pais["areaInSqKm"]}</td>
                                <td>{pais["continentName"]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </body>
                       </html>''')

    print(f'Archivo HTML "paisesPoblacion.html" creado con {len(ordenarPais)} registros.')

# Llama a la función para generar el archivo HTML ordenado por población
generarPaisesPoblacion(paises)
