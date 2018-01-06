from apps.similarities.Cosine.algorithm.views import runTitleSimilarity
from apps.recommenders.UserAverage.algorithm.views import runUserAverage
from apps.evaluators.views import runEvaluation
import logging
logger = logging.getLogger(__name__)

def bigBang():
    logger.info("[Start Big Bang]")
    # Calc Similarity
    runTitleSimilarity()
    # Calc Recommendations
    runUserAverage()
    # Calc Evaluations
    runEvaluation()
    logger.info("[Finish Big Bang]")
