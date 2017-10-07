from random import choice
from api.songs.models import Song, SongSimilarity
from .cosineSimilarity import text_cos_similarity

def titleSimilarity(DEBUG=1):
    songBase = Song.objects.get(id="SOVEUVC12A6310EAF1")
    songsCompare = choice(Song.objects.all())
    # <DEBUG>
    if (DEBUG != 0):
        print("Cosine similarity entre " + songBase.title + ":")
        print("\t" + songsCompare.title + " é: ", str(text_cos_similarity([songBase.title,songsCompare.title]))) # </DEBUG>

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
