import os
from .cleanDB import cleanRecTables
from apps.evaluators.views import runEvaluations, runAnalizers
from apps.recommenders.views import runRecommenders
import logging
logger = logging.getLogger(__name__)

def recommendation_evaluate_analise(songSetLimit):
    runRecommenders(songSetLimit=songSetLimit)
    #runEvaluations(at=5)
    #runAnalizers(at=5)
    #runEvaluations(at=10)
    #runAnalizers(at=10)

def run_score_evaluate_analise():
    logger.info("*"*30)
    logger.info("* Iniciando script Recomendar, Avaliar e Analizar as recomendações")
    logger.info("*"*30)
    for songSetLimit in [1000, 5000, 10000]:
        for i in range(30):
            logger.info("*"*30)
            logger.info("\tTamanho do banco (" + str(songSetLimit) + ") Ciclo: " + str(i))
            logger.info("*"*30)
            logger.info("Limpando Recommendação: " + str(cleanRecTables()))
            #recommendation_evaluate_analise(songSetLimit)
            os.system('cls||clear')
    logger.info('Finalizando Script')
