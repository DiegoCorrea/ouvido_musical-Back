from api.songs.models import Song, SongSimilarity
from .cosineSimilarity import cosineSimilarity

def titleSimilarityAllDB(DEBUG=1):
    allSongs = Song.objects.all()
    status = 0
    lenSongs = len(allSongs)
    songsSimilaries = { }
    for songBase in allSongs:
        # <DEBUG>
        if (DEBUG <= 2):
            status += 1
            print("\n\n+ Músicas processadas: " + str(status) + " de um total ", str(lenSongs))
            print("\n[Cosine similarity] \"" + songBase.title + "\"") # </DEBUG>
        songsSimilaries.setdefault(songBase.id, { })
        for songCompare in allSongs:
            if songBase == songCompare: continue
            sim = cosineSimilarity([songBase.title,songCompare.title])
            # <DEBUG>
            if (DEBUG <= 1):
                print("\t\"" + songCompare.title + "\" é: ", str(sim[0][1])) # </DEBUG>
            songsSimilaries[songBase.id].setdefault(songCompare.id, sim)
            similar = SongSimilarity(songBase=songBase, songCompare=songCompare, similarity=sim[0][1])
            similar.save()
        allSongs = allSongs.exclude(id=songBase.id)

def titleSimilarityNewSongs(DEBUG=1):
    allSongs = Song.objects.all()
    songsSimilaries = { }
    lenSongs = len(allSongs)
    status = 0
    newSong = 0
    for similar in SongSimilarity.objects.all():
        songsSimilaries.setdefault(similar.songBase_id, { })
        songsSimilaries[similar.songBase_id].setdefault(similar.songCompare_id, similar.similarity)
    for songBase in allSongs:
        if (songBase.id not in songsSimilaries):
            songsSimilaries.setdefault(songBase.id, { })
            newSong += 1
        # <DEBUG>
        if (DEBUG <= 2):
            status += 1
            print("\n\n+ Músicas processadas: " + str(status) + " de um total ", str(lenSongs))
            print("\n\n+ Novas músicas: " + str(newSong))
            print("\n[Cosine similarity]  \"" + songBase.title + "\"") # </DEBUG>
        for songCompare in allSongs:
            if songBase == songCompare: continue
            if (((songBase.id in songsSimilaries) and (songCompare.id in songsSimilaries[songBase.id])) or ((songCompare.id in songsSimilaries) and (songBase.id in songsSimilaries[songCompare.id]))):
                # <DEBUG>
                if (DEBUG <= 1):
                    print("\t-> \""+ songCompare.title + "\" já calculado!") # </DEBUG>
                continue
            sim = cosineSimilarity([songBase.title,songCompare.title])
            # <DEBUG>
            if (DEBUG <= 1):
                print("\t\"" + songCompare.title + "\" é: ", str(sim[0][1])) # </DEBUG>
            songsSimilaries[songBase.id].setdefault(songCompare.id, sim)
            similar = SongSimilarity(songBase=songBase, songCompare=songCompare, similarity=sim[0][1])
            similar.save()
        allSongs = allSongs.exclude(id=songBase.id)

def titleSimilarity():
    allSongs = Song.objects.all()[:20]
    matrixSimilarity = cosineSimilarity([ song.title for song in allSongs ])
    i = 0
    totalSong = len(allSongs)
    for songBase in allSongs:
        print('++Musica: ' + songBase.title)
        j = 0
        for songCompare in allSongs:
            print('\t' + songCompare.title + '\t --> \t' + str(matrixSimilarity[i][j]))
            #similar = SongSimilarity(songBase=songBase, songCompare=songCompare, similarity=matrixSimilarity[i][j])
            #similar.save()
            j += 1
        i += 1
        allSongs = allSongs.exclude(id=songBase.id)
