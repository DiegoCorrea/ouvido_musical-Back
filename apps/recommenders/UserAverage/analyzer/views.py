from .algorithm import (
    all_similarity_gLine,
    all_similarity_gBoxPlot
)
from .benchmark import (
    all_time_gBoxPlot,
    all_time_gLine
)


def runUserAverageValueGraph():
    all_similarity_gLine()
    all_similarity_gBoxPlot()


def runUserAverageBenchmarkGraph():
    all_time_gBoxPlot()
    all_time_gLine()


def runUserAverageAnalizers():
    runUserAverageValueGraph()
    runUserAverageBenchmarkGraph()
