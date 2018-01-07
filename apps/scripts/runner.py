import os
from .votate import votateUserAverage
from .cleanDB import cleanRecTables, cleanVotateTable
from apps.evaluators.views import runEvaluations, runAnalizers
import logging
logger = logging.getLogger(__name__)

def votate_evaluate_analise():
    votateUserAverage()
    runEvaluations()
    runAnalizers()

def clean_votate_evaluate_analise():
    cleanRecTables()
    cleanVotateTable()

def run_votate_evaluate_analise():
    logger.info("*"*30)
    logger.info("* Iniciando script Votar, Avaliar e Analizar as recomendações")
    logger.info("*"*30)
    for i in range(5):
        logger.info("*"*30)
        logger.info("\tCiclo: " + str(i))
        logger.info("*"*30)
        clean_votate_evaluate_analise()
        votate_evaluate_analise()
        os.system('cls||clear')
    logger.info('Finalizando Script')
