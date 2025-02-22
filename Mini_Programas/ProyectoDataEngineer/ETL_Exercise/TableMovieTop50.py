import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3


URL = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

# Inicializacion de varialbles
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = "/home/project/WScraping/Top_50_films.csv"
df = pd.DataFrame(columns=["Average Rank","Film","Year"]) # Crear dataset vacio
count = 0

html_page = requests.get(URL).text

# Creacion de objeto de busqueda
data = BeautifulSoup(html_page, 'html.parser')

# Busqueda de elementos
tables = data.find_all('tbody')
rows = tables[0].find_all('tr') # Extrae todos los elementos row

# Recorrer la lista de elementos 'tr'
for row in rows:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break

# Guardar archivos en base de datos y en archivo CSV
df.to_csv(csv_path) # Guarda el script en la ruta asignada
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
