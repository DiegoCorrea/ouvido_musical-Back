import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.evaluators.MAP.algorithm.models import MAP
import logging

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
        './files/apps/evaluators/MAP/graphs/'
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
        './files/apps/evaluators/MAP/graphs/'
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
        './files/apps/evaluators/MAP/graphs/'
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
            (benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        )
        for benchmark in allBenchmarks
    ]
    benchmarkCountList = Counter(benchmarkTimes)
    mode = benchmarkCountList.most_common(1)[0][0]
    logger.debug('MAP Benchmark -> Mode: ' + str(mode))
    directory = str(
        './files/apps/evaluators/MAP/graphs/'
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
