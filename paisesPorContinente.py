import csv
from html import escape

# Leer el archivo
with open('paises.txt', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    paises = list(reader)

# Función para procesar la información y generar HTML
def generarPaisesContinente(paises):
    with open('paisesPorContinente.html', 'w') as htmlfile:
        htmlfile.write('''<html>
                           <head>
                               <title>Información de Países</title>
                           </head>
                           <body>
                               <h1>Información de Países</h1>
                               <table border='1'>
                                   <tr>
                                       <th>CountryCode</th>
                                       <th>Nombre del País</th>
                                       <th>Capital</th>
                                       <th>Población</th>
                                       <th>Área (m²)</th>
                                   </tr>\n''')

        # Ordenar la lista de países alfabéticamente por el nombre del país
        ordenarPais = sorted(paises, key=lambda x: x['countryName'])

        for pais in ordenarPais:
            htmlfile.write(f'''<tr>
                                <td>{pais["countryCode"]}</td>
                                <td>{pais["countryName"]}</td>
                                <td>{pais["capital"]}</td>
                                <td>{pais["population"]}</td>
                                <td>{pais["areaInSqKm"]}</td>
                            </tr>\n''')

        htmlfile.write('''</table>
                       </body>
                       </html>''')

    print(f'Archivo HTML "paises.html" creado con {len(ordenarPais)} registros.')

# Llama a la función para generar los archivos HTML
generarHTML(paises)
