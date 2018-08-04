import matplotlib.pyplot as plt
import logging
import os

from apps.metadata.CONSTANTS import START_VALIDE_RUN, TOTAL_RUN, GRAPH_SET_COLORS_LIST
from apps.kemures.similarities.Cosine.benchmark import BenchCosine_SongTitle

logger = logging.getLogger(__name__)


def all_time_gLine(size_list):
    logger.info("[Start Bench Cosine (Graph Line)]")
    allBenchmarks = {}
    for runner in size_list:
        allBenchmarks.setdefault(runner, [])
        for benchmark in BenchCosine_SongTitle.objects.filter(
            setSize=runner
        )[START_VALIDE_RUN:TOTAL_RUN]:
            allBenchmarks[runner].append(
                (
                    benchmark.finished_at - benchmark.started_at
                ).total_seconds()
            )
    directory = str(
        'files/apps/similarities/Cosine/graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    # plt.title(
    #     'Cosine Similarity'
    #     + '\nTime Latency'
    # )
    plt.xlabel('Round Id')
    plt.ylabel('Time Latency (seconds)')
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[0]]))],
        [benchmark for benchmark in allBenchmarks[size_list[0]]],
        color=GRAPH_SET_COLORS_LIST[0],
        label=size_list[0]
    )
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[1]]))],
        [benchmark for benchmark in allBenchmarks[size_list[1]]],
        color=GRAPH_SET_COLORS_LIST[1],
        label=size_list[1]
    )
    plt.plot(
        [i+1 for i in range(len(allBenchmarks[size_list[2]]))],
        [benchmark for benchmark in allBenchmarks[size_list[2]]],
        color=GRAPH_SET_COLORS_LIST[2],
        label=size_list[2]
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'cosine_all_time_gLine.png'
    )
    plt.close()
    logger.info("[Finish Bench Csine (Graph Line)]")


def all_time_gBoxPlot(size_list):
    logger.info("[Start Bench Cosine (Graph BoxPlot)]")
    allBenchmarks = {}
    for runner in size_list:
        allBenchmarks.setdefault(runner, [])
        for benchmark in BenchCosine_SongTitle.objects.filter(
            setSize=runner
        )[START_VALIDE_RUN:TOTAL_RUN]:
            allBenchmarks[runner].append(
                (
                    benchmark.finished_at - benchmark.started_at
                ).total_seconds()
            )
    directory = str(
        'files/apps/similarities/Cosine/graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    # plt.title(
    #     'Cosine Similarity'
    #     + '\nTime Latency'
    # )
    plt.ylabel('Round Time (seconds)')
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
        + 'cosine_all_time_gBoxPlot.png'
    )
    plt.close()
    logger.info("[Finish Bench Cosine (Graph BoxPlot)]")
