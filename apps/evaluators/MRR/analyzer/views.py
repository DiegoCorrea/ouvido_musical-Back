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


def runMRRValueGraph(at=5, setSongLimit):
    value_gLine(at=at, setSongLimit=setSongLimit)
    value_gScatter(at=at, setSongLimit=setSongLimit)
    value_gBoxPlot(at=at, setSongLimit=setSongLimit)
    value_gBar(at=at, setSongLimit=setSongLimit)


def runMRRBenchmarkGraph(at=5, setSongLimit):
    bench_gBar(at=at, setSongLimit=setSongLimit)
    bench_gLine(at=at, setSongLimit=setSongLimit)
    bench_gBoxPlot(at=at, setSongLimit=setSongLimit)
    bench_gScatter(at=at, setSongLimit=setSongLimit)


def runAllMRRAnalizers(at=5, setSongLimit):
    runMRRValueGraph(at=at, setSongLimit=setSongLimit)
    runMRRBenchmarkGraph(at=at, setSongLimit=setSongLimit)
