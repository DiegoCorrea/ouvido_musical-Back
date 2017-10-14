from api.users.models import User
from api.songs.models import Song
def getDistinctUsers(range=0):
    print ('*'*30)
    print ('Processando a entrada do Play Entry para Distinct User')
    print ('*'*30)
    status = 1
    distinctList = []
    for line in open('config/postgres/bigger/bigPlayEntry.csv', 'r'):
        line = line.split('\t')
        distinctList.append(line[0])
        if (status % 10000 == 0):
            print (" -> ",status)
        if (status == range):
            break
    distinctList = set(distinctList)
    print ('Total de Usuarios Distintos: ', len(distinctList))
    print ('Salvando no Arquivo. Aguarde alguns minutos!')
    toSaveFile = open('config/postgres/bigger/distinctUser'+ str(range) +'.seed', 'w+')
    toSaveFile.write('id\n')
    for user in distinctList:
        toSaveFile.write(user + '\n')
    toSaveFile.close()
    print ('Usuarios distintos gerado e salvo. Finalizando o script!')

def getDistinctSong(range=0):
    print ('*'*30)
    print ('Processando a entrada do Song Entry para Distinct Song')
    print ('*'*30)
    distinctList = []
    status = 1
    toSaveFile = open('config/postgres/bigger/distinctSong'+ str(range) +'.seed', 'w+')
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
        if (status == range):
            break
    print ('Total de Usuarios Distintos: ', len(distinctList))
    toSaveFile.close()
    print ('Usuarios distintos gerado e salvo. Finalizando o script!')

def getDistinctPlayCount():
    print ('*'*30)
    print ('Processando a entrada do Play Entry para Distinct Play')
    print ('*'*30)
    distinctList = {}
    status = 0
    for line in open('config/postgres/bigger/bigPlayEntry.csv', 'r'):
        status += 1
        if status == 1: continue
        if (status % 1000 == 0):
            print (" -> ",status)
        line = line.split('\t')
        if (line[0] in distinctList):
            if(line[1] in distinctList[line[0]]):
                distinctList[line[0]][line[1]] += line[1]
            else:
                distinctList[line[0]].setdefault(line[1], line[2])
        else:
            distinctList.setdefault(line[0], {})
            distinctList[line[0]].setdefault(line[1], line[2])
        if (status == 10000):
            break;
    print ('Total de Usuarios Distintos: ', len(distinctList))
    print ('Salvando no Arquivo. Aguarde alguns minutos!')
    toSaveFile = open('config/postgres/bigger/distinctPlay.seed', 'w+')
    toSaveFile.write('user_id,song_id,play_count\n')
    for user in distinctList:
        for (song, play) in distinctList[user].items():
            toSaveFile.write(user + ',' + song + ',' + play)
    toSaveFile.close()
    print ('Usuarios distintos gerado e salvo. Finalizando o script!')

def rangedDistinctPlayCount(range=0):
    print ('*'*30)
    print ('Processando a entrada do Play Entry para Distinct Play')
    print ('*'*30)
    distinctList = {}
    status = 1
    for line in open('config/postgres/bigger/bigPlayEntry.csv', 'r'):
        if status == 1: continue
        if (status % 1000 == 0):
            print (" -> ",status)
        line = line.split('\t')
        if (User.objects.get(id=line[0])):
            if (Song.objects.get(id=line[1])):
                status += 1
                if (line[0] in distinctList):
                    if(line[1] in distinctList[line[0]]):
                        distinctList[line[0]][line[1]] += line[1]
                    else:
                        distinctList[line[0]].setdefault(line[1], line[2])
                else:
                    distinctList.setdefault(line[0], {})
                    distinctList[line[0]].setdefault(line[1], line[2])
                if (status == range):
                    break
    print ('Total de Usuarios Distintos: ', len(distinctList))
    print ('Salvando no Arquivo. Aguarde alguns minutos!')
    toSaveFile = open('config/postgres/bigger/distinctPlay'+ str(range) +'.seed', 'w+')
    toSaveFile.write('user_id,song_id,play_count\n')
    for user in distinctList:
        for (song, play) in distinctList[user].items():
            toSaveFile.write(user + ',' + song + ',' + play)
    toSaveFile.close()
    print ('Usuarios distintos gerado e salvo. Finalizando o script!')
