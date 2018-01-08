import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.evaluators.NDCG.algorithm.models import NDCG
from django.db import connection
import logging

logger = logging.getLogger(__name__)

def value_gLine(at=5):
    logger.info("[Start NDCG Value (Graph Line)]")
    allEvaluations = NDCG.objects.filter(limit=at)
    evaluationValues = [ ]
    evaluationMeanValues = [ ]
    evaluationMedianValues = [ ]
    for evaluation in allEvaluations:
        evaluationValues.append(evaluation.value)
        evaluationMeanValues.append(np.mean(evaluationValues))
        evaluationMedianValues.append(np.median(evaluationValues))
    logger.debug("NDCG Evaluation -> Mean: " + str(evaluationMeanValues[-1]))
    logger.debug("NDCG Evaluation -> Median: " + str(evaluationMedianValues[-1]))
    logger.debug("NDCG Evaluation -> Run Number: " + str(len(evaluationValues)))
    directory = str('./files/apps/evaluators/NDCG/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('NDCG - Normalize Discounted Cumulative Gain@' + str(at))
    plt.xlabel('ID do execução')
    plt.ylabel('Valor do NDCG')
    plt.plot([evaluation.id for evaluation in allEvaluations],[evaluation for evaluation in evaluationValues],color='red',label='Valor')
    plt.plot([evaluation.id for evaluation in allEvaluations],[evaluation for evaluation in evaluationMeanValues],color='green',label='Media')
    plt.plot([evaluation.id for evaluation in allEvaluations],[evaluation for evaluation in evaluationMedianValues],color='blue',label='Mediana')
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gLine-[' + str(at) + '].png')
    plt.close()
    logger.info("[Finish NDCG Value (Graph Line)]")
def value_gScatter(at=5):
    logger.info("[Start NDCG Value (Graph Scatter)]")
    allEvaluations = NDCG.objects.filter(limit=at)
    evaluationValues = [ ]
    evaluationMeanValues = [ ]
    evaluationMedianValues = [ ]
    for evaluation in allEvaluations:
        evaluationValues.append(evaluation.value)
        evaluationMeanValues.append(np.mean(evaluationValues))
        evaluationMedianValues.append(np.median(evaluationValues))
    logger.debug("NDCG Evaluation -> Mean: " + str(evaluationMeanValues[-1]))
    logger.debug("NDCG Evaluation -> Median: " + str(evaluationMedianValues[-1]))
    logger.debug("NDCG Evaluation -> Run Number: " + str(len(evaluationValues)))
    directory = str('./files/apps/evaluators/NDCG/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('NDCG - Normalize Discounted Cumulative Gain@' + str(at))
    plt.ylabel('Valor NDCG')
    plt.xlabel('Valor NDCG')
    plt.scatter(evaluationValues, evaluationValues, label='Media: ' + str(float("{0:.4f}".format(evaluationValues[-1]))))
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'value_gScatter-[' + str(at) + '].png')
    plt.close()
    logger.info("[Finish NDCG Value (Graph Scatter)]")
def value_gBoxPlot(at=5):
    logger.info("[Start NDCG Value (Graph BoxPlot)]")
    allEvaluations = NDCG.objects.filter(limit=at)
    evaluationValues = [(evalution.value) for evalution in allEvaluations]
    logger.debug("NDCG Evaluation -> Run Number: " + str(len(evaluationValues)))
    directory = str('./files/apps/evaluators/NDCG/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('NDCG - Normalize Discounted Cumulative Gain@' + str(at))
    plt.boxplot(evaluationValues, labels='V')
    plt.savefig(str(directory) + 'value_gBoxPlot-[' + str(at) + '].png')
    plt.close()
    logger.info("[Finish NDCG Value (Graph BoxPlot)]")
def value_gBar(at=5):
    logger.info("[Start NDCG Value (Graph Bar)]")
    allEvaluations = NDCG.objects.filter(limit=at)
    evaluationValues = [float("{0:.4f}".format(evalution.value)) for evalution in allEvaluations]
    evalutionCountList = Counter(evaluationValues)
    mode = evalutionCountList.most_common(1)[0][0]
    logger.debug('NDCG Evaluation -> Mode: ' + str(mode))
    directory = str('./files/apps/evaluators/NDCG/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('NDCG - Normalize Discounted Cumulative Gain@' + str(at))
    plt.ylabel('Intervalor de valores')
    plt.xlabel('Quantidade')
    plt.bar(evalutionCountList.values(),evalutionCountList.keys(), label='Moda: ' + str(float("{0:.4f}".format(mode))))
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gBar-[' + str(at) + '].png')
    plt.close()
    logger.info("[Finish NDCG Value (Graph Bar)]")
