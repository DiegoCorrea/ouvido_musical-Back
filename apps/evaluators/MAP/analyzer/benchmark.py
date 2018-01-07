import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.evaluators.MAP.benchmark.models import BenchMAP
from django.db import connection

directory = str('./apps/evaluators/MAP/analyzer/graphs/' + str(connection.settings_dict['NAME'] + '/benchmark/'))
if not os.path.exists(directory):
    os.makedirs(directory)

def bench_gLine():
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [divmod((benchmark.finished_at - benchmark.started_at).total_seconds(), 60) for benchmark in allBenchmarks]
    benchmarkTotalTime = [(benchmark.finished_at - benchmark.started_at).total_seconds() for benchmark in allBenchmarks]
    benchmarkMean = np.mean(benchmarkTotalTime)
    benchmarkMedian = np.median(benchmarkTotalTime)
    plt.figure()
    plt.grid(True)
    plt.title('MAP Benchmark')
    plt.xlabel('ID do MAP')
    plt.ylabel('Tempo de execução')
    plt.text(-0.1, 1, r'Media: ' + str(benchmarkMean))
    plt.text(-0.1, .8, r'Mediana: ' + str(benchmarkMedian))
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark[1] for benchmark in benchmarkTimes])
    plt.savefig(str(directory) + 'value_gLine' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')

def bench_gScatter(at=5):
    allBenchmarks = MAP.objects.filter(limit=at)
    benchmarkTimes = [benchmark.value for benchmark in allBenchmarks]
    evaluationMean = np.mean(benchmarkTimes)
    evaluationMedian = np.median(benchmarkTimes)
    plt.figure()
    plt.grid(True)
    plt.title('MAP - Mean Averange Precision@' + str(at))
    plt.ylabel('Valor MAP')
    plt.xlabel('Valor MAP')
    plt.text(-0.1, 1, r'Media: ' + str(float("{0:.2f}".format(evaluationMean))))
    plt.text(-0.1, .8, r'Mediana: ' + str(float("{0:.2f}".format(evaluationMedian))))
    plt.scatter(benchmarkTimes, benchmarkTimes)
    plt.axis([-0.2, 1.2, -0.2, 1.2])
    plt.savefig(str(directory) + 'value_gScatter' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')

def bench_gBoxPlot(at=5):
    allBenchmarks = MAP.objects.filter(limit=at)
    benchmarkTimes = [benchmark.value for benchmark in allBenchmarks]
    plt.figure()
    plt.title('MAP - Mean Averange Precision@' + str(at))
    plt.boxplot(benchmarkTimes)
    plt.savefig(str(directory) + 'value_gBoxPlot' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')

def bench_gBar(at=5):
    allBenchmarks = MAP.objects.filter(limit=at)
    benchmarkTimes = [float("{0:.1f}".format(benchmark.value)) for benchmark in allBenchmarks]
    evalutionCountList = Counter(benchmarkTimes)
    plt.figure()
    plt.title('MAP - Mean Averange Precision@' + str(at))
    plt.ylabel('Intervalor de valores')
    plt.xlabel('Quantidade')
    plt.bar(evalutionCountList.values(),evalutionCountList.keys())
    plt.savefig(str(directory) + 'value_gBar' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')
