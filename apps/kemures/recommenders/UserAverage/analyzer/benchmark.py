import matplotlib.pyplot as plt
import logging
import os

from apps.kemures.recommenders.UserAverage import (
    UserAverage_Life
)

from apps.kemures.kernel_var import (
    SET_SIZE_LIST,
    INTERVAL,
    GRAPH_SET_COLORS_LIST
)

logger = logging.getLogger(__name__)


def all_time_gLine(size_list=SET_SIZE_LIST):
    logger.info("[Start Bench User Average (Graph Line)]")
    allBenchmarks = {}
    for recommenderRunner in UserAverage_Life.objects.filter(
        setSize__in=size_list
    ):
        if recommenderRunner.setSize not in allBenchmarks:
            allBenchmarks.setdefault(recommenderRunner.setSize, [])
        allBenchmarks[recommenderRunner.setSize].append(
            (
                recommenderRunner.benchuseraverage.finished_at - recommenderRunner.benchuseraverage.started_at
            ).total_seconds()
        )
    directory = str(
        'files/apps/recommenders/UserAverage/graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    # plt.title(
    #     'User Average'
    #     + ' Benchmark'
    #     + '\n |u| - '
    #     + str(User.objects.count())
    # )
    plt.xlabel('Round Id')
    plt.ylabel('Time Latency (seconds)')
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
        + 'userAverage_all_time_gLine.png'
    )
    plt.close()
    logger.info("[Finish Bench User Average (Graph Line)]")


def all_time_gBoxPlot(size_list=SET_SIZE_LIST):
    logger.info("[Start Bench User Average (Graph BoxPlot)]")
    allBenchmarks = {}
    for recommenderRunner in UserAverage_Life.objects.filter(
        setSize__in=size_list
    ):
        if recommenderRunner.setSize not in allBenchmarks:
            allBenchmarks.setdefault(recommenderRunner.setSize, [])
        allBenchmarks[recommenderRunner.setSize].append(
            (
                recommenderRunner.benchuseraverage.finished_at - recommenderRunner.benchuseraverage.started_at
            ).total_seconds()
        )
    directory = str(
        'files/apps/recommenders/UserAverage/graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    # plt.title(
    #     'User Average'
    #     + ' Benchmark'
    #     + '\n |u| - '
    #     + str(User.objects.count())
    # )
    plt.ylabel('Time Latency (seconds)')
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
        + 'userAverage_all_time_gBoxPlot.png'
    )
    plt.close()
    logger.info("[Finish Bench User Average (Graph BoxPlot)]")
