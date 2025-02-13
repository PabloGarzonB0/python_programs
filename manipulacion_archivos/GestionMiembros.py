''' Script para generacion de registros de  miembros de un registro de miembros'''
from random import randint as rnd

memReg = './memberst.txt'
exReg = './inactive.txt'
fee = ('yes', 'no')

def genFiles(current, old):
    
    with open(current, 'w+') as writefile:
        writefile.write("Membership_No Date Joined Active \n")
        data = "{:^13} {:<11} {:<6} \n"
        
        for rowno in range(20): # numero de registros realizados
            date = str(rnd(2015,2020)) + '-' + str(rnd(1,12)) + '-' + str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999), date, fee[rnd(0,1)]))
            
    with open(current, 'r') as readfile, open(old, 'w+') as writefile:
            header = readfile.readline() # Leer la cabecera
            writefile.write(header)
            
            for line in readfile:
                if 'no' in line: #Verifica si el miembre se encuentra inactivo
                    writefile.write(line)
            
            
genFiles(memReg, exReg)