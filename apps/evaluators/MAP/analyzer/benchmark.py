import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.evaluators.MAP.benchmark.models import BenchMAP
from django.db import connection
import logging

logger = logging.getLogger(__name__)

def bench_gLine():
    logger.info("[Start Bench MAP (Graph Line)]")
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [ ]
    benchmarkMeanTimes = [ ]
    benchmarkMedianTimes = [ ]
    for benchmark in allBenchmarks:
        benchmarkTimes.append((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug("MAP Benchmark -> Mean (minutes): " + str(benchmarkMeanTimes[-1]))
    logger.debug("MAP Benchmark -> Median (minutes): " + str(benchmarkMedianTimes[-1]))
    logger.debug("MAP Benchmark -> Run Number: " + str(len(benchmarkTimes)))
    directory = str('./files/apps/evaluators/MAP/graphs/' + str(connection.settings_dict['NAME']) + '/benchmark/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('MAP - Mean Averange Precision\nBenchmark')
    plt.xlabel('ID da execução')
    plt.ylabel('Tempo de execução (minutos)')
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark for benchmark in benchmarkTimes],color='red',label='Tempo')
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark for benchmark in benchmarkMeanTimes],color='green',label='Media')
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark for benchmark in benchmarkMedianTimes],color='blue',label='Mediana')
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gLine.png')
    plt.close()
    logger.info("[Finish Bench MAP (Graph Line)]")
def bench_gScatter():
    logger.info("[Start Bench MAP (Graph Scatter)]")
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [ ]
    benchmarkMeanTimes = [ ]
    benchmarkMedianTimes = [ ]
    for benchmark in allBenchmarks:
        benchmarkTimes.append((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug("MAP Benchmark -> Mean (minutes): " + str(benchmarkMeanTimes[-1]))
    logger.debug("MAP Benchmark -> Median (minutes): " + str(benchmarkMedianTimes[-1]))
    logger.debug("MAP Benchmark -> Run Number: " + str(len(benchmarkTimes)))
    directory = str('./files/apps/evaluators/MAP/graphs/' + str(connection.settings_dict['NAME']) + '/benchmark/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('MAP - Mean Averange Precision\nBenchmark')
    plt.ylabel('Tempo de execução (minutos)')
    plt.xlabel('Tempo de execução (minutos)')
    plt.scatter(benchmarkTimes, benchmarkTimes, label='Media: ' + str(float("{0:.4f}".format(benchmarkMeanTimes[-1]))))
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'value_gScatter.png')
    plt.close()
    logger.info("[Finish Bench MAP (Graph Scatter)]")
def bench_gBoxPlot():
    logger.info("[Start Bench MAP (Graph BoxPlot)]")
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0) for benchmark in allBenchmarks]
    logger.debug("MAP Benchmark -> Run Number: " + str(len(benchmarkTimes)))
    directory = str('./files/apps/evaluators/MAP/graphs/' + str(connection.settings_dict['NAME']) + '/benchmark/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('MAP - Mean Averange Precision\nBenchmark')
    plt.boxplot(benchmarkTimes, labels='T')
    plt.savefig(str(directory) + 'value_gBoxPlot.png')
    plt.close()
    logger.info("[Finish Bench MAP (Graph BoxPlot)]")
def bench_gBar():
    logger.info("[Start Bench MAP (Graph Bar)]")
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [float("{0:.3f}".format((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)) for benchmark in allBenchmarks]
    benchmarkCountList = Counter(benchmarkTimes)
    mode = benchmarkCountList.most_common(1)[0][0]
    logger.debug('MAP Benchmark -> Mode: ' + str(mode))
    directory = str('./files/apps/evaluators/MAP/graphs/' + str(connection.settings_dict['NAME']) + '/benchmark/' + str(allBenchmarks.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('MAP - Mean Averange Precision\nBenchmark')
    plt.ylabel('Tempo execução (minutos)')
    plt.xlabel('Quantidade')
    plt.bar(benchmarkCountList.values(),benchmarkCountList.keys(), label='Moda: ' + str(float("{0:.3f}".format(mode))))
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gBar.png')
    plt.close()
    logger.info("[Finish Bench MAP (Graph Bar)]")