from api.songs.models import Song, SongSimilarity
from .cosineSimilarity import text_cos_similarity

def titleSimilarityAllDB(DEBUG=1):
    for songBase in Song.objects.all():
        # <DEBUG>
        if (DEBUG != 0):
            print("\n[Cosine similarity] entre \"" + songBase.title + "\":") # </DEBUG>
        for songsCompare in Song.objects.all():
            if songBase == songsCompare: continue
            sim = text_cos_similarity([songBase.title,songsCompare.title])
            if sim[0][1]== 0: continue
            # <DEBUG>
            if (DEBUG != 0):
                print("\t\"" + songsCompare.title + "\" é: ", str(sim[0][1])) # </DEBUG>
            similar = SongSimilarity(songBase=songBase,songCompare=songsCompare.id,similarity=sim[0][1])
            similar.save()
