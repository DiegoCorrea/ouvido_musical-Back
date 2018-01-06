from .similarities.views import runSimilarities
from .recommenders.views import runRecommenders
from .evaluators.views import runEvaluations

import logging
logger = logging.getLogger(__name__)
def bigBang():
    logger.info("[Start Big Bang]")
    # Calc Similarity
    runSimilarities()
    # Calc Recommendations
    runRecommenders()
    # Calc Evaluations
    runEvaluations()
    logger.info("[Finish Big Bang]")
