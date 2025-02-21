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
if __name__ == "__main__":
    #df= extrac_from_csv('source1.csv') 
    print("gola")
