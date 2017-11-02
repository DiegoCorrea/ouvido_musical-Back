from api.songs.models import Song, SongSimilarity
from .cosineSimilarity import text_cos_similarity

def titleSimilarityAllDB(DEBUG=1):
    allSongs = Song.objects.all()
    status = 0
    lenSongs = len(allSongs)
    songsSimilaries = { }
    for songBase in allSongs:
        # <DEBUG>
        if (DEBUG != 0):
            status += 1
            print("\n\n+ Músicas processadas: " + str(status) + " de um total ", str(lenSongs))
            print("\n[Cosine similarity] entre \"" + songBase.title + "\":") # </DEBUG>
        songsSimilaries.setdefault(songBase.id, { })
        for songCompare in allSongs:
            if songBase == songCompare: continue
            if ((songBase.id in songsSimilaries)
                and (songCompare.id in songsSimilaries[songBase.id])
                or (songCompare.id in songsSimilaries)
                and (songBase.id in songsSimilaries[songCompare.id])):
                # <DEBUG>
                if (DEBUG != 0):
                    print("\t-> \""+ songCompare.title + "\" já calculado!") # </DEBUG>
                continue
            sim = text_cos_similarity([songBase.title,songCompare.title])
            # if sim[0][1]== 0: continue
            # <DEBUG>
            if (DEBUG != 0):
                print("\t\"" + songCompare.title + "\" é: ", str(sim[0][1])) # </DEBUG>
            songsSimilaries[songBase.id].setdefault(songCompare.id, sim)
            similar = SongSimilarity(songBase=songBase, songCompare=songCompare.id, similarity=sim[0][1])
            similar.save()

def titleSimilarityNewSongs(DEBUG=1):
    allSongs = Song.objects.all()
    songsSimilaries = { }
    for similar in SongSimilarity.objects.all():
        if ((similar.songBase in songsSimilaries)
            and (similar.songCompare in songsSimilaries[similar.songBase])
            or (similar.songCompare in songsSimilaries)
            and (similar.songBase in songsSimilaries[similar.songCompare])): continue
        songsSimilaries.setdefault(similar.songBase, { })
        songsSimilaries[similar.songBase].setdefault(similar.songCompare, similar.similarity)
    status = 0
    for songBase in allSongs:
        if (songBase.id in songsSimilaries):
            continue
        else:
            songsSimilaries.setdefault(songBase.id, { })
        # <DEBUG>
        if (DEBUG != 0):
            status += 1
            print("\n+ Novas músicas processadas: ", status)
            print("\n[Cosine similarity] entre \"" + songBase.title + "\": ") # </DEBUG>
        for songCompare in allSongs:
            if songBase == songCompare: continue
            if ((songBase.id in songsSimilaries)
                and (songCompare.id in songsSimilaries[songBase.id])
                or (songCompare.id in songsSimilaries)
                and (songBase.id in songsSimilaries[songCompare.id])):
                # <DEBUG>
                if (DEBUG != 0):
                    print("\t-> \""+ songCompare.title + "\" já calculado!") # </DEBUG>
                continue
            sim = text_cos_similarity([songBase.title,songCompare.title])
            # if sim[0][1]== 0: continue
            # <DEBUG>
            if (DEBUG != 0):
                print("\t\"" + songCompare.title + "\" é: ", str(sim[0][1])) # </DEBUG>
            songsSimilaries[songBase.id].setdefault(songCompare.id, sim)
            similar = SongSimilarity(songBase=songBase, songCompare=songCompare.id, similarity=sim[0][1])
            similar.save()
