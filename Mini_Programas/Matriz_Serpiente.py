'''
Se quiere organizar una los asientos de un teatro de tamano n*n, los asientos se colocan en
disposicion de matriz de serpiente, escribir un programa que produzca este patron numerico
'''
# Metodo 1: mediante cadenas de texto
n = 5
seat = 1
for row in range(1,n + 1):
    rows_seat = ""
    for colum in range(1, n + 1):
            if row % 2 != 0:
                rows_seat = rows_seat + " "*(5 - len(str(seat))) + str(seat) #Conteo normal
                seat += 1
            else:
                rows_seat = " "*(5 - len(str(seat))) + str(seat) + rows_seat #Conteo inverso
                seat += 1
    print(rows_seat) # Se entregan las columnas como tipo string

# Metodo 2: mediante tratamiento de listas
n = 5
asientos = list(range(1,n * n + 1))
for i in range(n):
    fila = asientos[i * n  : (i+1) * n] # entrega la fila
    if i % 2 == 1: # El retorno es impar
        fila = fila[::-1] 
    print(''.join(f"{num:5d}" for num in fila))
