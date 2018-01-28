from .algorithm import (
    score_gBar,
    recommended_gBar,
    like_gBar,
    similarity_gScatter,
    similarity_gLine
)
from .benchmark import (
    all_bench_gBoxPlot,
    all_bench_gLine
)


def runUserAverageValueGraph(songSetLimit):
    pass


def runUserAverageBenchmarkGraph():
    all_bench_gBoxPlot()
    all_bench_gLine()


def runUserAverageAnalizers(songSetLimit):
    runUserAverageValueGraph(songSetLimit=songSetLimit)
    runUserAverageBenchmarkGraph()
