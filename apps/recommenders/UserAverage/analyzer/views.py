from .algorithm import (
    all_similarity_gLine,
    all_similarity_gBoxPlot
)
from .benchmark import (
    all_time_gBoxPlot,
    all_time_gLine
)


def runUserAverageValueGraphics():
    all_similarity_gLine()
    all_similarity_gBoxPlot()


def runUserAverageBenchmarkGraphics():
    all_time_gBoxPlot()
    all_time_gLine()


def userAverageGraphics():
    runUserAverageValueGraphics()
    runUserAverageBenchmarkGraphics()
