from .Cosine.handle import Cosine
import logging
logger = logging.getLogger(__name__)


def runSimilarities():
    logger.info("[Start Similarities]")
    cos = Cosine()
    logger.info("[Finish Similarities]")
