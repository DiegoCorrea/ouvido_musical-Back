from .UserAverage.algorithm.views import runUserAverage

import logging
logger = logging.getLogger(__name__)
def runRecommenders():
    logger.info("[Start Recommenders]")
    runUserAverage()
    logger.info("[Finish Recommenders]")
