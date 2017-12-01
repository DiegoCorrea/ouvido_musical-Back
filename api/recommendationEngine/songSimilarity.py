from api.songs.models import Song, SongSimilarity
from .similarityAlgorithms import cosineSimilarity

def titleSimilaritynewSongss(DEBUG=1):
    allSongs = Song.objects.all()
    similarSongs = { }
    lenSongs = len(allSongs)
    status = 0
    newSongs = 0
    for similar in SongSimilarity.objects.all():
        similarSongs.setdefault(similar.songBase_id, { })
        similarSongs[similar.songBase_id].setdefault(similar.songCompare_id, similar.similarity)
    for songBase in allSongs:
        if (songBase.id not in similarSongs):
            similarSongs.setdefault(songBase.id, { })
            newSongs += 1
        # <DEBUG>
        if (DEBUG <= 2):
            status += 1
            print("\n\n+ Músicas processadas: " + str(status) + " de um total ", str(lenSongs))
            print("\n\n+ Novas músicas: " + str(newSongs))
            print("\n[Cosine similarity]  \"" + songBase.title + "\"") # </DEBUG>
        for songCompare in allSongs:
            if songBase == songCompare: continue
            if (((songBase.id in similarSongs) and (songCompare.id in similarSongs[songBase.id])) or ((songCompare.id in similarSongs) and (songBase.id in similarSongs[songCompare.id]))):
                # <DEBUG>
                if (DEBUG <= 1):
                    print("\t-> \""+ songCompare.title + "\" já calculado!") # </DEBUG>
                continue
            sim = cosineSimilarity([songBase.title,songCompare.title])
            # <DEBUG>
            if (DEBUG <= 1):
                print("\t\"" + songCompare.title + "\" é: ", str(sim[0][1])) # </DEBUG>
            similarSongs[songBase.id].setdefault(songCompare.id, sim)
            similar = SongSimilarity(songBase=songBase, songCompare=songCompare, similarity=sim[0][1])
            similar.save()
        allSongs = allSongs.exclude(id=songBase.id)

def titleSimilarity(DEBUG=1):
    allSongs = Song.objects.all()
    similarSongs = { }
    newSongs = 0
    # Calc Cosine from Songs and return a symmetric matrix len(Songs) x len(Songs)
    similarityMatrix = cosineSimilarity([ song.title for song in allSongs ])
    # Load previous Songs similarities
    for similar in SongSimilarity.objects.all():
        similarSongs.setdefault(similar.songBase_id, { })
        similarSongs[similar.songBase_id].setdefault(similar.songCompare_id, similar.similarity)
    # Persiste Title similarity
    i = 0
    for songBase in allSongs:
        allSongs = allSongs.exclude(id=songBase.id)
        if (songBase.id not in similarSongs):
            similarSongs.setdefault(songBase.id, { })
            newSongs += 1
        j = i + 1
        for songCompare in allSongs:
            if (((songBase.id in similarSongs) and (songCompare.id in similarSongs[songBase.id])) or ((songCompare.id in similarSongs) and (songBase.id in similarSongs[songCompare.id]))):
                # <DEBUG>
                if (DEBUG <= 1):
                    print("\t-> \""+ songCompare.title + "\" já calculado!") # </DEBUG>
                continue
            similar = SongSimilarity(songBase=songBase, songCompare=songCompare, similarity=similarityMatrix[i][j])
            similar.save()
            j += 1
        i += 1
    print("\n\n+ Novas músicas: " + str(newSongs))
