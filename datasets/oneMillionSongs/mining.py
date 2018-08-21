import os
from random import sample

userPlayList = []
directory = ''


def getSongs(name, limit):
    global directory
    song_list = []
    print('*'*30)
    print('* Minerando ', str(limit), ' músicas *')
    print('*'*30)
    status = 0
    if not os.path.exists(directory):
        os.makedirs(directory)
    toSaveFile = open(
        'datasets/oneMillionSongs/sets/' + str(name) + '/songs.csv',
        'w+'
    )
    toSaveFile.write('id,title,album,artist\n')
    songSet = sample(
        set(
            open(
                'datasets/oneMillionSongs/clean_set/songs.csv',
                'r+'
                )
        ), limit
    )
    for line in songSet:
        if (status % 1000 == 0):
            print ("-> [", status, "]")
        lineSplit = line.split(',')
        song_list.append(lineSplit[0])
        toSaveFile.write(lineSplit[0] + ',' + lineSplit[1] + ',' + lineSplit[2] + ',' + lineSplit[3] + '\n')
        if (status > limit):
            break
        status += 1
    print ('- Total de Musicas: ', len(song_list))
    toSaveFile.close()
    print ('- Finalizando o script!')
    return song_list


def getPlayCount(song_list, name, limit, userLimit):
    global userPlayList
    global directory
    print ('*'*30)
    print ('* Pegando Lista de pessoas que ouviram as musicas *')
    print ('*'*30)
    status = 0
    if not os.path.exists(directory):
        os.makedirs(directory)
    toSaveFile = open(
        'datasets/oneMillionSongs/sets/' + str(name) + '/playCount.csv',
        'w+'
    )
    toSaveFile.write('user_id,song_id,play_count\n')
    for line in open(
        'datasets/oneMillionSongs/clean_set/playCount.csv',
        'r+'
    ):
        status += 1
        if status == 1:
            continue
        if (status % 1000 == 0):
            print ("-> [", status, "]")
        lineSplit = line.split(',')
        if (lineSplit[1] not in song_list):
            continue
        if lineSplit[0] not in userPlayList:
            userPlayList.append(lineSplit[0])
        toSaveFile.write(line)
    print ('- Total de usuarios: ', len(userPlayList))
    usersToSaveFile = open(
        'datasets/oneMillionSongs/sets/' + str(name) + '/users.csv',
        'w+'
    )
    usersToSaveFile.write('id\n')
    for user in userPlayList:
        usersToSaveFile.write(user + "\n")
    toSaveFile.close()
    usersToSaveFile.close()
    print ('- Finalizando o script!')


def start(name, limit, userLimit=None):
    global directory
    global songDict
    directory = 'datasets/oneMillionSongs/sets/' + str(name)
    song_list = getSongs(name, limit)
    getPlayCount(song_list, name, limit, userLimit)
    generate_load(name=name)


def generate_load(name):
    name = str(name)
    toSaveFile = open(
        'datasets/oneMillionSongs/sets/' + name + '/load.sql',
        'w+'
    )
    toSaveFile.write("\COPY songs_song FROM \'datasets/oneMillionSongs/sets/" + name + "/songs.csv\' DELIMITER \',\' CSV HEADER;\n"+"\COPY users_user FROM \'datasets/oneMillionSongs/sets/" + name + "/users.csv\' CSV HEADER;\n"+"\COPY \"user_preferences_userpreference\"(user_id,song_id,play_count) FROM 'datasets/oneMillionSongs/sets/" + name + "/playCount.csv' DELIMITER ',' CSV HEADER;\n")
    toSaveFile.close()

##########
def main():
    start(name="five_thousand", limit=5000)
    start(name="ten_thousand", limit=10000)
    start(name="25000", limit=25000)
