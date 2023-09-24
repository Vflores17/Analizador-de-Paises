import csv
from html import escape

# Leer el archivo
with open("paises.txt", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    paises = list(reader)

# Función para generar el archivo HTML
def generarTamannoPaises(paises):
    # Ordenar la lista de países por área en metros cuadrados de mayor a menor
    ordenarPais = sorted(paises, key=lambda x: float(x["areaInSqKm"]), reverse=True)

    with open("paisesPorArea.html", "w") as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Países por Área en Metros Cuadrados</title>
                           </head>
                           <body>
                               <h1>Países por Área en Metros Cuadrados</h1>
                               <table border='1'>
                                   <tr>
                                       <th>Área en Metros Cuadrados</th>
                                       <th>Código FIPS</th>
                                       <th>Nombre del País</th>
                                       <th>Nombre del Continente</th>
                                   </tr>\n''')

        for pais in ordenarPais:
            htmlfile.write(f'''<tr>
                                <td>{pais["areaInSqKm"]}</td>
                                <td>{pais["fipsCode"]}</td>
                                <td>{pais["countryName"]}</td>
                                <td>{pais["continentName"]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </body>
                       </html>''')

    print(f'Archivo HTML "paisesPorArea.html" creado con {len(ordenarPais)} registros.')

# Llama a la función para generar el archivo HTML ordenado por área en metros cuadrados
generarTamannoPaises(paises)
