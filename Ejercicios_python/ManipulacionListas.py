'''Ejercicios basados en la utilizacion de listas '''
# Q1. implemente una lista personalizada, que agrupe los elementos mas pequeños 
def hallar_cadenas_cortas(*args):
    cadenas_cortas = []
    cadena_minima = s_lista[0]
    for elemento in s_lista:
        if len(elemento) < len(cadena_minima):
            cadena_minima = elemento
    print("La cadena mas corta es: ", cadena_minima)

    for elemento in s_lista:
        if len(elemento) == len(cadena_minima):
            cadenas_cortas.append(elemento)
    print("Los elementos similares son {} ".format(cadenas_cortas))
    
# Q2. Calcular los n numeros primos de una secuencia
def numerosPrimos(*kargs):

    for x in range(3,50):
        a = 0
        for y in range(x, 0, -1):
            #print(x)
            if (x % y == 0):
                a += 1
        if a == 2:
            lista_pri.append(x)
    print("Lista de numeros primos agrupados: ",lista_pri)

def grafica_z():
    ''' Funcion para graficar la letra z en consola'''
    for fil in range(FILAS):
        for col in range(COLUMNAS):
            if(fil == 0 or fil == 6):
                print("x\t", end="")
            elif fil + col == 6:
                print("x\t", end="")
            else:
                print("\t", end="")
        print()
def grafica_n():
    ''' Funcion para graficar la letra n en consola'''
    for fil in range(FILAS):
        for col in range(COLUMNAS):
            if(col == 0 or col == 6):
                print("x\t", end="")
            elif col == fil:
                print("x\t", end="")
            else:
                print("\t", end ="")
        print()

if __name__ ==  "__main__" : 
    # Inicializacion de la lista a analizar
    
    s_lista = ['bc', 'dcd', 'bcdefg', 'aa', 'cdc', 'pq']
    hallar_cadenas_cortas(s_list)
    
    # Calcular los N numeros primos del valor n
    lista_pri = [2]
    numerosPrimos(lista_pri)
