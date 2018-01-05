from time import gmtime, strftime
from .songSimilarity import TitleSimilarity
from .recommenders import UserAverage

from .evaluation import runMAP, runMRR, runNDCG
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
    evaluateUsersRank()
    logger.info("[Finish Big Bang]")

def evaluateUsersRank(limit=5):
    runMAP(limit=limit)
    runMRR(limit=limit)
    runNDCG(limit=limit)
