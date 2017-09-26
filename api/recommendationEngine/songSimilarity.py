from random import choice
from api.songs.models import Song
from .cosineSimilarity import text_cos_similarity
from .cosineT2 import text_cos_similarity2

def titleSimilarity():
    songBase = Song.objects.get(id="SOVEUVC12A6310EAF1")
    songsCompare = choice(Song.objects.all())
    print("Cosine similarity entre " + songBase.title + ":")
    print("\t" + songsCompare.title + " é: ", str(text_cos_similarity([songBase.title,songsCompare.title])))

def titleSimilarityAllDB():
    for songBase in Song.objects.all():
        print("\n[Cosine similarity] entre \"" + songBase.title + "\":")
        for songsCompare in Song.objects.all():
            sim = text_cos_similarity2([songBase.title,songsCompare.title])
            print("\t\"" + songsCompare.title + "\" é: ", str(sim))
