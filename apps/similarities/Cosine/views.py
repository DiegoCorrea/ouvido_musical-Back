from .algorithm.views import TitleSimilarity
from .analyzer.views import runAlgorithmAnalizers
import logging
logger = logging.getLogger(__name__)


def runCosine():
    logger.info("[Start Title Similarity with Cosine]")
    TitleSimilarity()
    runAlgorithmAnalizers()
    logger.info("[Finish Title Similarity with Cosine]")
