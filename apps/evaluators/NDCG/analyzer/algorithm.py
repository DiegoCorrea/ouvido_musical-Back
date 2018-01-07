import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.evaluators.MRR.algorithm.models import MRR
from django.db import connection
import logging

logger = logging.getLogger(__name__)

def value_gLine(at=5):
    logger.info("[Start MRR Value (Graph Line)]")
    allEvaluations = MRR.objects.filter(limit=at)
    evaluationValues = [ ]
    evaluationMeanValues = [ ]
    evaluationMedianValues = [ ]
    for evaluation in allEvaluations:
        evaluationValues.append(evaluation.value)
        evaluationMeanValues.append(np.mean(evaluationValues))
        evaluationMedianValues.append(np.median(evaluationValues))
    logger.debug("MRR Evaluation -> Mean: " + str(evaluationMeanValues[-1]))
    logger.debug("MRR Evaluation -> Median: " + str(evaluationMedianValues[-1]))
    logger.debug("MRR Evaluation -> Run Number: " + str(len(evaluationValues)))
    directory = str('./apps/evaluators/MRR/analyzer/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('MRR - Mean Reciprocal Rank@' + str(at))
    plt.xlabel('ID do execução')
    plt.ylabel('Valor do MRR')
    plt.plot([evaluation.id for evaluation in allEvaluations],[evaluation for evaluation in evaluationValues],color='red',label='Valor')
    plt.plot([evaluation.id for evaluation in allEvaluations],[evaluation for evaluation in evaluationMeanValues],color='green',label='Media')
    plt.plot([evaluation.id for evaluation in allEvaluations],[evaluation for evaluation in evaluationMedianValues],color='blue',label='Mediana')
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gLine.png')
    logger.info("[Finish MRR Value (Graph Line)]")
def value_gScatter(at=5):
    logger.info("[Start MRR Value (Graph Scatter)]")
    allEvaluations = MRR.objects.filter(limit=at)
    evaluationValues = [ ]
    evaluationMeanValues = [ ]
    evaluationMedianValues = [ ]
    for evaluation in allEvaluations:
        evaluationValues.append(evaluation.value)
        evaluationMeanValues.append(np.mean(evaluationValues))
        evaluationMedianValues.append(np.median(evaluationValues))
    logger.debug("MRR Evaluation -> Mean: " + str(evaluationMeanValues[-1]))
    logger.debug("MRR Evaluation -> Median: " + str(evaluationMedianValues[-1]))
    logger.debug("MRR Evaluation -> Run Number: " + str(len(evaluationValues)))
    directory = str('./apps/evaluators/MRR/analyzer/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('MRR - Mean Reciprocal Rank@' + str(at))
    plt.ylabel('Valor MRR')
    plt.xlabel('Valor MRR')
    plt.scatter(evaluationValues, evaluationValues, label='Media: ' + str(float("{0:.4f}".format(evaluationValues[-1]))))
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'value_gScatter.png')
    logger.info("[Finish MRR Value (Graph Scatter)]")
def value_gBoxPlot(at=5):
    logger.info("[Start MRR Value (Graph BoxPlot)]")
    allEvaluations = MRR.objects.filter(limit=at)
    evaluationValues = [(evalution.value) for evalution in allEvaluations]
    logger.debug("MRR Evaluation -> Run Number: " + str(len(evaluationValues)))
    directory = str('./apps/evaluators/MRR/analyzer/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('MRR - Mean Reciprocal Rank@' + str(at))
    plt.boxplot(evaluationValues, labels='V')
    plt.savefig(str(directory) + 'value_gBoxPlot.png')
    logger.info("[Finish MRR Value (Graph BoxPlot)]")
def value_gBar(at=5):
    logger.info("[Start MRR Value (Graph Bar)]")
    allEvaluations = MRR.objects.filter(limit=at)
    evaluationValues = [float("{0:.4f}".format(evalution.value)) for evalution in allEvaluations]
    evalutionCountList = Counter(evaluationValues)
    mode = evalutionCountList.most_common(1)[0][0]
    logger.debug('MRR Evaluation -> Mode: ' + str(mode))
    directory = str('./apps/evaluators/MRR/analyzer/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('MRR - Mean Reciprocal Rank@' + str(at))
    plt.ylabel('Intervalor de valores')
    plt.xlabel('Quantidade')
    plt.bar(evalutionCountList.values(),evalutionCountList.keys(), label='Moda: ' + str(float("{0:.4f}".format(mode))))
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gBar.png')
    logger.info("[Finish MRR Value (Graph Bar)]")
