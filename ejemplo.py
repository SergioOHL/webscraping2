import requests
from bs4 import BeautifulSoup

acum = 0

for i in range(1, 95):
    if acum == 94:
        break

    url = "https://www2.aefcm.gob.mx/directorio_escuelas/cct_lista.jsp?numero_pagina=" + str(acum) + "&busqueda=null&nivel_cct=null&delegacion=null&turno_cct=null&TipoConsulta=0&numeroderegistros_string=100"
    acum += i

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tabla = soup.find('table')

    filas = tabla.find_all('tr')

    for fila in filas:
        celdas = fila.find_all('td')
        for celda in celdas:
            print(celda.text.strip())

    print()
