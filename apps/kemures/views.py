import os
import logging
from apps.tecnics.content_based_metadata import UserSongRecommendations
from apps.kemures.recommenders.views import runRecommenders
from apps.kemures.recommenders.UserAverage import (
    UserAverage_Recommendations
)
from apps.kemures.metrics import runEvaluations, runAnalizerEvaluations
from apps.kemures.recommenders.UserAverage import userAverageGraphics
from apps.kemures.similarities.Cosine.analyzer.views import cosineGraphics
from apps.metadata.CONSTANTS import SET_SIZE_LIST, AT_LIST, TOTAL_RUN

logger = logging.getLogger(__name__)


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


def recommendation_evaluate(songSetLimit):
    runRecommenders(songSetLimit=songSetLimit)
    for at in AT_LIST:
        runEvaluations(at=at, songSetLimit=songSetLimit)


def runTheSystem():
    for songSetLimit in SET_SIZE_LIST:
        for i in range(TOTAL_RUN):
            logger.info("*"*30)
            logger.info(
                "\tTamanho do banco ("
                + str(songSetLimit)
                + ") Ciclo: "
                + str(i)
            )
            logger.info("*"*30)
            cleanRecTables()
            recommendation_evaluate(songSetLimit)
            os.system('cls||clear')
    logger.info('Finalizando Script')


def runGraphicsGenerator():
    cosineGraphics()
    userAverageGraphics()
    for songSetLimit in SET_SIZE_LIST:
        for at in AT_LIST:
            runAnalizerEvaluations(songSetLimit=songSetLimit, at=at)
