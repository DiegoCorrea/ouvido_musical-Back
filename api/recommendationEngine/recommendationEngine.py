from random import choice, randint
from time import gmtime, strftime

from api.users.models import User
from api.songs.models import Song
from api.userSongRecommendation.models import UserSongRecommendation
from api.CONSTANTS import MAX_SCORE, MIN_SCORE

from .songSimilarity import titleSimilarityAllDB
from .userRecommendation import getUserRecommendations
from .evaluation import calcUsersMAP, calcUsersMRR, calcUsersNDCG

def make(DEBUG=1):
    # <DEBUG>
    execTime = { }
    if (DEBUG != 0):
        execTime.setdefault('Similarity-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    # </DEBUG>
    runSimilarity(DEBUG=DEBUG)
    # <DEBUG>
    if (DEBUG != 0):
        execTime.setdefault('Similarity-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
        execTime.setdefault('UserRecommendation-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    # </DEBUG>
    makeUserRecommendation(DEBUG=DEBUG)
    # <DEBUG>
    if (DEBUG != 0):
        execTime.setdefault('UserRecommendation-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
        execTime.setdefault('Evaluating-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    # </DEBUG>
    UsersEvaluating(DEBUG=DEBUG)
    # <DEBUG>
    if (DEBUG != 0):
        execTime.setdefault('Evaluating-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
        for item in execTime.items():
            print(item)
    # </DEBUG>

def runSimilarity(DEBUG=1):
    # <DEBUG>
    if (DEBUG != 0):
        print("Iniciando o Calculo de Similaridade entre as Músicas")
        print("*** Etapa 1 - Titulos semelhantes ***") # </DEBUG>
    titleSimilarityAllDB()
    # <DEBUG>
    if (DEBUG != 0):
        print("*** Calculo finalizao! ***") # </DEBUG>


def makeUserRecommendation(DEBUG=1):
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

def UsersEvaluating(DEBUG=1, range=5):
    mrrResult = calcUsersMRR(range=range,DEBUG=DEBUG)
    mapResult = calcUsersMAP(range=range,DEBUG=DEBUG)
    ndcgResult = calcUsersNDCG(range=range,DEBUG=DEBUG)
    print ('')
    print ("''"*30)
    print ("''"*30)
    print ("''"*30)
    print ('Avaliações das Recomendações ao Usuarios')
    print ("''"*30)
    print ("''"*30)
    print ("''"*30)
    print ('NDCG: ', ndcgResult)
    print ('MRR: ', mrrResult)
    print ('MAP: ', mapResult)
