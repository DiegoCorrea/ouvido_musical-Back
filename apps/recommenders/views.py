from .UserAverage.algorithm.views import runUserAverage
import logging
logger = logging.getLogger(__name__)


def runRecommenders(songSetLimit):
    logger.info("[Start Recommenders]")
    runUserAverage(songSetLimit=songSetLimit)
    logger.info("[Finish Recommenders]")
