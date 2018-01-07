import os
from .score import scoreUserAverage
from .cleanDB import cleanRecTables, cleanScoreTable
from apps.evaluators.views import runEvaluations, runAnalizers
import logging
logger = logging.getLogger(__name__)

def score_evaluate_analise():
    scoreUserAverage()
    runEvaluations()
    runAnalizers()

def clean_score():
    cleanRecTables()
    #cleanScoreTable()

def run_score_evaluate_analise():
    logger.info("*"*30)
    logger.info("* Iniciando script Votar, Avaliar e Analizar as recomendações")
    logger.info("*"*30)
    for i in range(5):
        logger.info("*"*30)
        logger.info("\tCiclo: " + str(i))
        logger.info("*"*30)
        clean_score()
        score_evaluate_analise()
        os.system('cls||clear')
    logger.info('Finalizando Script')
