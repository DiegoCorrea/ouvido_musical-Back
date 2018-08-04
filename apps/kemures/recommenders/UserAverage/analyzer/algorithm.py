import matplotlib.pyplot as plt
import logging
import os

from apps.kemures.recommenders.UserAverage import (
    UserAverage_Life
)
from apps.kemures.CONSTANTS import (
    SET_SIZE_LIST,
    INTERVAL,
    GRAPH_SET_COLORS_LIST
)

logger = logging.getLogger(__name__)


def all_similarity_gLine(size_list=SET_SIZE_LIST):
    logger.info("[Start User Average - Similarity (Graph Line)]")
    allSimilarities = {}
    for runner in size_list:
        allSimilarities.setdefault(runner, [])
        allSimilarities[runner] = [life.similarity for life in UserAverage_Life.objects.filter(setSize=runner)]
    directory = str(
        'files/apps/recommenders/UserAverage/graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    # plt.title(
    #     'User Average'
    # )
    plt.xlabel('Round Id')
    plt.ylabel('Similarity value')
    plt.plot(
        [i+1 for i in range(len(allSimilarities[size_list[0]][-INTERVAL:]))],
        [benchmark for benchmark in allSimilarities[size_list[0]][-INTERVAL:]],
        color=GRAPH_SET_COLORS_LIST[0],
        label=size_list[0]
    )
    plt.plot(
        [i+1 for i in range(len(allSimilarities[size_list[1]][-INTERVAL:]))],
        [benchmark for benchmark in allSimilarities[size_list[1]][-INTERVAL:]],
        color=GRAPH_SET_COLORS_LIST[1],
        label=size_list[1]
    )
    plt.plot(
        [i+1 for i in range(len(allSimilarities[size_list[2]][-INTERVAL:]))],
        [benchmark for benchmark in allSimilarities[size_list[2]][-INTERVAL:]],
        color=GRAPH_SET_COLORS_LIST[2],
        label=size_list[2]
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'userAverage_all_similarity_gLine.png'
    )
    plt.close()
    logger.info("[Finish UserAverage - Similarity (Graph Line)]")


def all_similarity_gBoxPlot(size_list=SET_SIZE_LIST):
    logger.info("[Start User Average - Similarity (Graph Box)]")
    allSimilarities = {}
    for runner in size_list:
        allSimilarities.setdefault(runner, [])
        allSimilarities[runner] = [life.similarity for life in UserAverage_Life.objects.filter(setSize=runner)]
    directory = str(
        'files/apps/recommenders/UserAverage/graphs/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    # plt.title(
    #     'User Average'
    # )
    plt.ylabel('Similarity value')
    plt.boxplot(
        [
            [evaluation for evaluation in allSimilarities[size_list[0]][-INTERVAL:]],
            [evaluation for evaluation in allSimilarities[size_list[1]][-INTERVAL:]],
            [evaluation for evaluation in allSimilarities[size_list[2]][-INTERVAL:]]
        ],
        labels=[size_list[0], size_list[1], size_list[2]]
    )
    plt.legend(loc='best')
    plt.savefig(
        str(directory)
        + 'userAverage_all_similarity_gBox.png'
    )
    plt.close()
    logger.info("[Finish UserAverage - Similarity (Graph Box)]")
