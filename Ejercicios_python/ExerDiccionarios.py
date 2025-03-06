def guardar_datosDic(lista_elementos):
    '''Funcion para almacenar datos personales en un diccionario '''
    diccionario = {}
    for elemento in lista_elementos:
        item = input(f"Ingrese por favor {elemento}")
        diccionario[elemento] = item
        
    mensaje = (
        f"Su nombre es {diccionario['nombre']}, "
        f"tiene {diccionario['edad']} años, "
        f"vive en {diccionario['direccion']} "
        f"y su número de teléfono es {diccionario['telefono']}."
    )
    print(mensaje)

def cotizacion_fruta(frutas_dict):
    ''' Funcion para cotizar n kg de fruta '''
    fruta = input("Cual es la fruta que desea comprar: ")
    if fruta in frutas_dict:
        kg = float(input("Ingrese la cantidad de fruta (kg) a comprar"))
        print("Comprar {} kg de {} cuestan: {} €".format(kg, fruta, (kg*frutas_dict[fruta])))
    else: print("Lamentablemente no se tiene la fruta que desea")
    

def conversion_fecha():
    ''' Funcion para convertir una determinada fecha a otro formato'''
    list_fecha = []
    diccinario_meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    fecha = input("Ingrese la fecha a convertir en el siguiente formato dd/mm/aaaa")
    if len(fecha) != 0:
        list_fecha = fecha.split("/")
        print(f"La fecha es {list_fecha[0]} del {diccinario_meses[int(list_fecha[1])]} de {list_fecha[2]}")
        
    else:  
        print("No se ingreso ningun formato valido, vuelvalo a intentar")

def creditos_asignatura(creditos_dict):
    '''Funcion que imprime en pantalla el numero de creditos acumulados de un estudiante'''
    total_creditos = 0
    for key, values in creditos_dict.items():
        #total_creditos += values
        print("{} tiene {} creditos".format(key, creditos_dict[key]))
         
    #print("Total de creditos acumulados es:", total_creditos)
    
def ingreso_datos_dic():
    datos_dict = {}
    lista_datos = ["nombre", "edad", "sexo", "Telefono", "Email"]
    for  elemento in lista_datos:
        dato = input(f"Favor ingrese su {elemento} y presione Enter: ")
        datos_dict[elemento] = dato
    print(f"Detalles personales son: \n{datos_dict}")
    
if __name__ == "__main__":
    lista_elementos = ["nombre", "edad", "direccion", "telefono"]
    frutas_dict = {'Platano':1.35, 'Manzana': 0.80, 'Pera':0.85, 'Naranja': 0.70}
    Menu = '''Menu de frutas disponibles:
    1. Platano
    2. Manzana
    3. Pera
    4. Naranja'''
    # Ejercicio 1.
    # Funcion para guardar datos en Dict
    #guardar_datosDic(lista_elementos)
    # Funcion para hacer operaciones en fruteria
    #print(Menu)
    # Ejercicio 2.
    #cotizacion_fruta(frutas_dict)
    # Ejercicio 3.
    conversion_fecha()
