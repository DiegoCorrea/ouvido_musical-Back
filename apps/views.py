from .similarities.views import runSimilarities
from .recommenders.views import runRecommenders
from .evaluators.views import runEvaluations, runAnalizers

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
    runAnalizers()
    logger.info("[Finish Big Bang]")
