# Ejercicios con diccionarios
def entrega_divisas(*kwargs):
    ''' Escribir un programa que guarde en una vairable el diccionario '''
    print("Defina la divisa que desea obtener")
    iter = 0 
    for div in divisas:
        iter += 1
        print(f"{iter}. {div}")
    respuesta = input("Ingrese alguno de los valores: \n")
    for div in divisas:
        iter -= 1
        if respuesta == div:
            print(f" Simbolo : {divisas[respuesta]}")
            break
        elif (iter == 0 ) : print("Divisa no encontrada")

def entrega_divisas2(*kwargs):
    respuesta = input("Ingrese alguno de los valores: \n")
    print("Simbolo : ",divisas.get(respuesta.title(), "La divisa no esta"))

if __name__ == "__main__":
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    # entrega_divisas(divisas)
    entrega_divisas2(divisas)
