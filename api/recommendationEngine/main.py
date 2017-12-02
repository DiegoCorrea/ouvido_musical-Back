from time import gmtime, strftime
from .songSimilarity import TitleSimilarity
from .recommenders import UserAverage
from .evaluation import calcUsersMAP, calcUsersMRR, calcUsersNDCG
import logging
logger = logging.getLogger(__name__)

def bigBang():
    execTime = { }
    logger.info("[Start Big Bang]")
    # Calc Similarity
    execTime.setdefault('Similarity-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    logger.info("")
    TitleSimilarity()
    execTime.setdefault('Similarity-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
    # Calc Recommendations
    logger.info("")
    execTime.setdefault('UserRecommendation-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    UserAverage()
    execTime.setdefault('UserRecommendation-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
    # Evaluating Rank
    logger.info("")
    execTime.setdefault('Evaluating-StartedAt', strftime("%a, %d %b %Y %X", gmtime()))
    evaluateUsersRank()
    execTime.setdefault('Evaluating-FinishedAt', strftime("%a, %d %b %Y %X", gmtime()))
    logger.info("")
    for item in execTime.items():
        logger.debug(item)
    logger.info("[Finish Big Bang]")

def evaluateUsersRank(range=5):
    mrrResult = calcUsersMRR(limit=range)
    mapResult = calcUsersMAP(limit=range)
    ndcgResult = calcUsersNDCG(limit=range)
