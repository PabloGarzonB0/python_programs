# PROGRAMA DE OPERACIONES ETL PARA EXTRACCION DE INFORMACION PIB DE PAISES

# importacion de librerias
import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3

def extract(url, table_attribs):
    ''' Esta funcion extrae la infromacion requerida de la pagina web y la guarda en un
    dataframe de pandas'''
    pass

def transform(df):
    ''' Esta funcion convierte la funcion del dataframe en formato floar pasando de millones a 
    billones, redondeando a 2 decimales y retornando el dataframe transformado'''
    pass

def load_to_csv(df, csv_path):
    ''' Esta funcion guarda el dataframe final en un archivo .csv considerando la ruta de 
    almacenamiento'''
    pass


def load_to_db(df, sql_connection, table_name):
    '''Esta funcion guarga el dataframe final en una tabla dentro de la base de datos'''
    pass

def run_query(query_statment, sql_connection):
    '''Esta funcion ejecuta una consulta dentro de la base de datos'''
    pass

def log_progress(message):
    '''Esta funcion genera un archivo log donde se guarda los registro de operaciones 
    de ejecucion realizados'''
    pass
    

URL = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
html_page = requests.get(URL).text


# Creacion de objeto de busqueda
soup_object = BeautifulSoup(html_page, 'html.parser')
print(soup_object.prettify())
