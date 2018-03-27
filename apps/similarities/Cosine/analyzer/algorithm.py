import matplotlib.pyplot as plt
import os
import logging

from apps.CONSTANTS import START_VALIDE_RUN, TOTAL_RUN
from apps.similarities.Cosine.benchmark.models import BenchCosine_SongTitle

logger = logging.getLogger(__name__)


def all_similarity_gLine(size_list):
    logger.info("[Start Cosine - Similarity (Graph Line)]")
    allBenchmarks = {}
    for runner in size_list:
        allBenchmarks.setdefault(runner, [])
        for benchmark in BenchCosine_SongTitle.objects.filter(
            setSize=runner
        )[START_VALIDE_RUN:TOTAL_RUN]:
            allBenchmarks[runner].append(benchmark.similarity)
    directory = str(
        'files/apps/similarities/Cosine/graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'Cosine Similarity'
    )
    plt.xlabel('Round Id')
    plt.ylabel('Similarity value')
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
        + 'cosine_all_results_gLine.png'
    )
    plt.close()
    logger.info("[Finish Cosine Similarity (Graph Line)]")


def all_similarity_gBoxPlot(size_list):
    logger.info("[Start Cosine Similarity (Graph BoxPlot)]")
    allBenchmarks = {}
    for runner in size_list:
        allBenchmarks.setdefault(runner, [])
        for benchmark in BenchCosine_SongTitle.objects.filter(setSize=runner):
            allBenchmarks[runner].append(benchmark.similarity)
    directory = str(
        'files/apps/similarities/Cosine/graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title(
        'Cosine Similarity'
    )
    plt.ylabel('Similarity value')
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
        + 'cosine_all_results_gBoxPlot.png'
    )
    plt.close()
    logger.info("[Finish Cosine Similarity (Graph BoxPlot)]")
