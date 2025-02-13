'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containig 'no'
    in the 'Active' Column and appends them to exMen
'''

def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as readFile, open(exMem, 'a+') as writeFile:
            header = readFile.readline()
             
            if writeFile.tell() == 0: 
                writeFile.write(header)
                
            members = readFile.readlines()
            inactive_members = [member for member in members if 'no' in member]

            # Volver al principio del archivo currentMem
            readFile.seek(0)
            readFile.truncate()
            
            readFile.write(header)
            # Iterar a traves de la lista de miembros

            for member in members :
                if 'no' in member:
                    writeFile.write(member)
                else:
                    readFile.write(member)

# Definir las rutas de los archivos
memReg =    './active_members.txt'
newMemReg = './inactive_members.txt'
cleanFiles(memReg,newMemReg)


headers = "Membership_No Date Joined Active \n"

with open(memReg, 'r') as readFile, open (newMemReg, 'r') as readFile2:
    print("Active members: \n\n")
    print(readFile.read())
    print("Inactive members: \n\n")
    print(readFile2.read())

