from .algorithm import (
    value_gLine,
    value_gScatter,
    value_gBoxPlot,
    value_gBar
)
from .benchmark import (
    bench_gBar,
    bench_gBoxPlot,
    bench_gLine,
    bench_gScatter
)


def runMRRValueGraph(songSetLimit, at=5):
    value_gLine(at=at, setSongLimit=setSongLimit)
    value_gScatter(at=at, setSongLimit=setSongLimit)
    value_gBoxPlot(at=at, setSongLimit=setSongLimit)
    value_gBar(at=at, setSongLimit=setSongLimit)


def runMRRBenchmarkGraph(songSetLimit, at=5):
    bench_gBar(at=at, setSongLimit=setSongLimit)
    bench_gLine(at=at, setSongLimit=setSongLimit)
    bench_gBoxPlot(at=at, setSongLimit=setSongLimit)
    bench_gScatter(at=at, setSongLimit=setSongLimit)


def runAllMRRAnalizers(songSetLimit, at=5):
    runMRRValueGraph(at=at, setSongLimit=setSongLimit)
    runMRRBenchmarkGraph(at=at, setSongLimit=setSongLimit)
