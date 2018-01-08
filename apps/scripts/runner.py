import os
from .score import scoreUserAverage
from .cleanDB import cleanRecTables, cleanScoreTable
from apps.evaluators.views import runEvaluations, runAnalizers
from apps.recommenders.views import runUserAverage
import logging
logger = logging.getLogger(__name__)

def score_evaluate_analise():
    runUserAverage()
    runEvaluations(at=5)
    runEvaluations(at=10)
    runAnalizers(at=5)
    runAnalizers(at=10)

def clean_score():
    cleanRecTables()
    #cleanScoreTable()

def run_score_evaluate_analise():
    logger.info("*"*30)
    logger.info("* Iniciando script Votar, Avaliar e Analizar as recomendações")
    logger.info("*"*30)
    for i in range(2):
        logger.info("*"*30)
        logger.info("\tCiclo: " + str(i))
        logger.info("*"*30)
        clean_score()
        score_evaluate_analise()
        os.system('cls||clear')
    logger.info('Finalizando Script')
