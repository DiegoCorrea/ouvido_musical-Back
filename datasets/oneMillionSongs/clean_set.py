import os


def clean_get_DistinctSongs():
    print ('*'*30)
    print ('* Limpando músicas duplicadas')
    print ('*'*30)
    distinctList = []
    status = 0
    toSaveFile = open(
        'datasets/oneMillionSongs/clean_set/songs.csv',
        'w+'
    )
    toSaveFile.write('id,title,album,artist,year\n')
    for line in open('datasets/oneMillionSongs/original_set/songs.csv', 'r+'):
        lineSplit = line.split(',')
        status += 1
        if (status % 10000 == 0):
            print ("-> [", status, "]")
        if lineSplit[0] not in distinctList:
            distinctList.append(lineSplit[0])
            toSaveFile.write(line)
        else:
            print ('[Alerta] Entrada Duplicada: ', line)
    print ('Total de Musicas Distintas: ', len(distinctList))
    toSaveFile.close()
    print ('- Distintos gerado e salvo. Finalizando o script! -')


def clean_get_DistinctPlayCount():
    print ('*'*30)
    print ('* Limpando músicas ouvidas duplicadas')
    print ('*'*30)
    distinctList = {}
    status = 0
    for line in open('datasets/oneMillionSongs/original_set/playCount.csv', 'r+'):
        status += 1
        if (status % 10000 == 0):
            print ("-> [", status, "]")
        line = line.split('\t')
        if (line[0] in distinctList):
            if(line[1] in distinctList[line[0]]):
                distinctList[line[0]][line[1]] += line[2]
            else:
                distinctList[line[0]].setdefault(line[1], line[2])
        else:
            distinctList.setdefault(line[0], {})
            distinctList[line[0]].setdefault(line[1], line[2])
    print ('- Total Distintos: ', len(distinctList), ' -')
    print ('- Salvando no Arquivo. Aguarde alguns minutos! -')
    toSaveFile = open(
        'datasets/oneMillionSongs/clean_set/playCount.csv',
        'w+'
    )
    toSaveFile.write('user_id,song_id,play_count\n')
    for user in distinctList:
        for (song, play) in distinctList[user].items():
            toSaveFile.write(user + ',' + song + ',' + play)
    toSaveFile.close()
    print ('- Distintos gerado e salvo. Finalizando o script! -')


def clean_all_files():
    directory = 'datasets/oneMillionSongs/clean_set/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    clean_get_DistinctSongs()
    clean_get_DistinctPlayCount()