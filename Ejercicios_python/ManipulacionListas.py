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
            if x % y == 0:
                a += 1
        if a == 2:
            lista_pri.append(x)
    print("Lista de numeros primos agrupados: ",lista_pri)

if __name__ ==  "__main__" : 
    # Inicializacion de la lista a analizar
    
    s_lista = ['bc', 'dcd', 'bcdefg', 'aa', 'cdc', 'pq']
    hallar_cadenas_cortas(s_list)
    
    # Calcular los N numeros primos del valor n
    lista_pri = [2]
    numerosPrimos(lista_pri)
