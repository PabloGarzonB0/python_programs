
''' Clean and separete function'''

def cleanFiles(currentMen, exMen):
    with open(currentMen, 'r+') as writeFile:
        with open(exMen, 'a+') as appendFile:
            # get data
            writeFile.seek(0)
            members = writeFile.readlines()
            headers = members[0]
            members.pop(0)
            
            # Extract inactive members
            inactive = []
            for member in members:
                if 'no' in member:
                    inactive.append(member)
                
            # Retorna nuevamente al inicion el .txt
            writeFile.seek(0)
            writeFile.write(headers)
            for member in members:
                if member in inactive:
                    appendFile.write(member)
                else:
                    writeFile.write(member)
            writeFile.truncate()
                    


memReg = 'AllMem.txt'
exReg = 'inactiveMem.txt'
cleanFiles(memReg, exReg)

headers = "Membership_No Date Joined Actibe \n"

with open(memReg, 'r') as readFile, open(exReg, 'r') as readFile2:
    print("Active Members: \n")
    print(readFile.read())
    print("Inactive Members: \n")
    print(readFile2.read())
    
