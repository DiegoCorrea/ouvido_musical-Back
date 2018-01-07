import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.recommenders.UserAverage.algorithm.models import UserAverage_Recommendations
from django.db import connection
import logging

logger = logging.getLogger(__name__)

def value_gLine(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Value (Graph Line)]")
    itemValues = [ ]
    evaluationMeanValues = [ ]
    evaluationMedianValues = [ ]
    for evaluation in allItens:
        itemValues.append(evaluation.value)
        evaluationMeanValues.append(np.mean(itemValues))
        evaluationMedianValues.append(np.median(itemValues))
    logger.debug("User Average Evaluation -> Mean: " + str(evaluationMeanValues[-1]))
    logger.debug("User Average Evaluation -> Median: " + str(evaluationMedianValues[-1]))
    logger.debug("User Average Evaluation -> Run Number: " + str(len(itemValues)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('User Average - Mean Averange Precision@' + str(at))
    plt.xlabel('ID do execução')
    plt.ylabel('Valor do User Average')
    plt.plot([evaluation.id for evaluation in allItens],[evaluation for evaluation in itemValues],color='red',label='Valor')
    plt.plot([evaluation.id for evaluation in allItens],[evaluation for evaluation in evaluationMeanValues],color='green',label='Media')
    plt.plot([evaluation.id for evaluation in allItens],[evaluation for evaluation in evaluationMedianValues],color='blue',label='Mediana')
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gLine.png')
    plt.close()
    logger.info("[Finish User Average Value (Graph Line)]")
def value_gScatter(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Value (Graph Scatter)]")
    itemValues = [ ]
    evaluationMeanValues = [ ]
    evaluationMedianValues = [ ]
    for evaluation in allItens:
        itemValues.append(evaluation.value)
        evaluationMeanValues.append(np.mean(itemValues))
        evaluationMedianValues.append(np.median(itemValues))
    logger.debug("User Average Evaluation -> Mean: " + str(evaluationMeanValues[-1]))
    logger.debug("User Average Evaluation -> Median: " + str(evaluationMedianValues[-1]))
    logger.debug("User Average Evaluation -> Run Number: " + str(len(itemValues)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('User Average - Mean Averange Precision@' + str(at))
    plt.ylabel('Valor User Average')
    plt.xlabel('Valor User Average')
    plt.scatter(itemValues, itemValues, label='Media: ' + str(float("{0:.4f}".format(itemValues[-1]))))
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'value_gScatter.png')
    plt.close()
    logger.info("[Finish User Average Value (Graph Scatter)]")
def value_gBoxPlot(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Value (Graph BoxPlot)]")
    itemValues = [(evalution.value) for evalution in allItens]
    logger.debug("User Average Evaluation -> Run Number: " + str(len(itemValues)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('User Average - Mean Averange Precision@' + str(at))
    plt.boxplot(itemValues, labels='V')
    plt.savefig(str(directory) + 'value_gBoxPlot.png')
    plt.close()
    logger.info("[Finish User Average Value (Graph BoxPlot)]")
def value_gBar(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Score (Graph Bar)]")
    itemValues = [evalution.score for evalution in allItens]
    countList = Counter(itemValues)
    logger.debug('User Averange Benchmark -> List: ' + str(countList))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allItens.last().created_at) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('User Average - Score')
    plt.ylabel('Quantidade de usuários')
    plt.xlabel('Nota')
    plt.bar(countList.keys(), countList.values())
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gBar.png')
    plt.close()
    logger.info("[Finish User Average Score (Graph Bar)]")
