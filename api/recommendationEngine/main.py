from time import gmtime, strftime
from .songSimilarity import TitleSimilarity
from .recommenders import UserAverage
from .evaluation import calcUsersMAP, calcUsersMRR, calcUsersNDCG
import logging
logger = logging.getLogger(__name__)
def bigBang(DEBUG=1):
    execTime = { }
    logger.info("[Start Big Bang]")
    # Calc Similarity
    execTime.setdefault('Similarity-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    TitleSimilarity()
    execTime.setdefault('Similarity-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
    # Calc Recommendations
    execTime.setdefault('UserRecommendation-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    UserAverage()
    execTime.setdefault('UserRecommendation-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
    # Evaluating Rank
    execTime.setdefault('Evaluating-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    evaluateUsersRank()
    execTime.setdefault('Evaluating-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
    for item in execTime.items():
        logger.debug(item)
    logger.info("[Finish Big Bang]")

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
