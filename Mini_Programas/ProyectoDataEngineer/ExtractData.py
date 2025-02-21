'''ETL para la extraccion de datos de archivos Json y CSV considerando unicamente datos uniformes'''

import glob
import pandas as pd
# Extraccion de los datos
list_csv = glob.glob('*.csv')
list_json = glob.glob('*.json')

def extrac_from_csv(file_to_process):       # Deben contenerse las mismas columnas que el DataFrame
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extrac_from_json(file_to_process):   # Deben contenerse las mismas columnas que el DataFrame
    dataframe = pd.read_csv(file_to_process)
    return dataframe


def extract():
    # Creacion de dataframe vacio para almacenar los datos
    extracted_data = pd.DataFrame(columns=['name','height','wieght'])
    
    # Procesar todos los archivos csv
    for csvfile in glob.glob(".csv"):
        extracted_data = extracted_data.append(extrac_from_csv(csvfile), ignore_index=True)
        
    # Procesar todos los archivos json
    for jsonfile in glob.glob(".json"):
        extracted_data = extracted_data.append(extrac_from_csv(jsonfile), ignore_index=True)
    return extracted_data
        
def transform(data):
    # Convertir datos que se encuentran en pulgadas a milimetros
    data['height'] = round(data.height * 0.0252,2)
    # Convertir las libras a kilogramos
    data['weight']= round(data.weight * 0.45359237,2)
    return data 

def load(target_file, data_to_load):
    data_to_load.to_csv(target_file)


    # Registro de datos
def log(message):
    timestamp_format = "%Y-%h-%d-%H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)  # Se formatea la fecha teniendo en cuenta este estilo
    with open("logfile.txt", "+a") as f:
        f.write(timestamp + ',' + message + '\n' )
    
if __name__ == "__main__":
    target_file = "tranformed_data.csv"
    
    # LLamada a funciones para Refinar los datos finales
    log("ETL Job Started")
    log("Extract phase Started")
    extracted_data = extract()
    log("Extract phase Ended")
    
    log("Transform Job Started")
    transformed_data = transform(extracted_data)
    log("Transrom Job Ended")
    
    log("Load Job Started")
    load(target_file, transformed_data)
    log("Load Job Ended")
    
    log("Finish ETL Process...")    
   

