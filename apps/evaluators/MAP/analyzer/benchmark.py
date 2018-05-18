import matplotlib.pyplot as plt
import numpy as np
import logging
import os

from collections import Counter
from apps.CONSTANTS import (
    SET_SIZE_LIST,
    START_VALIDE_RUN,
    INTERVAL,
    AT_LIST
)
from apps.data.users.models import User
from apps.evaluators.MAP.algorithm.models import MAP

logger = logging.getLogger(__name__)


def bench_gLine(songSetLimit, at=5):
    logger.info("[Start Bench MAP (Graph Line)]")
    allBenchmarks = []
    for evalution in MAP.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchmap)
    benchmarkTimes = []
    benchmarkMeanTimes = []
    benchmarkMedianTimes = []
    for benchmark in allBenchmarks:
        timeRun = (benchmark.finished_at - benchmark.started_at)
        benchmarkTimes.append(timeRun.total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug(
        "MAP Benchmark -> Mean (minutes): "
        + str(benchmarkMeanTimes[-1])
    )
    logger.debug(
        "MAP Benchmark -> Median (minutes): "
        + str(benchmarkMedianTimes[-1])
    )
    logger.debug(
        "MAP Benchmark -> Run Number: "
        + str(len(benchmarkTimes))
    )
    directory = str(
        'files/apps/evaluators/MAP/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'MAP - Mean Averange Precision@'
        + str(at)
        + '\nBenchmark - set '
        + str(songSetLimit)
    )
    plt.xlabel('ID da execução')
    plt.ylabel('Tempo de execução (minutos)')
    plt.plot(
        [i for i in range(len(allBenchmarks))],
        [benchmark for benchmark in benchmarkTimes],
        color='red',
        label='Tempo'
    )
    plt.plot(
        [i for i in range(len(allBenchmarks))],
        [benchmark for benchmark in benchmarkMeanTimes],
        color='green',
        label='Media'
    )
    plt.plot(
        [i for i in range(len(allBenchmarks))],
        [benchmark for benchmark in benchmarkMedianTimes],
        color='blue',
        label='Mediana'
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'value_gLine.png'
    )
    plt.close()
    logger.info("[Finish Bench MAP (Graph Line)]")


def bench_gScatter(songSetLimit, at=5):
    logger.info("[Start Bench MAP (Graph Scatter)]")
    allBenchmarks = []
    for evalution in MAP.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchmap)
    benchmarkTimes = []
    benchmarkMeanTimes = []
    benchmarkMedianTimes = []
    for benchmark in allBenchmarks:
        timeRun = (benchmark.finished_at - benchmark.started_at)
        benchmarkTimes.append(timeRun.total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug(
        "MAP Benchmark -> Mean (minutes): "
        + str(benchmarkMeanTimes[-1])
    )
    logger.debug(
        "MAP Benchmark -> Median (minutes): "
        + str(benchmarkMedianTimes[-1])
    )
    logger.debug(
        "MAP Benchmark -> Run Number: "
        + str(len(benchmarkTimes))
    )
    directory = str(
        'files/apps/evaluators/MAP/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'MAP - Mean Averange Precision@'
        + str(at)
        + '\nBenchmark - set '
        + str(songSetLimit)
    )
    plt.ylabel('Tempo de execução (minutos)')
    plt.xlabel('Tempo de execução (minutos)')
    plt.scatter(
        benchmarkTimes,
        benchmarkTimes,
        label='Media: '
        + str(float("{0:.4f}".format(benchmarkMeanTimes[-1])))
    )
    plt.legend(loc='upper left')
    plt.savefig(
        str(directory)
        + 'value_gScatter.png'
    )
    plt.close()
    logger.info("[Finish Bench MAP (Graph Scatter)]")


def bench_gBoxPlot(songSetLimit, at=5):
    logger.info("[Start Bench MAP (Graph BoxPlot)]")
    allBenchmarks = []
    for evalution in MAP.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchmap)
    benchmarkTimes = []
    benchmarkMeanTimes = []
    benchmarkMedianTimes = []
    for benchmark in allBenchmarks:
        timeRun = (benchmark.finished_at - benchmark.started_at)
        benchmarkTimes.append(timeRun.total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug(
        "MAP Benchmark -> Mean (minutes): "
        + str(benchmarkMeanTimes[-1])
    )
    logger.debug(
        "MAP Benchmark -> Median (minutes): "
        + str(benchmarkMedianTimes[-1])
    )
    logger.debug(
        "MAP Benchmark -> Run Number: "
        + str(len(benchmarkTimes))
    )
    directory = str(
        'files/apps/evaluators/MAP/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'MAP - Mean Averange Precision@'
        + str(at)
        + '\nBenchmark - set '
        + str(songSetLimit)
    )
    plt.boxplot(benchmarkTimes, labels='T')
    plt.savefig(
        str(directory)
        + 'value_gBoxPlot.png'
    )
    plt.close()
    logger.info("[Finish Bench MAP (Graph BoxPlot)]")


def bench_gBar(songSetLimit, at=5):
    logger.info("[Start Bench MAP (Graph Bar)]")
    allBenchmarks = []
    for evalution in MAP.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchmap)
    benchmarkTimes = [
        float("{0:.3f}".format(
                (
                    benchmark.finished_at - benchmark.started_at
                ).total_seconds() / 60.0
            )
        )
        for benchmark in allBenchmarks
    ]
    benchmarkCountList = Counter(benchmarkTimes)
    mode = benchmarkCountList.most_common(1)[0][0]
    logger.debug('MAP Benchmark -> Mode: ' + str(mode))
    directory = str(
        'files/apps/evaluators/MAP/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'MAP - Mean Averange Precision@'
        + str(at)
        + '\nBenchmark - set '
        + str(songSetLimit)
    )
    plt.ylabel('Tempo execução (minutos)')
    plt.xlabel('Quantidade')
    plt.bar(
        benchmarkCountList.values(),
        benchmarkCountList.keys()
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'value_gBar.png'
    )
    plt.close()
    logger.info("[Finish Bench MAP (Graph Bar)]")

# ###################################################################### #


def all_time_gLine(at=5, size_list=SET_SIZE_LIST):
    logger.info("[Start Bench MAP (Graph Line)]")
    allBenchmarks = {}
    for evalution in MAP.objects.filter(at=at):
        if evalution.life.setSize not in allBenchmarks:
            allBenchmarks.setdefault(evalution.life.setSize, [])
        else:
            allBenchmarks[evalution.life.setSize].append(
                (
                    evalution.benchmap.finished_at - evalution.benchmap.started_at
                ).total_seconds() / 60.0
            )
    directory = str(
        'files/apps/evaluators/MAP/graphs/all/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'MAP - Mean Averange Precision@'
        + str(at)
        + ' Benchmark'
        + '\n |u| - '
        + str(User.objects.count())
    )
    plt.xlabel('Round Id')
    plt.ylabel('Round time (minute)')
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[0]][-INTERVAL:]))],
        [benchmark for benchmark in allBenchmarks[size_list[0]][-INTERVAL:]],
        color='red',
        label=size_list[0]
    )
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[1]][-INTERVAL:]))],
        [benchmark for benchmark in allBenchmarks[size_list[1]][-INTERVAL:]],
        color='green',
        label=size_list[1]
    )
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[2]][-INTERVAL:]))],
        [benchmark for benchmark in allBenchmarks[size_list[2]][-INTERVAL:]],
        color='blue',
        label=size_list[2]
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'map_all_time_gLine_'
        + str(at)
        + '.png'
    )
    plt.close()
    logger.info("[Finish Bench MAP (Graph Line)]")


def all_time_gBoxPlot(at=5, size_list=SET_SIZE_LIST):
    logger.info("[Start Bench MAP (Graph BoxPlot)]")
    allBenchmarks = {}
    for evalution in MAP.objects.filter(at=at):
        if evalution.life.setSize not in allBenchmarks:
            allBenchmarks.setdefault(evalution.life.setSize, [])
        else:
            allBenchmarks[evalution.life.setSize].append(
                (
                    evalution.benchmap.finished_at - evalution.benchmap.started_at
                ).total_seconds() / 60.0
            )
    directory = str(
        'files/apps/evaluators/MAP/graphs/all/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'MAP - Mean Averange Precision@'
        + str(at)
        + ' Benchmark'
        + '\n |u| - '
        + str(User.objects.count())
    )
    plt.ylabel('Round time (minute)')
    plt.boxplot(
        [
            [benchmark for benchmark in allBenchmarks[size_list[0]][-INTERVAL:]],
            [benchmark for benchmark in allBenchmarks[size_list[1]][-INTERVAL:]],
            [benchmark for benchmark in allBenchmarks[size_list[2]][-INTERVAL:]]
        ],
        labels=[size_list[0], size_list[1], size_list[2]]
    )
    plt.savefig(
        str(directory)
        + 'map_all_time_gBoxPlot_'
        + str(at)
        + '.png'
    )
    plt.close()
    logger.info("[Finish Bench MAP (Graph BoxPlot)]")


# ########################################################################## #
# ########################################################################## #
# ########################################################################## #


def report_MAP_time(at_list=AT_LIST, size_list=SET_SIZE_LIST):
    logger.info("[Start MAP Report]")
    allEvaluations = {}
    for at in at_list:
        allEvaluations_at = {}
        for evalution in MAP.objects.filter(at=at):
            if evalution.life.setSize not in allEvaluations_at:
                allEvaluations_at.setdefault(evalution.life.setSize, [])
                allEvaluations_at[evalution.life.setSize].append(evalution.benchmap)
            else:
                allEvaluations_at[evalution.life.setSize].append(evalution.benchmap)
        allEvaluations[at] = allEvaluations_at
    directory = str(
        'files/apps/evaluators/MAP/csv/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    toSaveFile = open(
        directory + 'map_time.csv',
        'w+'
    )
    toSaveFile.write('at,size,mean\n')
    for at in at_list:
        for size in size_list:
            meanAT = np.mean(
                [
                    (benchmark.finished_at - benchmark.started_at).total_seconds()/60.0
                    for benchmark in allEvaluations[at][size][-INTERVAL:]]
            )
            toSaveFile.write(str(at) + ',' + str(size) + ',' + str(float("{0:.3f}".format(meanAT))) + '\n')
            print('|' + str(at) + '|' + str(size) + '|' + str(float("{0:.3f}".format(meanAT))) + "\t|")
    toSaveFile.close()
