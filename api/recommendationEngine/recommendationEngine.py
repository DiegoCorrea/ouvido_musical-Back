from random import choice, randint

from api.songs.models import Song, SongSimilarity
from api.users.models import User
from api.userPlaySong.models import UserPlaySong
from api.userSongRecommendation.models import UserSongRecommendation
from api.CONSTANTS import MAX_SCORE, MIN_SCORE

from .songSimilarity import titleSimilarityAllDB
from .userRecommendation import getUserRecommendations
from .evaluation import calcUsersMAP, calcUsersMRR

def runSimilarity(DEBUG=1):
    # <DEBUG>
    if (DEBUG != 0):
        print("Iniciando o Calculo de Similaridade entre as Músicas")
        print("*** Etapa 1 - Titulos semelhantes ***") # </DEBUG>
    titleSimilarityAllDB()
    # <DEBUG>
    if (DEBUG != 0):
        print("*** Calculo finalizao! ***") # </DEBUG>


def runUserRecommendation(DEBUG=1):
    for user in User.objects.all():
        # <DEBUG>
        if (DEBUG != 0):
            print ('')
            print ("''"*30)
            print ('\nUser: ', user.id) # </DEBUG>
        recommendations = getUserRecommendations(user.id,DEBUG=DEBUG)
        for (song_id, similarity) in recommendations.items():
            userRec = UserSongRecommendation(
                        song_id=song_id,
                        user_id=user.id,
                        similarity=similarity,
                        iLike=bool(choice([True, False])),
                        score=randint(MIN_SCORE,MAX_SCORE))
            userRec.save()
            # <DEBUG>
            if (DEBUG != 0):
                song = Song.objects.get(id=song_id)
                print ('\n++ Musicas recomendadas')
                print ('\t-- Musica: ', song.title)
                print ('\t-- Similaridade', similarity)
                print ('\t-- Like: ', userRec.iLike)
                print ('\t-- Score: ', userRec.score) # </DEBUG>

def UsersEvaluating(DEBUG=1):
    mrrResult = calcUsersMRR(range=5,DEBUG=DEBUG)
    mapResult = calcUsersMAP(range=5,DEBUG=DEBUG)
