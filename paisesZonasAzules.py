import csv
from html import escape

# Leer el archivo
with open("paises.txt", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    paises = list(reader)

paisesEspecificados = ["United States", "Costa Rica", "Italy", "Greece", "Japan"]

# Función para generar el archivo HTML
def generarZonasAzules(paises):
    # Filtrar los países especificados
    paises_filtrados = [pais for pais in paises if pais["countryName"] in paisesEspecificados]

    with open("paisesZonaAzul.html", "w") as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información de Países Especificados</title>
                           </head>
                           <body>
                               <h1>Información de Países Especificados</h1>
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
                                <td>{pais["geonameId"]}</td>
                                <td>{pais["countryName"]}</td>
                                <td>{pais["currencyCode"]}</td>
                                <td>{pais["languages"]}</td>
                                <td>{pais["capital"]}</td>
                                <td>{pais["population"]}</td>
                                <td>{pais["areaInSqKm"]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </body>
                       </html>''')

    print(f'Archivo HTML "paisesZonaAzul.html" creado con {len(paises_filtrados)} registros.')

# Llama a la función para generar el archivo HTML ordenado por área en metros cuadrados
generarZonasAzules(paises)
