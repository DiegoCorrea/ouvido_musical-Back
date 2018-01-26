import matplotlib.pyplot as plt
import numpy as np
import logging
import os

from collections import Counter
from apps.data.users.models import User
from apps.evaluators.MAP.algorithm.models import MAP

logger = logging.getLogger(__name__)


def value_gLine(songSetLimit, at=5):
    logger.info("[Start MAP Value (Graph Line)]")
    allEvaluations = []
    for evalution in MAP.objects.filter(at=at):
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
        "MAP Evaluation -> Mean: "
        + str(evaluationMeanValues[-1])
    )
    logger.debug(
        "MAP Evaluation -> Median: "
        + str(evaluationMedianValues[-1])
    )
    logger.debug(
        "MAP Evaluation -> Run Number: "
        + str(len(evaluationValues))
    )
    directory = str(
        'files/apps/evaluators/MAP/graphs/'
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
        'MAP - Mean Averange Precision@'
        + str(at)
        + '\nSet - '
        + str(songSetLimit)
    )
    plt.xlabel('ID do execução')
    plt.ylabel('Valor do MAP')
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
    plt.savefig(str(directory) + 'value_gLine.png')
    plt.close()
    logger.info("[Finish MAP Value (Graph Line)]")


def value_gScatter(songSetLimit, at=5):
    logger.info("[Start MAP Value (Graph Scatter)]")
    allEvaluations = []
    for evalution in MAP.objects.filter(at=at):
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
        "MAP Evaluation -> Mean: "
        + str(evaluationMeanValues[-1])
    )
    logger.debug(
        "MAP Evaluation -> Median: "
        + str(evaluationMedianValues[-1])
    )
    logger.debug(
        "MAP Evaluation -> Run Number: "
        + str(len(evaluationValues))
    )
    directory = str(
        'files/apps/evaluators/MAP/graphs/'
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
        'MAP - Mean Averange Precision@'
        + str(at)
        + '\nSet - '
        + str(songSetLimit)
    )
    plt.ylabel('Valor MAP')
    plt.xlabel('Valor MAP')
    plt.scatter(
        evaluationValues,
        evaluationValues,
        label='Media: '
        + str(float("{0:.4f}".format(evaluationValues[-1])))
    )
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'value_gScatter.png')
    plt.close()
    logger.info("[Finish MAP Value (Graph Scatter)]")


def value_gBoxPlot(songSetLimit, at=5):
    logger.info("[Start MAP Value (Graph BoxPlot)]")
    allEvaluations = []
    for evalution in MAP.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allEvaluations.append(evalution)
    evaluationValues = [
        (evalution.value)
        for evalution in allEvaluations
    ]
    logger.debug(
        "MAP Evaluation -> Run Number: "
        + str(len(evaluationValues))
    )
    directory = str(
        'files/apps/evaluators/MAP/graphs/'
        + str(songSetLimit)
        + '/algorithm/'
        + str(at)
        + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'MAP - Mean Averange Precision@'
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
    logger.info("[Finish MAP Value (Graph BoxPlot)]")


def value_gBar(songSetLimit, at=5):
    logger.info("[Start MAP Value (Graph Bar)]")
    allEvaluations = []
    for evalution in MAP.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allEvaluations.append(evalution)
    evaluationValues = [
        float("{0:.4f}".format(evalution.value))
        for evalution in allEvaluations
    ]
    evalutionCountList = Counter(evaluationValues)
    mode = evalutionCountList.most_common(1)[0][0]
    logger.debug('MAP Evaluation -> Mode: ' + str(mode))
    directory = str(
        'files/apps/evaluators/MAP/graphs/'
        + str(songSetLimit)
        + '/algorithm/'
        + str(at)
        + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'MAP - Mean Averange Precision@'
        + str(at)
        + '\nSet - '
        + str(songSetLimit)
    )
    plt.ylabel('Intervalor de valores')
    plt.xlabel('Quantidade')
    plt.bar(
        evalutionCountList.values(),
        evalutionCountList.keys(),
        label='Moda: ' + str(float("{0:.4f}".format(mode)))
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'value_gBar.png'
    )
    plt.close()
    logger.info("[Finish MAP Value (Graph Bar)]")


# ########################################################################## #


def all_value_gLine(at=5):
    logger.info("[Start MAP Value (Graph Line)]")
    allEvaluations = {}
    for evalution in MAP.objects.filter(at=at):
        if evalution.life.setSize not in allEvaluations:
            allEvaluations.setdefault(evalution.life.setSize, [])
        else:
            allEvaluations[evalution.life.setSize].append(evalution)
    directory = str(
        'files/apps/evaluators/MAP/graphs/all/'
        + 'algorithm/'
        + str(at)
        + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'MAP - Mean Averange Precision@'
        + str(at)
        + '\n User set - '
        + str(User.objects.count())
    )
    plt.xlabel('ID do execução')
    plt.ylabel('Valor do MAP')
    plt.plot(
        [i for i in range(len(allEvaluations[1000]))],
        [evaluation.value for evaluation in allEvaluations[1000]],
        color='red',
        label='1000'
        )
    plt.plot(
        [i for i in range(len(allEvaluations[2000]))],
        [evaluation.value for evaluation in allEvaluations[2000]],
        color='green',
        label='2000'
    )
    plt.plot(
        [i for i in range(len(allEvaluations[3000]))],
        [evaluation.value for evaluation in allEvaluations[3000]],
        color='blue',
        label='3000'
    )
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'all_value_gLine.png')
    plt.close()
    logger.info("[Finish MAP Value (Graph Line)]")


def all_value_gBoxPlot(at=5):
    logger.info("[Start MAP Value (Graph BoxPlot)]")
    allEvaluations = {}
    for evalution in MAP.objects.filter(at=at):
        if evalution.life.setSize not in allEvaluations:
            allEvaluations.setdefault(evalution.life.setSize, [])
        else:
            allEvaluations[evalution.life.setSize].append(evalution)
    directory = str(
        'files/apps/evaluators/MAP/graphs/all/'
        + 'algorithm/'
        + str(at)
        + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'MAP - Mean Averange Precision@'
        + str(at)
        + '\n User set - '
        + str(User.objects.count())
    )
    plt.boxplot(
        [
            [evaluation.value for evaluation in allEvaluations[1000]],
            [evaluation.value for evaluation in allEvaluations[2000]],
            [evaluation.value for evaluation in allEvaluations[3000]]
        ],
        labels=[1000, 2000, 3000]
    )
    plt.savefig(
        str(directory)
        + 'all_value_gBoxPlot.png'
    )
    plt.close()
    logger.info("[Finish MAP Value (Graph BoxPlot)]")
