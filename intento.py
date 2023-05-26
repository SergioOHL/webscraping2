import requests
import csv
from bs4 import BeautifulSoup

page = requests.get('https://www2.aefcm.gob.mx/directorio_escuelas/cct_lista.jsp?nivel_cct=null&delegacion=null&turno_cct=null&TipoConsulta=0&submit=Buscar')
soup = BeautifulSoup(page.text, 'html.parser')

blockquote_items = soup.find_all('table')

