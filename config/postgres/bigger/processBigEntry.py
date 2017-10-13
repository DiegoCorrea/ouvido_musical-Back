def getDistinctUsers():
    print ('*'*30)
    print ('Processando a entrada do Play Entry para Distinct User')
    print ('*'*30)

    distinctList = []
    for line in open('config/postgres/bigger/bigPlayEntry.csv', 'r'):
        line = line.split('\t')
        distinctList.append(line[0])
    distinctList = set(distinctList)
    print ('Total de Usuarios Distintos: ', len(distinctList))
    print ('Salvando no Arquivo. Aguarde alguns minutos!')
    toSaveFile = open('config/postgres/bigger/distinctUser.seed', 'w+')
    toSaveFile.write('id\n')
    for user in distinctList:
        toSaveFile.write(user + '\n')
    toSaveFile.close()
    print ('Usuarios distintos gerado e salvo. Finalizando o script!')

def getDistinctSong():
    print ('*'*30)
    print ('Processando a entrada do Song Entry para Distinct Song')
    print ('*'*30)
    distinctList = []
    status = 1
    toSaveFile = open('config/postgres/bigger/distinctSong.seed', 'w+')
    toSaveFile.write('id,title,album,artist,year\n')
    for line in open('config/postgres/bigger/bigSongEntry.csv', 'r'):
        lineSplit = line.split(',')
        if (status % 10000 == 0):
            print (" -> ",status)
        if lineSplit[0] not in distinctList:
            distinctList.append(lineSplit[0])
            toSaveFile.write(line)
        else:
            print ('[Alerta] Entrada Duplicada : ', line)
        status += 1
    print ('Total de Usuarios Distintos: ', len(distinctList))
    toSaveFile.close()
    print ('Usuarios distintos gerado e salvo. Finalizando o script!')
