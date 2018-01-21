import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.similarities.Cosine.benchmark.models import BenchCosine_SongTitle
from apps.similarities.Cosine.algorithm.models import CosineSimilarity_SongTitle
import logging

logger = logging.getLogger(__name__)


def bench_gLine(songSetLimit=Song.objects.count()):
    logger.info("[Start Bench Cosine (Graph Line)]")
    life_list = UserAverage_Life.objects.filter(setSize=songSetLimit)
    allBenchmarks = BenchCosine_SongTitle.objects.filter(life__in=[run.id for run in life_list])
    benchmarkTimes = []
    benchmarkMeanTimes = []
    benchmarkMedianTimes = []
    for benchmark in allBenchmarks:
        benchmarkTimes.append((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug("Cosine Benchmark -> Mean (minutes): " + str(benchmarkMeanTimes[-1]))
    logger.debug("Cosine Benchmark -> Median (minutes): " + str(benchmarkMedianTimes[-1]))
    logger.debug("Cosine Benchmark -> Run Number: " + str(len(benchmarkTimes)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(songSetLimit) + '/benchmark/' + str(life_list.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('Cosine - Set'+str(songSetLimit)+'\nBenchmark')
    plt.xlabel('ID da execução')
    plt.ylabel('Tempo de execução (minutos)')
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark for benchmark in benchmarkTimes],color='red',label='Tempo')
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark for benchmark in benchmarkMeanTimes],color='green',label='Media')
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark for benchmark in benchmarkMedianTimes],color='blue',label='Mediana')
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gLine.png')
    plt.close()
    logger.info("[Finish Bench Cosine (Graph Line)]")


def bench_gScatter(songSetLimit, allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start Bench Cosine (Graph Scatter)]")
    life_list = UserAverage_Life.objects.filter(setSize=songSetLimit)
    allBenchmarks = BenchCosine_SongTitle.objects.filter(life__in=[ run.id for run in life_list])
    benchmarkTimes = []
    benchmarkMeanTimes = []
    benchmarkMedianTimes = []
    for benchmark in allBenchmarks:
        benchmarkTimes.append((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)
        benchmarkMeanTimes.append(np.mean(benchmarkTimes))
        benchmarkMedianTimes.append(np.median(benchmarkTimes))
    logger.debug("Cosine Benchmark -> Mean (minutes): " + str(benchmarkMeanTimes[-1]))
    logger.debug("Cosine Benchmark -> Median (minutes): " + str(benchmarkMedianTimes[-1]))
    logger.debug("Cosine Benchmark -> Run Number: " + str(len(benchmarkTimes)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(songSetLimit) + '/benchmark/' + str(life_list.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('Cosine - Set'+str(songSetLimit)+'\nBenchmark')
    plt.ylabel('Tempo de execução (minutos)')
    plt.xlabel('Tempo de execução (minutos)')
    plt.scatter(benchmarkTimes, benchmarkTimes, label='Media: ' + str(float("{0:.4f}".format(benchmarkMeanTimes[-1]))))
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'value_gScatter.png')
    plt.close()
    logger.info("[Finish Bench Cosine (Graph Scatter)]")


def bench_gBoxPlot(songSetLimit, allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start Bench Cosine (Graph BoxPlot)]")
    life_list = UserAverage_Life.objects.filter(setSize=songSetLimit)
    allBenchmarks = BenchCosine_SongTitle.objects.filter(life__in=[ run.id for run in life_list])
    benchmarkTimes = [((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0) for benchmark in allBenchmarks]
    logger.debug("Cosine Benchmark -> Run Number: " + str(len(benchmarkTimes)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(songSetLimit) + '/benchmark/' + str(life_list.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('Cosine - Set'+str(songSetLimit)+'\nBenchmark')
    plt.boxplot(benchmarkTimes, labels='T')
    plt.savefig(str(directory) + 'value_gBoxPlot.png')
    plt.close()
    logger.info("[Finish Bench Cosine (Graph BoxPlot)]")


def bench_gBar(songSetLimit, allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start Bench Cosine (Graph Bar)]")
    life_list = UserAverage_Life.objects.filter(setSize=songSetLimit)
    allBenchmarks = BenchCosine_SongTitle.objects.filter(life__in=[ run.id for run in life_list])
    benchmarkTimes = [float("{0:.2f}".format((benchmark.finished_at - benchmark.started_at).total_seconds() / 60.0)) for benchmark in allBenchmarks]
    benchmarkCountList = Counter(benchmarkTimes)
    common = benchmarkCountList
    mode = common.most_common(1)[0][0]
    logger.debug('Cosine Benchmark -> Mode: ' + str(mode))
    logger.debug('Cosine Benchmark -> List: ' + str(benchmarkCountList))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(songSetLimit) + '/benchmark/' + str(life_list.last().id) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('Cosine - Set'+str(songSetLimit)+'\nBenchmark')
    plt.ylabel('Tempo execução (minutos)')
    plt.xlabel('Quantidade')
    plt.bar(benchmarkCountList.values(),benchmarkCountList.keys(), label='Moda: ' + str(float("{0:.2f}".format(mode))))
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'value_gBar.png')
    plt.close()
    logger.info("[Finish Bench Cosine (Graph Bar)]")
