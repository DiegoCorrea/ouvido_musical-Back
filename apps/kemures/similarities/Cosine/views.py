from .algorithm.views import TitleSimilarity, TitleSimilarityWithObserver
from .analyzer.views import runCosineAnalizers
from apps.metadata.CONSTANTS import SET_SIZE_LIST, TOTAL_RUN
import logging
logger = logging.getLogger(__name__)


def runCosine():
    logger.info("[Start Title Similarity with Cosine]")
    TitleSimilarity()
    logger.info("[Finish Title Similarity with Cosine]")


def runSimilaritiesWithConfig():
    logger.info("[Start Similarities]")
    for setSize in SET_SIZE_LIST:
        for run in range(TOTAL_RUN):
            TitleSimilarityWithObserver(setSize=setSize)
    logger.info("[Finish Similarities]")
    runCosineAnalizers()
