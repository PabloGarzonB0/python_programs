import sqlite3
import pandas as pd


# Conexion a la base de datos
conn = sqlite3.connect('STAFF.db')  # Crea un base de datos llamada STAFF

# Mapear datos de la base de datos
table_name = 'INSTRUCTOR'
attribute_list = ["ID", 'FNAME','LNAME', 'CITY','CCODE']

file_path = r'D:\DesarrolloWeb_projects\EjercicioPython\ConsultaDB\INSTRUCTOR.csv'

# Leer datos del archivo csv
df = pd.read_csv(file_path, names = attribute_list)

# Cargar csv a base de datos
df.to_sql(table_name, conn, if_exists='replace', index=False)
print("Table is ready")

# Consulta 1. ver todos los registros
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_output)


# Insercion de nuevos datos a la base de datos
data_dict = {
    "ID": [100],
    "FNAME":['John'],
    "LNAME":["Doe"],
    "CITY" :["Paris"],
    "CCODE":["FR"]
}

data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists='append', index=False)
print("Data appended successfully")


# Consulta 2. ver los campos de nombre y apellido
query_statement = f"SELECT FNAME, LNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_output)

# Consulta 3. Conteo del numero total de registros
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_output)



conn.close()