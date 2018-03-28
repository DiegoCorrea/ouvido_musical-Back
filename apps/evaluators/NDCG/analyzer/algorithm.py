import matplotlib.pyplot as plt
import numpy as np
import logging
import os

from collections import Counter
from apps.CONSTANTS import SET_SIZE_LIST
from apps.data.users.models import User
from apps.evaluators.NDCG.algorithm.models import NDCG

logger = logging.getLogger(__name__)


def value_gLine(songSetLimit, at=5):
    logger.info("[Start NDCG Value (Graph Line)]")
    allEvaluations = []
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allEvaluations.append(evalution)
    evaluationValues = []
    evaluationMeanValues = []
    evaluationMedianValues = []
    for evaluation in allEvaluations:
        evaluationValues.append(evaluation.value)
        evaluationMeanValues.append(np.mean(evaluationValues))
        evaluationMedianValues.append(np.median(evaluationValues))
    logger.debug(
        "NDCG Evaluation -> Mean: "
        + str(evaluationMeanValues[-1])
    )
    logger.debug(
        "NDCG Evaluation -> Median: "
        + str(evaluationMedianValues[-1])
    )
    logger.debug(
        "NDCG Evaluation -> Run Number: "
        + str(len(evaluationValues))
    )
    directory = str(
        './files/apps/evaluators/NDCG/graphs/'
        + str(songSetLimit)
        + '/algorithm/'
        + str(at)
        + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'NDCG - Normalize Discounted Cumulative Gain@'
        + str(at)
        + '\nSet - '
        + str(songSetLimit)
    )
    plt.xlabel('ID do execução')
    plt.ylabel('Valor do NDCG')
    plt.plot(
        [i for i in range(len(allEvaluations))],
        [evaluation for evaluation in evaluationValues],
        color='red',
        label='Valor'
    )
    plt.plot(
        [i for i in range(len(allEvaluations))],
        [evaluation for evaluation in evaluationMeanValues],
        color='green',
        label='Media'
    )
    plt.plot(
        [i for i in range(len(allEvaluations))],
        [evaluation for evaluation in evaluationMedianValues],
        color='blue',
        label='Mediana'
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'value_gLine.png'
    )
    plt.close()
    logger.info("[Finish NDCG Value (Graph Line)]")


def value_gScatter(songSetLimit, at=5):
    logger.info("[Start NDCG Value (Graph Scatter)]")
    allEvaluations = []
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allEvaluations.append(evalution)
    evaluationValues = []
    evaluationMeanValues = []
    evaluationMedianValues = []
    for evaluation in allEvaluations:
        evaluationValues.append(evaluation.value)
        evaluationMeanValues.append(np.mean(evaluationValues))
        evaluationMedianValues.append(np.median(evaluationValues))
    logger.debug(
        "NDCG Evaluation -> Mean: "
        + str(evaluationMeanValues[-1])
    )
    logger.debug(
        "NDCG Evaluation -> Median: "
        + str(evaluationMedianValues[-1])
    )
    logger.debug(
        "NDCG Evaluation -> Run Number: "
        + str(len(evaluationValues))
    )
    directory = str(
        './files/apps/evaluators/NDCG/graphs/'
        + str(songSetLimit)
        + '/algorithm/'
        + str(at)
        + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'NDCG - Normalize Discounted Cumulative Gain@'
        + str(at)
        + '\nSet - '
        + str(songSetLimit)
    )
    plt.ylabel('Valor NDCG')
    plt.xlabel('Valor NDCG')
    plt.scatter(
        evaluationValues,
        evaluationValues,
        label='Media: '
        + str(float("{0:.4f}".format(evaluationValues[-1])))
    )
    plt.legend(loc='upper left')
    plt.savefig(
        str(directory)
        + 'value_gScatter.png'
    )
    plt.close()
    logger.info("[Finish NDCG Value (Graph Scatter)]")


def value_gBoxPlot(songSetLimit, at=5):
    logger.info("[Start NDCG Value (Graph BoxPlot)]")
    allEvaluations = []
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allEvaluations.append(evalution)
    evaluationValues = [
        (evalution.value)
        for evalution in allEvaluations
    ]
    logger.debug(
        "NDCG Evaluation -> Run Number: "
        + str(len(evaluationValues))
    )
    directory = str(
        './files/apps/evaluators/NDCG/graphs/'
        + str(songSetLimit)
        + '/algorithm/'
        + str(at)
        + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'NDCG - Normalize Discounted Cumulative Gain@'
        + str(at)
        + '\nSet - '
        + str(songSetLimit)
    )
    plt.boxplot(evaluationValues, labels='V')
    plt.savefig(
        str(directory)
        + 'value_gBoxPlot.png'
    )
    plt.close()
    logger.info("[Finish NDCG Value (Graph BoxPlot)]")


def value_gBar(songSetLimit, at=5):
    logger.info("[Start NDCG Value (Graph Bar)]")
    allEvaluations = []
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allEvaluations.append(evalution)
    evaluationValues = [
        float("{0:.4f}".format(evalution.value))
        for evalution in allEvaluations
    ]
    evalutionCountList = Counter(evaluationValues)
    mode = evalutionCountList.most_common(1)[0][0]
    logger.debug('NDCG Evaluation -> Mode: ' + str(mode))
    directory = str(
        './files/apps/evaluators/NDCG/graphs/'
        + str(songSetLimit)
        + '/algorithm/'
        + str(at)
        + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'NDCG - Normalize Discounted Cumulative Gain@'
        + str(at)
        + '\nSet - '
        + str(songSetLimit)
    )
    plt.ylabel('Intervalor de valores')
    plt.xlabel('Quantidade')
    plt.bar(
        evalutionCountList.values(),
        evalutionCountList.keys(),
        label='Moda: '
        + str(float("{0:.4f}".format(mode)))
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'value_gBar.png'
    )
    plt.close()
    logger.info("[Finish NDCG Value (Graph Bar)]")


# ########################################################################## #


def all_value_gLine(at=5, size_list=SET_SIZE_LIST):
    logger.info("[Start NDCG Value (Graph Line)]")
    allEvaluations = {}
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize not in allEvaluations:
            allEvaluations.setdefault(evalution.life.setSize, [])
        else:
            allEvaluations[evalution.life.setSize].append(evalution)
    directory = str(
        'files/apps/evaluators/NDCG/graphs/all/'
        + str(at)
        + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'NDCG - Normalize Discounted Cumulative Gain@'
        + str(at)
        + '\n |u| - '
        + str(User.objects.count())
    )
    plt.xlabel('Round Id')
    plt.ylabel('NDCG value')
    plt.plot(
        [i+1 for i in range(len(allEvaluations[size_list[0]]))],
        [evaluation.value for evaluation in allEvaluations[size_list[0]]],
        color='red',
        label=size_list[0]
        )
    plt.plot(
        [i+1 for i in range(len(allEvaluations[size_list[1]]))],
        [evaluation.value for evaluation in allEvaluations[size_list[1]]],
        color='green',
        label=size_list[1]
    )
    plt.plot(
        [i+1 for i in range(len(allEvaluations[size_list[2]]))],
        [evaluation.value for evaluation in allEvaluations[size_list[2]]],
        color='blue',
        label=size_list[2]
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'ndcg_all_algorithm_gLine_'
        + str(at)
        + '.png'
    )
    plt.close()
    logger.info("[Finish NDCG Value (Graph Line)]")


def all_value_gBoxPlot(at=5, size_list=SET_SIZE_LIST):
    logger.info("[Start NDCG Value (Graph BoxPlot)]")
    allEvaluations = {}
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize not in allEvaluations:
            allEvaluations.setdefault(evalution.life.setSize, [])
        else:
            allEvaluations[evalution.life.setSize].append(evalution)
    directory = str(
        'files/apps/evaluators/NDCG/graphs/all/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'NDCG - Normalize Discounted Cumulative Gain@'
        + str(at)
        + '\n |u| - '
        + str(User.objects.count())
    )
    plt.ylabel('NDCG value')
    plt.boxplot(
        [
            [evaluation.value for evaluation in allEvaluations[size_list[0]]],
            [evaluation.value for evaluation in allEvaluations[size_list[1]]],
            [evaluation.value for evaluation in allEvaluations[size_list[2]]]
        ],
        labels=[size_list[0], size_list[1], size_list[2]]
    )
    plt.savefig(
        str(directory)
        + 'all_algorithm_gBoxPlot_'
        + str(at)
        + '.png'
    )
    plt.close()
    logger.info("[Finish NDCG Value (Graph BoxPlot)]")
