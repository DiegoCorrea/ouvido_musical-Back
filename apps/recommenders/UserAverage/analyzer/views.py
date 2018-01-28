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
    like_gBar(songSetLimit=songSetLimit)
    recommended_gBar(songSetLimit=songSetLimit)
    score_gBar(songSetLimit=songSetLimit)
    similarity_gLine(songSetLimit=songSetLimit)
    similarity_gScatter(songSetLimit=songSetLimit)


def runUserAverageBenchmarkGraph():
    all_bench_gBoxPlot()
    all_bench_gLine()


def runUserAverageAnalizers(songSetLimit):
    runUserAverageValueGraph(songSetLimit=songSetLimit)
    runUserAverageBenchmarkGraph()
