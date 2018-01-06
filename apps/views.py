from apps.similarities.views import runSimilarities
from apps.recommenders.UserAverage.algorithm.views import runUserAverage
from apps.evaluators.views import runEvaluation

import logging
logger = logging.getLogger(__name__)
def bigBang():
    logger.info("[Start Big Bang]")
    # Calc Similarity
    runSimilarities()
    # Calc Recommendations
    runUserAverage()
    # Calc Evaluations
    runEvaluation()
    logger.info("[Finish Big Bang]")
