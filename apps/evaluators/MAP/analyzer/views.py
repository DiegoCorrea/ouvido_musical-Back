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


def runMAPValueGraph(at=5,songSetLimit):
    value_gLine(at=at,songSetLimit=songSetLimit)
    value_gScatter(at=at,songSetLimit=songSetLimit)
    value_gBoxPlot(at=at,songSetLimit=songSetLimit)
    value_gBar(at=at,songSetLimit=songSetLimit)


def runMAPBenchmarkGraph(at=5,songSetLimit):
    bench_gBar(at=at,songSetLimit=songSetLimit)
    bench_gLine(at=at,songSetLimit=songSetLimit)
    bench_gBoxPlot(at=at,songSetLimit=songSetLimit)
    bench_gScatter(at=at,songSetLimit=songSetLimit)


def runAllMAPAnalizers(at=5, songSetLimit):
    runMAPValueGraph(at=at,songSetLimit=songSetLimit)
    runMAPBenchmarkGraph(at=at,songSetLimit=songSetLimit)
