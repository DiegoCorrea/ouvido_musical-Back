from .Cosine.views import runCosine
import logging
logger = logging.getLogger(__name__)


def runSimilarities():
    logger.info("[Start Similarities]")
    runCosine()
    logger.info("[Finish Similarities]")
