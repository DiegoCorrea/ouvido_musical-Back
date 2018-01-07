import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.evaluators.MAP.benchmark.models import BenchMAP
from django.db import connection
import logging

logger = logging.getLogger(__name__)
directory = str('./apps/evaluators/MAP/analyzer/graphs/' + str(connection.settings_dict['NAME'] + '/benchmark/'))
if not os.path.exists(directory):
    os.makedirs(directory)

def bench_gLine():
    logger.info("[Start Bench Graph Line]")
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0) for benchmark in allBenchmarks]
    benchmarkMean = np.mean(benchmarkTimes)
    benchmarkMedian = np.median(benchmarkTimes)
    logger.debug("MAP Benchmark Time Mean: " + str(benchmarkMean))
    logger.debug("MAP Benchmark Time Median: " + str(benchmarkMedian))
    plt.figure()
    plt.grid(True)
    plt.title('MAP Benchmark')
    plt.xlabel('ID do MAP')
    plt.ylabel('Tempo de execução (minutos)')
    plt.text(-0.1, 1, r'Media: ' + str(float("{0:.2f}".format(benchmarkMean))))
    plt.text(-0.1, .8, r'Mediana: ' + str(float("{0:.2f}".format(benchmarkMedian))))
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark for benchmark in benchmarkTimes])
    plt.savefig(str(directory) + 'value_gLine' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')
    logger.info("[Finish Bench Graph Line]")
def bench_gScatter(at=5):
    logger.info("[Start Bench Graph Scatter]")
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0) for benchmark in allBenchmarks]
    benchmarkMean = np.mean(benchmarkTimes)
    benchmarkMedian = np.median(benchmarkTimes)
    logger.debug("MAP Benchmark Time Mean: " + str(benchmarkMean))
    logger.debug("MAP Benchmark Time Median: " + str(benchmarkMedian))
    plt.figure()
    plt.grid(True)
    plt.title('MAP Benchmark')
    plt.ylabel('Tempo de execução (minutos)')
    plt.xlabel('Tempo de execução (minutos)')
    plt.text(-0.1, 1, r'Media: ' + str(float("{0:.2f}".format(benchmarkMean))))
    plt.text(-0.1, .8, r'Mediana: ' + str(float("{0:.2f}".format(benchmarkMedian))))
    plt.scatter(benchmarkTimes, benchmarkTimes)
    plt.savefig(str(directory) + 'value_gScatter' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')
    logger.info("[Finish Bench Graph Scatter]")
def bench_gBoxPlot(at=5):
    logger.info("[Start Bench Graph BoxPlot]")
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0) for benchmark in allBenchmarks]
    plt.figure()
    plt.title('MAP Benchmark')
    plt.boxplot(benchmarkTimes)
    plt.savefig(str(directory) + 'value_gBoxPlot' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')
    logger.info("[Finish Bench Graph BoxPlot]")
def bench_gBar(at=5):
    logger.info("[Start Bench Graph Bar]")
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [float("{0:.1f}".format((benchmark.finished_at - benchmark.started_at).total_seconds())) for benchmark in allBenchmarks]
    benchmarkCountList = Counter(benchmarkTimes)
    plt.figure()
    plt.title('MAP Benchmark')
    plt.ylabel('Tempo execução (minutos)')
    plt.xlabel('Quantidade')
    plt.bar(benchmarkCountList.values(),benchmarkCountList.keys())
    plt.savefig(str(directory) + 'value_gBar' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')
    logger.info("[Finish Bench Graph Bar]")
