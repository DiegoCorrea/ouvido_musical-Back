from random import choice

from api.songs.models import Song, SongSimilarity
from api.users.models import User
from api.userPlaySong.models import UserPlaySong
from api.userSongRecommendation.models import UserSongRecommendation

from .songSimilarity import titleSimilarityAllDB
from .userRecommendation import getUserRecommendations

def runSimilarity():
    print("Iniciando o Calculo de Similaridade entre as Músicas")
    print("*** Etapa 1 - Titulos semelhantes ***")
    titleSimilarityAllDB()
    print("*** Calculo finalizao! ***")


def runUserRecommendation(DEBUG=0):
    for user in User.objects.all():
        if (DEBUG != 0):
            print ('')
            print ("''"*30)
            print ('\nUser: ', user.id)
        recommendations = getUserRecommendations(user.id)
        for (song_id, similarity) in recommendations.items():
            userRec = UserSongRecommendation(song_id=song_id,user_id=user.id,similarity=similarity,iLike=bool(choice([True, False])))
            userRec.save()
            if (DEBUG != 0):
                song = Song.objects.get(id=song_id)
                print ('\n++ Musicas recomendadas')
                print ('\t-- Musica: ', song.title)
                print ('\t-- Similaridade', similarity)
                print ('\t-- Like: ', userRec.iLike)
