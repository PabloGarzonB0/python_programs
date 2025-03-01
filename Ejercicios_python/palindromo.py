''' Programa para calcular si un numero es palindromo'''
def metodo_1(Number):
    estado = True
    # Metodo 1.
    while estado:
        if Number == Number[::-1]:
            print("The Number is palindrom")
        else: 
            print("The number isn't palindrom")
        Respuesta = input("Desea continuar evaluado cualquier otro numero [y/n]")
        if Respuesta != "y": break
    print("**Programa finalizado**")


def metodo_2(Number):
    # Metodo 2.
    revesNumber = ""
    contador = len(Number)
    # Calcular numero invertido
    while contador > 0 :
        revesNumber = revesNumber + Number[contador-1]
        contador -= 1
    # Validacion
    if Number == revesNumber: print("The Number is palindrom")
    else:                     print("The number isn't palindrom")
    print("**Programa finalizado**")





if "__name__" == "__main__":
    Number = input("Ingrese el valor que desea evaluar")
    metodo_1(Number)
    metodo_2(Number)
    