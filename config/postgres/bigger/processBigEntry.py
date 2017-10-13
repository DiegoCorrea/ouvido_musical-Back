def getDistinctUsers():
    print ('*'*30)
    print ('Processando a entrada do Play Entry para Distinct User Entry')
    print ('*'*30)

    distinctList = []
    for line in open('config/postgres/bigger/bigPlayEntry.csv', 'r'):
        line = line.split('\t')
        distinctList.append(line[0])
    distinctList = set(distinctList)
    print ('Total de Usuarios Distintos: ', len(distinctList))
    print ('Salvando no Arquivo. Aguarde alguns minutos!')
    userFile = open('config/seed/postgres/bigger/bigUserEntry.csv', 'w')
    userFile.write('id\n')
    for user in distinctList:
        userFile.write(user + '\n')
    userFile.close()
    print ('Usuarios distintos gerado e salvo. Finalizando o script!')
