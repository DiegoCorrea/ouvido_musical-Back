from .UserAverage.algorithm.views import runUserAverage

import logging
logger = logging.getLogger(__name__)
def runRecommenders():
    logger.INFO("[Start Recommenders]")
    runUserAverage()
    logger.INFO("[Finish Recommenders]")
