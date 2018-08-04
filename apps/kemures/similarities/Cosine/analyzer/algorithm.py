import matplotlib.pyplot as plt
import os
import logging

from apps.metadata.CONSTANTS import (
    SET_SIZE_LIST,
    INTERVAL,
    GRAPH_SET_COLORS_LIST
)
from apps.kemures.similarities.Cosine.benchmark import BenchCosine_SongTitle

logger = logging.getLogger(__name__)


def all_similarity_gLine(size_list=SET_SIZE_LIST):
    logger.info("[Start Cosine - Similarity (Graph Line)]")
    allBenchmarks = {}
    for runner in size_list:
        allBenchmarks.setdefault(runner, [])
        for benchmark in BenchCosine_SongTitle.objects.filter(
            setSize=runner
        ):
            allBenchmarks[runner].append(benchmark.similarity)
    directory = str(
        'files/apps/similarities/Cosine/graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    # plt.title(
    #     'Cosine Similarity'
    # )
    plt.xlabel('Round Id')
    plt.ylabel('Similarity value')
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[0]][-INTERVAL:]))],
        [benchmark for benchmark in allBenchmarks[size_list[0]][-INTERVAL:]],
        color=GRAPH_SET_COLORS_LIST[0],
        label=size_list[0]
    )
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[1]][-INTERVAL:]))],
        [benchmark for benchmark in allBenchmarks[size_list[1]][-INTERVAL:]],
        color=GRAPH_SET_COLORS_LIST[1],
        label=size_list[1]
    )
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[2]][-INTERVAL:]))],
        [benchmark for benchmark in allBenchmarks[size_list[2]][-INTERVAL:]],
        color=GRAPH_SET_COLORS_LIST[2],
        label=size_list[2]
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'cosine_all_results_gLine.png'
    )
    plt.close()
    logger.info("[Finish Cosine Similarity (Graph Line)]")


def all_similarity_gBoxPlot(size_list=SET_SIZE_LIST):
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
    plt.grid(True)
    # plt.title(
    #     'Cosine Similarity'
    # )
    plt.ylabel('Similarity value')
    plt.boxplot(
        [
            [benchmark for benchmark in allBenchmarks[size_list[0]][-INTERVAL:]],
            [benchmark for benchmark in allBenchmarks[size_list[1]][-INTERVAL:]],
            [benchmark for benchmark in allBenchmarks[size_list[2]][-INTERVAL:]]
        ],
        labels=[size_list[0], size_list[1], size_list[2]]
    )
    plt.savefig(
        str(directory)
        + 'cosine_all_results_gBoxPlot.png'
    )
    plt.close()
    logger.info("[Finish Cosine Similarity (Graph BoxPlot)]")
