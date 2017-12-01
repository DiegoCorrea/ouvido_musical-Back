from time import gmtime, strftime

from .songSimilarity import titleSimilarity
from .recommenders import makeUserRecommendation
from .evaluation import calcUsersMAP, calcUsersMRR, calcUsersNDCG

def bigBang(DEBUG=1):
    # <DEBUG>
    execTime = { }
    if (DEBUG <= 5):
        execTime.setdefault('Similarity-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    # </DEBUG>
    titleSimilarity()
    # <DEBUG>
    if (DEBUG <= 5):
        execTime.setdefault('Similarity-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
        execTime.setdefault('UserRecommendation-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    # </DEBUG>
    makeUserRecommendation(DEBUG=DEBUG)
    # <DEBUG>
    if (DEBUG <= 5):
        execTime.setdefault('UserRecommendation-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
        execTime.setdefault('Evaluating-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    # </DEBUG>
    evaluateUsersRank(DEBUG=DEBUG)
    # <DEBUG>
    if (DEBUG <= 5):
        execTime.setdefault('Evaluating-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
        for item in execTime.items():
            print(item)
    # </DEBUG>

def evaluateUsersRank(DEBUG=1, range=5):
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
