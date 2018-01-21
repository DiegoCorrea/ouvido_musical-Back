import os
from .data.userSongRecommendation.models import UserSongRecommendations
from .similarities.views import runSimilarities
from .recommenders.views import runRecommenders
from .recommenders.UserAverage.algorithm.models import (
    UserAverage_Recommendations
)
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


def cleanRecTables(userRec=True, userAveRec=True):
    logger.info("-"*30)
    logger.info('Limpando as tabelas de recomendações')
    if userRec:
        logger.info(
            "Deletando UserSongRecommendations -----> "
            + str(UserSongRecommendations.objects.all().delete())
        )
    if userAveRec:
        logger.info(
            "Deletando UserAverage_Recommendations -----> "
            + str(UserAverage_Recommendations.objects.all().delete())
        )
    logger.info("-"*30)


def recommendation_evaluate_analise(songSetLimit):
    runRecommenders(songSetLimit=songSetLimit)
    runEvaluations(at=5, songSetLimit=songSetLimit)
    runEvaluations(at=10, songSetLimit=songSetLimit)


def run_score_evaluate_analise():
    logger.info("*"*30)
    logger.info("* Recomendar, Avaliar e Analizar as recomendações")
    logger.info("*"*30)
    for songSetLimit in [1000, 2000, 3000]:
        for i in range(10):
            logger.info("*"*30)
            logger.info(
                "\tTamanho do banco ("
                + str(songSetLimit)
                + ") Ciclo: "
                + str(i)
            )
            logger.info("*"*30)
            cleanRecTables()
            recommendation_evaluate_analise(songSetLimit)
            os.system('cls||clear')
    logger.info('Finalizando Script')
