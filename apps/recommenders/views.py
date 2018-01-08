from .UserAverage.algorithm.views import runUserAverage
from .UserAverage.analyzer.views import runAllUserAverageAnalizers
import logging
logger = logging.getLogger(__name__)
def runRecommenders():
    logger.info("[Start Recommenders]")
    runUserAverage()
    runAllUserAverageAnalizers()
    logger.info("[Finish Recommenders]")
