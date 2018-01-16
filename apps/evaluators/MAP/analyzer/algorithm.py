import matplotlib.pyplot as plt
import numpy as np
import logging
import os
from collections import Counter
from django.db import connection
from apps.evaluators.MAP.algorithm.models import MAP
from apps.recommenders.UserAverage.algorithm.models import UserAverage_Life

logger = logging.getLogger(__name__)

def value_gLine(at=5,songSetLimit):
    logger.info("[Start MAP Value (Graph Line)]")
    allEvaluations = MAP.objects.filter(at=at,life_id=UserAverage_Life.objects.last())
    evaluationValues = [ ]
    evaluationMeanValues = [ ]
    evaluationMedianValues = [ ]
    for evaluation in allEvaluations:
        evaluationValues.append(evaluation.value)
        evaluationMeanValues.append(np.mean(evaluationValues))
        evaluationMedianValues.append(np.median(evaluationValues))
    logger.debug("MAP Evaluation -> Mean: " + str(evaluationMeanValues[-1]))
    logger.debug("MAP Evaluation -> Median: " + str(evaluationMedianValues[-1]))
    logger.debug("MAP Evaluation -> Run Number: " + str(len(evaluationValues)))
    directory = str('./files/apps/evaluators/MAP/graphs/' + str(songSetLimit) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('MAP - Mean Averange Precision@' + str(at))
    plt.xlabel('ID do execução')
    plt.ylabel('Valor do MAP')
    plt.plot([evaluation.id for evaluation in allEvaluations],[evaluation for evaluation in evaluationValues],color='red',label='Valor')
    plt.plot([evaluation.id for evaluation in allEvaluations],[evaluation for evaluation in evaluationMeanValues],color='green',label='Media')
    plt.plot([evaluation.id for evaluation in allEvaluations],[evaluation for evaluation in evaluationMedianValues],color='blue',label='Mediana')
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gLine-[' + str(at) + '].png')
    plt.close()
    logger.info("[Finish MAP Value (Graph Line)]")
def value_gScatter(at=5,songSetLimit):
    logger.info("[Start MAP Value (Graph Scatter)]")
    allEvaluations = MAP.objects.filter(at=at,life_id=UserAverage_Life.objects.last())
    evaluationValues = [ ]
    evaluationMeanValues = [ ]
    evaluationMedianValues = [ ]
    for evaluation in allEvaluations:
        evaluationValues.append(evaluation.value)
        evaluationMeanValues.append(np.mean(evaluationValues))
        evaluationMedianValues.append(np.median(evaluationValues))
    logger.debug("MAP Evaluation -> Mean: " + str(evaluationMeanValues[-1]))
    logger.debug("MAP Evaluation -> Median: " + str(evaluationMedianValues[-1]))
    logger.debug("MAP Evaluation -> Run Number: " + str(len(evaluationValues)))
    directory = str('./files/apps/evaluators/MAP/graphs/' + str(songSetLimit) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('MAP - Mean Averange Precision@' + str(at))
    plt.ylabel('Valor MAP')
    plt.xlabel('Valor MAP')
    plt.scatter(evaluationValues, evaluationValues, label='Media: ' + str(float("{0:.4f}".format(evaluationValues[-1]))))
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'value_gScatter-[' + str(at) + '].png')
    plt.close()
    logger.info("[Finish MAP Value (Graph Scatter)]")
def value_gBoxPlot(at=5,songSetLimit):
    logger.info("[Start MAP Value (Graph BoxPlot)]")
    allEvaluations = MAP.objects.filter(at=at,life_id=UserAverage_Life.objects.last())
    evaluationValues = [(evalution.value) for evalution in allEvaluations]
    logger.debug("MAP Evaluation -> Run Number: " + str(len(evaluationValues)))
    directory = str('./files/apps/evaluators/MAP/graphs/' + str(songSetLimit) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('MAP - Mean Averange Precision@' + str(at))
    plt.boxplot(evaluationValues, labels='V')
    plt.savefig(str(directory) + 'value_gBoxPlot-[' + str(at) + '].png')
    plt.close()
    logger.info("[Finish MAP Value (Graph BoxPlot)]")
def value_gBar(at=5,songSetLimit):
    logger.info("[Start MAP Value (Graph Bar)]")
    allEvaluations = MAP.objects.filter(at=at,life_id=UserAverage_Life.objects.last())
    evaluationValues = [float("{0:.4f}".format(evalution.value)) for evalution in allEvaluations]
    evalutionCountList = Counter(evaluationValues)
    mode = evalutionCountList.most_common(1)[0][0]
    logger.debug('MAP Evaluation -> Mode: ' + str(mode))
    directory = str('./files/apps/evaluators/MAP/graphs/' + str(songSetLimit) + '/algorithm/' + str(allEvaluations.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('MAP - Mean Averange Precision@' + str(at))
    plt.ylabel('Intervalor de valores')
    plt.xlabel('Quantidade')
    plt.bar(evalutionCountList.values(),evalutionCountList.keys(), label='Moda: ' + str(float("{0:.4f}".format(mode))))
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gBar-[' + str(at) + '].png')
    plt.close()
    logger.info("[Finish MAP Value (Graph Bar)]")
