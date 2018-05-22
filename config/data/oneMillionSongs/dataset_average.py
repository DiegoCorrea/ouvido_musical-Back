import os


def songs_statistical():
    set_to_analyse = open(
        'config/data/oneMillionSongs/originalEntry/songs.csv',
        'r+'
        )
    songs = []
    albuns = []
    artists = []
    years = []
    for line in set_to_analyse:
        lineSplit = line.split(',')
        songs.append(lineSplit[1])
        albuns.append(lineSplit[2])
        artists.append(lineSplit[3])
        years.append(lineSplit[4])
    songs_len = len(songs)
    albuns_len = len(set(albuns))
    artists_len = len(set(artists))
    years_len = len(set(years))
    sorted_years = sorted(set(years))
    print('Songs: ' + str(songs_len))
    print('')
    print('Albuns: ' + str(albuns_len))
    print('+ Songs/Albuns ' + str(songs_len/albuns_len))
    print('')
    print('Artists: ' + str(artists_len))
    print('+ Songs/Artists: ' + str(songs_len/artists_len))
    print('+ Album/Artists: ' + str(albuns_len/artists_len))
    print('')
    print('years: ' + str(years_len))
    print('+ year min: ' + str(sorted_years[1]))
    print('+ year max: ' + str(sorted_years[-1]))
    print('+ years of songs: ' + str(int(sorted_years[-1]) - int(sorted_years[1])))


def user_statistical():
    set_to_analyse = open(
        'config/data/oneMillionSongs/originalEntry/playCount.csv',
        'r+'
        )
    songs = []
    users = []
    heard = []
    for line in set_to_analyse:
        lineSplit = line.split('\t')
        users.append(lineSplit[0])
        songs.append(lineSplit[1])
        heard.append(int(lineSplit[2]))
    songs_len = len(set(songs))
    users_len = len(set(users))
    heard_total = sum(heard)
    print('Songs: ' + str(songs_len))
    print('')
    print('Users: ' + str(users_len))
    print('+ Songs/Users ' + str(songs_len/users_len))
    print('')
    print('Heard: ' + str(heard_total))
    print('+ Heard/Users: ' + str(heard_total/users_len))
    print('+ Heard/Songs: ' + str(heard_total/songs_len))
