import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.evaluators.MRR.algorithm.models import MRR
from django.db import connection

directory = str('./apps/evaluators/MRR/analyzer/graphs/' + str(connection.settings_dict['NAME'] + '/'))
if not os.path.exists(directory):
    os.makedirs(directory)
def value_gLine(at=5):
    allEvaluations = MRR.objects.filter(limit=at)
    evaluationValues = [evalution.value for evalution in allEvaluations]
    evaluationMean = np.mean(evaluationValues)
    evaluationMedian = np.median(evaluationValues)
    plt.figure()
    plt.grid(True)
    plt.title('MRR - Mean Reciprocal Rank@' + str(at))
    plt.xlabel('ID do MRR')
    plt.ylabel('Valor do MRR')
    plt.text(-0.1, 1, r'Media: ' + str(evaluationMean))
    plt.text(-0.1, .8, r'Mediana: ' + str(evaluationMedian))
    plt.plot([evalution.id for evalution in allEvaluations],[evalution.value for evalution in allEvaluations])
    plt.savefig(str(directory) + 'value_gLine' + '-[id]-'+ str(allEvaluations.last().id) + '.png')

def value_gScatter(at=5):
    allEvaluations = MRR.objects.filter(limit=at)
    evaluationValues = [evalution.value for evalution in allEvaluations]
    evaluationMean = np.mean(evaluationValues)
    evaluationMedian = np.median(evaluationValues)
    plt.figure()
    plt.grid(True)
    plt.title('MRR - Mean Reciprocal Rank@' + str(at))
    plt.ylabel('Valor MRR')
    plt.xlabel('Valor MRR')
    plt.text(-0.1, 1, r'Media: ' + str(float("{0:.2f}".format(evaluationMean))))
    plt.text(-0.1, .8, r'Mediana: ' + str(float("{0:.2f}".format(evaluationMedian))))
    plt.scatter(evaluationValues, evaluationValues)
    plt.axis([-0.2, 1.2, -0.2, 1.2])
    plt.savefig(str(directory) + 'value_gScatter' + '-[id]-'+ str(allEvaluations.last().id) + '.png')

def value_gBoxPlot(at=5):
    allEvaluations = MRR.objects.filter(limit=at)
    evaluationValues = [evalution.value for evalution in allEvaluations]
    plt.figure()
    plt.title('MRR - Mean Reciprocal Rank@' + str(at))
    plt.boxplot(evaluationValues)
    plt.savefig(str(directory) + 'value_gBoxPlot' + '-[id]-'+ str(allEvaluations.last().id) + '.png')

def value_gBar(at=5):
    allEvaluations = MRR.objects.filter(limit=at)
    evaluationValues = [float("{0:.1f}".format(evalution.value)) for evalution in allEvaluations]
    evalutionCountList = Counter(evaluationValues)
    plt.figure()
    plt.title('MRR - Mean Reciprocal Rank@' + str(at))
    plt.ylabel('Intervalor de valores')
    plt.xlabel('Quantidade')
    plt.bar(evalutionCountList.values(),evalutionCountList.keys())
    plt.savefig(str(directory) + 'value_gBar' + '-[id]-'+ str(allEvaluations.last().id) + '.png')
