from api.songs.models import Song, SongSimilarity
from .cosineSimilarity import text_cos_similarity

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
            sim = text_cos_similarity([songBase.title,songCompare.title])
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
            sim = text_cos_similarity([songBase.title,songCompare.title])
            # <DEBUG>
            if (DEBUG <= 1):
                print("\t\"" + songCompare.title + "\" é: ", str(sim[0][1])) # </DEBUG>
            songsSimilaries[songBase.id].setdefault(songCompare.id, sim)
            similar = SongSimilarity(songBase=songBase, songCompare=songCompare, similarity=sim[0][1])
            similar.save()
        allSongs = allSongs.exclude(id=songBase.id)
