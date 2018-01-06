import os
songList = [ ]
songDict = None
userPlayList = [ ]
directory = ''
def getSongs(name, limit):
    global songList
    global directory
    print ('*'*30)
    print ('* Minerando ', str(limit) ,' músicas *')
    print ('*'*30)
    status = 0
    if not os.path.exists(directory):
        os.makedirs(directory)
    toSaveFile = open('config/data/oneMillionSongs/' + str(name) + '/songs.csv', 'w+')
    for line in open('config/data/oneMillionSongs/originalCleanEntry/songs.csv', 'r+'):
        status += 1
        if (status % 1000 == 0):
            print ("-> [", status, "]")
        lineSplit = line.split(',')
        songList.append(lineSplit[0])
        toSaveFile.write(lineSplit[0] + ',' + lineSplit[1] + '\n')
        if (status == limit):
            break
    print ('- Total de Musicas: ', len(songList))
    toSaveFile.close()
    print ('- Finalizando o script!')

def getPlayCount(name, limit):
    global songDict
    global userPlayList
    global directory
    print ('*'*30)
    print ('* Pegando Lista de pessoas que ouviram as musicas *')
    print ('*'*30)
    status = 0
    if not os.path.exists(directory):
        os.makedirs(directory)
    toSaveFile = open('config/data/oneMillionSongs/' + str(name) + '/playCount.csv', 'w+')
    toSaveFile.write('user_id,song_id,play_count\n')
    for line in open('config/data/oneMillionSongs/originalCleanEntry/playCount.csv', 'r+'):
        status += 1
        if status == 1: continue
        if (status % 1000 == 0):
            print ("-> [", status, "]")
        lineSplit = line.split(',')
        if (lineSplit[1] not in songDict): continue
        userPlayList.append(lineSplit[0])
        toSaveFile.write(line)
    userDict = set(userPlayList)
    print ('- Total de usuarios: ', len(userDict))
    usersToSaveFile = open('config/data/oneMillionSongs/' + str(name) + '/users.csv', 'w+')
    usersToSaveFile.write('id\n')
    for user in userDict:
        usersToSaveFile.write(user + "\n")
    toSaveFile.close()
    usersToSaveFile.close()
    print ('- Finalizando o script!')

def start(name, limit):
    global directory
    global songDict
    directory = 'config/data/oneMillionSongs/' + str(name)
    getSongs(name, limit)
    songDict = set(songList)
    getPlayCount(name, limit)


##########
def main():
    start(name="fiveHhundred",limit=500)
    start(name="thousand",limit=1000)
    start(name="tenThousand",limit=10000)
    start(name="hundredThousand",limit=100000)
