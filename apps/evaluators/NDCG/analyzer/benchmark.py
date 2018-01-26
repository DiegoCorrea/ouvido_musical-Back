import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.evaluators.NDCG.algorithm.models import NDCG
from django.db import connection
import logging

logger = logging.getLogger(__name__)


def bench_gLine(songSetLimit, at=5):
    logger.info("[Start Bench NDCG (Graph Line)]")
    allBenchmarks = []
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchndcg)
    benchmarkTimes = []
    benchmarkMeanTimes = []
    benchmarkMedianTimes = []
    for benchmark in allBenchmarks:
        timeRun = (benchmark.finished_at - benchmark.started_at)
        benchmarkTimes.append(timeRun.total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug(
        "NDCG Benchmark -> Normalize Discounted (minutes): "
        + str(benchmarkMeanTimes[-1])
    )
    logger.debug(
        "NDCG Benchmark -> Median (minutes): "
        + str(benchmarkMedianTimes[-1])
    )
    logger.debug(
        "NDCG Benchmark -> Run Number: "
        + str(len(benchmarkTimes))
    )
    directory = str(
        'files/apps/evaluators/NDCG/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'NDCG - Normalize Discounted Cumulative Gain@'
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
    logger.info("[Finish Bench NDCG (Graph Line)]")


def bench_gScatter(songSetLimit, at=5):
    logger.info("[Start Bench NDCG (Graph Scatter)]")
    allBenchmarks = []
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchndcg)
    benchmarkTimes = []
    benchmarkMeanTimes = []
    benchmarkMedianTimes = []
    for benchmark in allBenchmarks:
        benchmarkTimes.append(
            (benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0
        )
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug(
        "NDCG Benchmark -> Normalize Discounted (minutes): "
        + str(benchmarkMeanTimes[-1])
    )
    logger.debug(
        "NDCG Benchmark -> Median (minutes): "
        + str(benchmarkMedianTimes[-1])
    )
    logger.debug(
        "NDCG Benchmark -> Run Number: "
        + str(len(benchmarkTimes))
    )
    directory = str(
        'files/apps/evaluators/NDCG/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'NDCG - Normalize Discounted Cumulative Gain@'
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
    logger.info("[Finish Bench NDCG (Graph Scatter)]")


def bench_gBoxPlot(songSetLimit, at=5):
    logger.info("[Start Bench NDCG (Graph BoxPlot)]")
    allBenchmarks = []
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchndcg)
    benchmarkTimes = [
        ((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        for benchmark in allBenchmarks
    ]
    logger.debug(
        "NDCG Benchmark -> Run Number: "
        + str(len(benchmarkTimes))
    )
    directory = str(
        'files/apps/evaluators/NDCG/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'NDCG - Normalize Discounted Cumulative Gain@'
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
    logger.info("[Finish Bench NDCG (Graph BoxPlot)]")


def bench_gBar(songSetLimit, at=5):
    logger.info("[Start Bench NDCG (Graph Bar)]")
    allBenchmarks = []
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize == songSetLimit:
            allBenchmarks.append(evalution.benchndcg)
    benchmarkTimes = [
        float("{0:.3f}".format(
            (benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        )
        for benchmark in allBenchmarks
    ]
    benchmarkCountList = Counter(benchmarkTimes)
    mode = benchmarkCountList.most_common(1)[0][0]
    logger.debug(
        'NDCG Benchmark -> Mode: '
        + str(mode)
    )
    directory = str(
        'files/apps/evaluators/NDCG/graphs/'
        + str(songSetLimit)
        + '/benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'NDCG - Normalize Discounted Cumulative Gain@'
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
    logger.info("[Finish Bench NDCG (Graph Bar)]")

# ###################################################################### #


def all_bench_gLine(at=5):
    logger.info("[Start Bench NDCG (Graph Line)]")
    allBenchmarks = {}
    for evalution in NDCG.objects.filter(at=at):
        if evalution.life.setSize not in allBenchmarks:
            allBenchmarks.setdefault(evalution.life.setSize, [])
        else:
            allBenchmarks[evalution.life.setSize].append(
                (
                    evalution.benchndcg.finished_at - evalution.benchndcg.started_at
                ).total_seconds() / 60.0
            )
    directory = str(
        'files/apps/evaluators/NDCG/graphs/all/'
        + 'benchmark/'
        + str(at) + '/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'NDCG - Mean Reciprocal Rank@'
        + str(at)
        + '\nBenchmark'
    )
    plt.xlabel('ID da execução')
    plt.ylabel('Tempo de execução (minutos)')
    plt.plot(
        [i for i in range(len(allBenchmarks[1000]))],
        [benchmark for benchmark in allBenchmarks[1000]],
        color='red',
        label='1000'
    )
    plt.plot(
        [i for i in range(len(allBenchmarks[2000]))],
        [benchmark for benchmark in allBenchmarks[2000]],
        color='green',
        label='2000'
    )
    plt.plot(
        [i for i in range(len(allBenchmarks[3000]))],
        [benchmark for benchmark in allBenchmarks[3000]],
        color='blue',
        label='3000'
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'all_value_gLine.png'
    )
    plt.close()
    logger.info("[Finish Bench NDCG (Graph Line)]")
