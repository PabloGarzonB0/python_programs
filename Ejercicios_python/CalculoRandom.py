# Programa de simulacion de la loteria
import random as rdn
n1 = int(rdn.random()*10) + 1
n2 = int(rdn.random()*10) + 1
n3 = int(rdn.random()*10) + 1

print(f"numeros de juego  {n1}, {n2},  {n3}")
contador = 0
a, b, c = input("Ingresar 3 numeros de la loteria (digitos del 1 al 10)").split()
a = int(a); b = int(b); c = int(c)

# Comprobacion del acerito de los elementos de la loteria
def comprobacion(numeroElegido, contador):
    if numeroElegido == n1 or numeroElegido == n2 or numeroElegido == n3:
        contador += 1
    if contador == 3:
            print("Felicitaciones, ganaste la loteria")
    return contador

# LLamada a la funcion
contador = comprobacion(a,contador)
contador = comprobacion(b,contador)
contador = comprobacion(c,contador)
