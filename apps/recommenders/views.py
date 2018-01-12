from .UserAverage.algorithm.views import runUserAverage
from .UserAverage.analyzer.views import runAllUserAverageAnalizers
import logging
logger = logging.getLogger(__name__)
def runRecommenders(songSetLimit):
    logger.info("[Start Recommenders]")
    runUserAverage(songSetLimit=songSetLimit)
    runAllUserAverageAnalizers()
    logger.info("[Finish Recommenders]")
