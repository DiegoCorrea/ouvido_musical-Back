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


def runNDCGValueGraph(at=5,songSetLimit):
    value_gLine(at=at, songSetLimit=songSetLimit)
    value_gScatter(at=at, songSetLimit=songSetLimit)
    value_gBoxPlot(at=at, songSetLimit=songSetLimit)
    value_gBar(at=at, songSetLimit=songSetLimit)


def runNDCGBenchmarkGraph(at=5,songSetLimit):
    bench_gBar(at=at, songSetLimit=songSetLimit)
    bench_gLine(at=at, songSetLimit=songSetLimit)
    bench_gBoxPlot(at=at, songSetLimit=songSetLimit)
    bench_gScatter(at=at, songSetLimit=songSetLimit)


def runAllNDCGAnalizers(at=5,songSetLimit):
    runNDCGValueGraph(at=at, songSetLimit=songSetLimit)
    runNDCGBenchmarkGraph(at=at, songSetLimit=songSetLimit)
