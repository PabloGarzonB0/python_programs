import random

def generar_asientos(filas=3, columnas=6):
    """Generar una matriz de asientos con valores aleatorios de 0 y 1."""
    return [[random.randrange(0,2) for _ in range(columnas)] for _ in range(filas)]

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

def main():
    """Funcion principal que ejectua el programa."""
    # Sistema de reserva de asientos
    asientos = generar_asientos()
    imprimir_asientos(asientos)


if __name__ == "__main__":
    main()