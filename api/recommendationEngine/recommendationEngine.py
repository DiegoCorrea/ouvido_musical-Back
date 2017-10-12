from random import choice, randint
import numpy as np

from api.songs.models import Song, SongSimilarity
from api.users.models import User
from api.userPlaySong.models import UserPlaySong
from api.userSongRecommendation.models import UserSongRecommendation
from api.CONSTANTS import MAX_SCORE, MIN_SCORE

from .songSimilarity import titleSimilarityAllDB
from .userRecommendation import getUserRecommendations
from .userRecommendation import calcUserMAP, calcUserMRR

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

# <Params>
# range é o numero referente a quantas posições quer se calcular o MAP
# range padrão é 5
# </Params>
def usersMAP(range=5, DEBUG=1):
    # <DEBUG>
    if (DEBUG != 0):
        print ('\nMAP com range de ', range) # </DEBUG>
    ap = [calcUserMAP(user.usersongrecommendation_set.all()[:range], DEBUG=DEBUG) for user in User.objects.all()]
    # <DEBUG>
    if (DEBUG != 0):
        print ('\n\tMean Averange Precision: ', np.mean(ap))
        print ('\t++ Averange Precision dos usuarios: ', ap)
        print ('\t++ Total de usuarios: ', len(User.objects.all())) # </DEBUG>

# <Params>
# range é o numero referente a quantas posições quer se calcular o MRR
# range padrão é 5
# </Params>
def usersMRR(range=5, DEBUG=1):
    # <DEBUG>
    if (DEBUG != 0):
        print ('\nMRR com range de ', range) # </DEBUG>
    mrrList = [calcUserMRR(user.usersongrecommendation_set.all()[:range], DEBUG=DEBUG) for user in User.objects.all()]
    # <DEBUG>
    if (DEBUG != 0):
        print ('\n\tMean Reciprocal Rank: ', np.mean(mrrList))
        print ('\t++ Lista de MRR dos usuarios: ', mrrList)
        print ('\t++ Total de usuarios: ', len(User.objects.all())) # </DEBUG>
