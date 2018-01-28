import matplotlib.pyplot as plt
import numpy as np
import logging
import os

from collections import Counter
from apps.data.users.models import User
from apps.recommenders.UserAverage.algorithm.models import (
    UserAverage_Life
)

logger = logging.getLogger(__name__)


def all_bench_gLine(size_list=[1500, 3000, 4500]):
    logger.info("[Start Bench User Average (Graph Line)]")
    allBenchmarks = {}
    for recommenderRunner in UserAverage_Life.objects.filter(
        setSize__in=size_list
    ):
        if recommenderRunner.setSize not in allBenchmarks:
            allBenchmarks.setdefault(recommenderRunner.setSize, [])
        else:
            allBenchmarks[recommenderRunner.setSize].append(
                (
                    recommenderRunner.benchuseraverage.finished_at - recommenderRunner.benchuseraverage.started_at
                ).total_seconds() / 60.0
            )
    directory = str(
        'files/apps/recommenders/UserAverage/graphs/all/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'User Average'
        + ' Benchmark'
        + '\n |u| - '
        + str(User.objects.count())
    )
    plt.xlabel('ID da execução')
    plt.ylabel('Tempo de execução (minutos)')
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
        + 'all_bench_gLine.png'
    )
    plt.close()
    logger.info("[Finish Bench User Average (Graph Line)]")


def all_bench_gBoxPlot(size_list=[1500, 3000, 4500]):
    logger.info("[Start Bench User Average (Graph BoxPlot)]")
    allBenchmarks = {}
    for recommenderRunner in UserAverage_Life.objects.filter(
        setSize__in=size_list
    ):
        if recommenderRunner.setSize not in allBenchmarks:
            allBenchmarks.setdefault(recommenderRunner.setSize, [])
        else:
            allBenchmarks[recommenderRunner.setSize].append(
                (
                    recommenderRunner.benchuseraverage.finished_at - recommenderRunner.benchuseraverage.started_at
                ).total_seconds() / 60.0
            )
    directory = str(
        'files/apps/recommenders/UserAverage/graphs/all/'
    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title(
        'User Average'
        + ' Benchmark'
        + '\n |u| - '
        + str(User.objects.count())
    )
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
        + 'all_bench_gBoxPlot.png'
    )
    plt.close()
    logger.info("[Finish Bench User Average (Graph BoxPlot)]")
