import matplotlib.pyplot as plt
import numpy as np
import logging
import os

from collections import Counter
from apps.CONSTANTS import SET_SIZE_LIST
from apps.data.users.models import User
from apps.evaluators.MRR.algorithm.models import MRR

logger = logging.getLogger(__name__)


def bench_gLine(songSetLimit, at=5):
    logger.info("[Start Bench MRR (Graph Line)]")
    allBenchmarks = []
    for evalution in MRR.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchmrr)
    benchmarkTimes = []
    benchmarkMeanTimes = []
    benchmarkMedianTimes = []
    for benchmark in allBenchmarks:
        timeRun = (benchmark.finished_at - benchmark.started_at)
        benchmarkTimes.append(timeRun.total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug(
        "MRR Benchmark -> Mean (minutes): "
        + str(benchmarkMeanTimes[-1])
    )
    logger.debug(
        "MRR Benchmark -> Median (minutes): "
        + str(benchmarkMedianTimes[-1])
    )
    logger.debug(
        "MRR Benchmark -> Run Number: "
        + str(len(benchmarkTimes))
    )
    directory = str(
        'files/apps/evaluators/MRR/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'MRR - Mean Reciprocal Rank@'
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
    logger.info("[Finish Bench MRR (Graph Line)]")


def bench_gScatter(songSetLimit, at=5):
    logger.info("[Start Bench MRR (Graph Scatter)]")
    allBenchmarks = []
    for evalution in MRR.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchmrr)
    benchmarkTimes = []
    benchmarkMeanTimes = []
    benchmarkMedianTimes = []
    for benchmark in allBenchmarks:
        timeRun = (benchmark.finished_at - benchmark.started_at)
        benchmarkTimes.append(timeRun.total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug(
        "MRR Benchmark -> Mean (minutes): "
        + str(benchmarkMeanTimes[-1])
    )
    logger.debug(
        "MRR Benchmark -> Median (minutes): "
        + str(benchmarkMedianTimes[-1])
    )
    logger.debug(
        "MRR Benchmark -> Run Number: "
        + str(len(benchmarkTimes))
    )
    directory = str(
        'files/apps/evaluators/MRR/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'MRR - Mean Reciprocal Rank@'
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
    plt.savefig(str(directory) + 'value_gScatter.png')
    plt.close()
    logger.info("[Finish Bench MRR (Graph Scatter)]")


def bench_gBoxPlot(songSetLimit, at=5):
    logger.info("[Start Bench MRR (Graph BoxPlot)]")
    allBenchmarks = []
    for evalution in MRR.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchmrr)
    benchmarkTimes = [
        ((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        for benchmark in allBenchmarks
    ]
    logger.debug(
        "MRR Benchmark -> Run Number: "
        + str(len(benchmarkTimes))
    )
    directory = str(
        'files/apps/evaluators/MRR/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'MRR - Mean Reciprocal Rank@'
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
    logger.info("[Finish Bench MRR (Graph BoxPlot)]")


def bench_gBar(songSetLimit, at=5):
    logger.info("[Start Bench MRR (Graph Bar)]")
    allBenchmarks = []
    for evalution in MRR.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchmrr)
    benchmarkTimes = [
        float("{0:.3f}".format(
            (
                benchmark.finished_at - benchmark.started_at
            ).total_seconds() / 60.0)
        )
        for benchmark in allBenchmarks
    ]
    benchmarkCountList = Counter(benchmarkTimes)
    mode = benchmarkCountList.most_common(1)[0][0]
    logger.debug('MRR Benchmark -> Mode: ' + str(mode))
    directory = str(
        'files/apps/evaluators/MRR/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'MRR - Mean Reciprocal Rank@'
        + str(at)
        + '\nBenchmark - set '
        + str(songSetLimit)
    )
    plt.ylabel('Tempo execução (minutos)')
    plt.xlabel('Quantidade')
    plt.bar(
        benchmarkCountList.values(),
        benchmarkCountList.keys(),
        label='Moda: '
        + str(float("{0:.3f}".format(mode)))
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'value_gBar.png'
    )
    plt.close()
    logger.info("[Finish Bench MRR (Graph Bar)]")


# ###################################################################### #


def all_bench_gLine(at=5, size_list=SET_SIZE_LIST):
    logger.info("[Start Bench MRR (Graph Line)]")
    allBenchmarks = {}
    for evalution in MRR.objects.filter(at=at):
        if evalution.life.setSize not in allBenchmarks:
            allBenchmarks.setdefault(evalution.life.setSize, [])
        else:
            allBenchmarks[evalution.life.setSize].append(
                (
                    evalution.benchmrr.finished_at - evalution.benchmrr.started_at
                ).total_seconds() / 60.0
            )
    directory = str(
        'files/apps/evaluators/MRR/graphs/all/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'MRR - Mean Reciprocal Rank@'
        + str(at)
        + ' Benchmark'
        + '\n |u| - '
        + str(User.objects.count())
    )
    plt.xlabel('ID da execução')
    plt.ylabel('Tempo de execução (minutos)')
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[0]]))],
        [benchmark for benchmark in allBenchmarks[size_list[0]]],
        color='red',
        label=size_list[0]
    )
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[1]]))],
        [benchmark for benchmark in allBenchmarks[size_list[1]]],
        color='green',
        label=size_list[1]
    )
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[2]]))],
        [benchmark for benchmark in allBenchmarks[size_list[2]]],
        color='blue',
        label=size_list[2]
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'all_bench_gLine.png'
    )
    plt.close()
    logger.info("[Finish Bench MRR (Graph Line)]")


def all_bench_gBoxPlot(at=5, size_list=SET_SIZE_LIST):
    logger.info("[Start Bench MRR (Graph BoxPlot)]")
    allBenchmarks = {}
    for evalution in MRR.objects.filter(at=at):
        if evalution.life.setSize not in allBenchmarks:
            allBenchmarks.setdefault(evalution.life.setSize, [])
        else:
            allBenchmarks[evalution.life.setSize].append(
                (
                    evalution.benchmrr.finished_at - evalution.benchmrr.started_at
                ).total_seconds() / 60.0
            )
    directory = str(
        'files/apps/evaluators/MRR/graphs/all/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'MRR - Mean Reciprocal Rank@'
        + str(at)
        + ' Benchmark'
        + '\n |u| - '
        + str(User.objects.count())
    )
    plt.ylabel('Tempo de execução (minutos)')
    plt.boxplot(
        [
            [benchmark for benchmark in allBenchmarks[size_list[0]]],
            [benchmark for benchmark in allBenchmarks[size_list[1]]],
            [benchmark for benchmark in allBenchmarks[size_list[2]]]
        ],
        labels=[size_list[0], size_list[1], size_list[2]]
    )
    plt.savefig(
        str(directory)
        + 'all_bench_gBoxPlot.png'
    )
    plt.close()
    logger.info("[Finish Bench MRR (Graph BoxPlot)]")
