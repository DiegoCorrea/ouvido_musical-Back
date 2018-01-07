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
    plt.ylabel('Tempo de execução /s')
    plt.text(-0.1, 1, r'Media: ' + str(float("{0:.2f}".format(benchmarkMean))))
    plt.text(-0.1, .8, r'Mediana: ' + str(float("{0:.2f}".format(benchmarkMedian))))
    plt.plot([benchmark.id for benchmark in allBenchmarks],[benchmark[1] for benchmark in benchmarkTimes])
    plt.savefig(str(directory) + 'value_gLine' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')

def bench_gScatter(at=5):
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [divmod((benchmark.finished_at - benchmark.started_at).total_seconds(), 60) for benchmark in allBenchmarks]
    benchmarkTotalTime = [(benchmark.finished_at - benchmark.started_at).total_seconds() for benchmark in allBenchmarks]
    benchmarkMean = np.mean(benchmarkTotalTime)
    benchmarkMedian = np.median(benchmarkTotalTime)
    plt.figure()
    plt.grid(True)
    plt.title('MAP Benchmark')
    plt.ylabel('Tempo de execução /s')
    plt.xlabel('Tempo de execução /s')
    plt.text(-0.1, 1, r'Media: ' + str(float("{0:.2f}".format(benchmarkMean))))
    plt.text(-0.1, .8, r'Mediana: ' + str(float("{0:.2f}".format(benchmarkMedian))))
    plt.scatter(benchmarkTotalTime, benchmarkTotalTime)
    plt.savefig(str(directory) + 'value_gScatter' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')

def bench_gBoxPlot(at=5):
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [divmod((benchmark.finished_at - benchmark.started_at).total_seconds(), 60) for benchmark in allBenchmarks]
    benchmarkTotalTime = [(benchmark.finished_at - benchmark.started_at).total_seconds() for benchmark in allBenchmarks]
    plt.figure()
    plt.title('MAP Benchmark')
    plt.boxplot(benchmarkTotalTime)
    plt.savefig(str(directory) + 'value_gBoxPlot' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')

def bench_gBar(at=5):
    allBenchmarks = BenchMAP.objects.all()
    benchmarkTimes = [divmod((benchmark.finished_at - benchmark.started_at).total_seconds(), 60) for benchmark in allBenchmarks]
    benchmarkTotalTime = [float("{0:.1f}".format((benchmark.finished_at - benchmark.started_at).total_seconds())) for benchmark in allBenchmarks]
    benchmarkCountList = Counter(benchmarkTotalTime)
    plt.figure()
    plt.title('MAP Benchmark')
    plt.ylabel('Tempo execução \s')
    plt.xlabel('Quantidade')
    plt.bar(benchmarkCountList.values(),benchmarkCountList.keys())
    plt.savefig(str(directory) + 'value_gBar' + '-[id]-'+ str(allBenchmarks.last().id) + '.png')
