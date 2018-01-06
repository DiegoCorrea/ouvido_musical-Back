from .Cosine.algorithm.views import runTitleSimilarity

import logging
logger = logging.getLogger(__name__)
def runSimilarities():
    logger.info("[Start Similarities]")
    runTitleSimilarity()
    logger.info("[Finish Similarities]")
