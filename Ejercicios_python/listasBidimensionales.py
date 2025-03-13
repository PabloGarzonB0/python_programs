import random

def generar_asientos(filas=3, columnas=6):
    """Generar una matriz de asientos con valores aleatorios de 0 y 1."""
    return [[random.randrange(0,2) for _ in range(columnas)] for _ in range(filas)]

def contar_asientos_disponibles(asientos):
    """cuenta los asientos disponibles en la matriz (representados por 0). """
    return sum(fila.count(0) for fila in asientos)

def imprimir_asientos(asientos):
    """Imprime la matriz de asientos y cuenta los asientos disponibles"""
    disponibles = 0
    for fila in asientos:
        for asientos in fila:
            print(asientos, end=" ")
            if asientos == 0:
                disponibles += 1
        print()
    print(f"El numero de asietos dispoinbles en la sala es: {disponibles}")

def crear_matriz_numerica(filas=4, columnas=4):
    """Crear una matriz 4x4 con valores secuenciales del 1 al 16."""
    return [[columnas * i + j + 1 for j in range(columnas)] for i in range(filas)]

def imprimir_matriz(matriz):
    """Imprime una matriz de forma estructurada """
    for fila in matriz:
        print(fila)


def main():
    """Funcion principal que ejectua el programa."""
    # Sistema de reserva de asientos
    asientos = generar_asientos()
    imprimir_asientos(asientos)
    # opcion 2 para visualizar asientos
    contar_asientos_disponibles(asientos)
    # Creacion de matriz numerica
    matriz_numerica = crear_matriz_numerica()
    imprimir_matriz(matriz_numerica)


if __name__ == "__main__":
    # Seccion principal
    main()
