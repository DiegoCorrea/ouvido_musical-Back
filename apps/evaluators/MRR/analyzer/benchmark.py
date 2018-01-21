import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.evaluators.MRR.benchmark.models import BenchMRR
from django.db import connection
import logging

logger = logging.getLogger(__name__)


def bench_gLine(at, songSetLimit):
    logger.info("[Start Bench MRR (Graph Line)]")
    allBenchmarks = BenchMRR.objects.all().filter(
        id.life.setSize=songSetLimit
    ).filter(id.at=at)
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
        './files/apps/evaluators/MRR/graphs/'
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
        [benchmark.id for benchmark in allBenchmarks],
        [benchmark for benchmark in benchmarkTimes],
        color='red',
        label='Tempo'
    )
    plt.plot(
        [benchmark.id for benchmark in allBenchmarks],
        [benchmark for benchmark in benchmarkMeanTimes],
        color='green',
        label='Media'
    )
    plt.plot(
        [benchmark.id for benchmark in allBenchmarks],
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


def bench_gScatter(at, songSetLimit):
    logger.info("[Start Bench MRR (Graph Scatter)]")
    allBenchmarks = BenchMRR.objects.all().filter(
        id.life.setSize=songSetLimit
    ).filter(id.at=at)
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
        './files/apps/evaluators/MRR/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    directory = str(
        './files/apps/evaluators/MRR/graphs/'
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


def bench_gBoxPlot(at, songSetLimit):
    logger.info("[Start Bench MRR (Graph BoxPlot)]")
    allBenchmarks = BenchMRR.objects.all().filter(
        id.life.setSize=songSetLimit
    ).filter(id.at=at)
    benchmarkTimes = [
        ((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        for benchmark in allBenchmarks
    ]
    logger.debug(
        "MRR Benchmark -> Run Number: "
        + str(len(benchmarkTimes))
    )
    directory = str(
        './files/apps/evaluators/MRR/graphs/'
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


def bench_gBar(at, songSetLimit):
    logger.info("[Start Bench MRR (Graph Bar)]")
    allBenchmarks = BenchMRR.objects.all().filter(
        id.life.setSize=songSetLimit
    ).filter(id.at=at)
    benchmarkTimes = [
        float("{0:.3f}".format((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0))
        for benchmark in allBenchmarks
    ]
    benchmarkCountList = Counter(benchmarkTimes)
    mode = benchmarkCountList.most_common(1)[0][0]
    logger.debug('MRR Benchmark -> Mode: ' + str(mode))
    directory = str(
        './files/apps/evaluators/MRR/graphs/'
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
