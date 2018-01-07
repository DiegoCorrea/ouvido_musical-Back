import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.evaluators.NDCG.benchmark.models import BenchNDCG
from django.db import connection
import logging

logger = logging.getLogger(__name__)

def bench_gLine():
    logger.info("[Start Bench NDCG (Graph Line)]")
    allBenchmarks = BenchNDCG.objects.all()
    benchmarkTimes = [ ]
    benchmarkMeanTimes = [ ]
    benchmarkMedianTimes = [ ]
    for benchmark in allBenchmarks:
        benchmarkTimes.append((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug("NDCG Benchmark -> Normalize Discounted (minutes): " + str(benchmarkMeanTimes[-1]))
    logger.debug("NDCG Benchmark -> Median (minutes): " + str(benchmarkMedianTimes[-1]))
    logger.debug("NDCG Benchmark -> Run Number: " + str(len(benchmarkTimes)))
    directory = str('./apps/evaluators/NDCG/analyzer/graphs/' + str(connection.settings_dict['NAME']) + '/benchmark/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('NDCG - Normalize Discounted Cumulative Gain\nBenchmark')
    plt.xlabel('ID da execução')
    plt.ylabel('Tempo de execução (minutos)')
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark for benchmark in benchmarkTimes],color='red',label='Tempo')
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark for benchmark in benchmarkMeanTimes],color='green',label='Media')
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark for benchmark in benchmarkMedianTimes],color='blue',label='Mediana')
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gLine.png')
    plt.close()
    logger.info("[Finish Bench NDCG (Graph Line)]")
def bench_gScatter():
    logger.info("[Start Bench NDCG (Graph Scatter)]")
    allBenchmarks = BenchNDCG.objects.all()
    benchmarkTimes = [ ]
    benchmarkMeanTimes = [ ]
    benchmarkMedianTimes = [ ]
    for benchmark in allBenchmarks:
        benchmarkTimes.append((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug("NDCG Benchmark -> Normalize Discounted (minutes): " + str(benchmarkMeanTimes[-1]))
    logger.debug("NDCG Benchmark -> Median (minutes): " + str(benchmarkMedianTimes[-1]))
    logger.debug("NDCG Benchmark -> Run Number: " + str(len(benchmarkTimes)))
    directory = str('./apps/evaluators/NDCG/analyzer/graphs/' + str(connection.settings_dict['NAME']) + '/benchmark/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('NDCG - Normalize Discounted Cumulative Gain\nBenchmark')
    plt.ylabel('Tempo de execução (minutos)')
    plt.xlabel('Tempo de execução (minutos)')
    plt.scatter(benchmarkTimes, benchmarkTimes, label='Media: ' + str(float("{0:.4f}".format(benchmarkMeanTimes[-1]))))
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'value_gScatter.png')
    plt.close()
    logger.info("[Finish Bench NDCG (Graph Scatter)]")
def bench_gBoxPlot():
    logger.info("[Start Bench NDCG (Graph BoxPlot)]")
    allBenchmarks = BenchNDCG.objects.all()
    benchmarkTimes = [((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0) for benchmark in allBenchmarks]
    logger.debug("NDCG Benchmark -> Run Number: " + str(len(benchmarkTimes)))
    directory = str('./apps/evaluators/NDCG/analyzer/graphs/' + str(connection.settings_dict['NAME']) + '/benchmark/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('NDCG - Normalize Discounted Cumulative Gain\nBenchmark')
    plt.boxplot(benchmarkTimes, labels='T')
    plt.savefig(str(directory) + 'value_gBoxPlot.png')
    plt.close()
    logger.info("[Finish Bench NDCG (Graph BoxPlot)]")
def bench_gBar():
    logger.info("[Start Bench NDCG (Graph Bar)]")
    allBenchmarks = BenchNDCG.objects.all()
    benchmarkTimes = [float("{0:.3f}".format((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)) for benchmark in allBenchmarks]
    benchmarkCountList = Counter(benchmarkTimes)
    mode = benchmarkCountList.most_common(1)[0][0]
    logger.debug('NDCG Benchmark -> Mode: ' + str(mode))
    directory = str('./apps/evaluators/NDCG/analyzer/graphs/' + str(connection.settings_dict['NAME']) + '/benchmark/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('NDCG - Normalize Discounted Cumulative Gain\nBenchmark')
    plt.ylabel('Tempo execução (minutos)')
    plt.xlabel('Quantidade')
    plt.bar(benchmarkCountList.values(),benchmarkCountList.keys(), label='Moda: ' + str(float("{0:.3f}".format(mode))))
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gBar.png')
    plt.close()
    logger.info("[Finish Bench NDCG (Graph Bar)]")
