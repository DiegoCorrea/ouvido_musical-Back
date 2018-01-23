from .UserAverage.algorithm.views import runUserAverage
from .UserAverage.analyzer.views import runUserAverageAnalizers
import logging
logger = logging.getLogger(__name__)


def runRecommenders(songSetLimit):
    logger.info("[Start Recommenders]")
    runUserAverage(songSetLimit=songSetLimit)
    logger.info("[Finish Recommenders]")
