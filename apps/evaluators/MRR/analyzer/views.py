from .algorithm import (
    value_gLine,
    value_gScatter,
    value_gBoxPlot,
    value_gBar,
    all_value_gBoxPlot,
    all_value_gLine
)
from .benchmark import (
    bench_gBar,
    bench_gBoxPlot,
    bench_gLine,
    bench_gScatter,
    all_bench_gLine,
    all_bench_gBoxPlot
)


def runMRRValueGraph(songSetLimit, at=5):
    value_gLine(at=at, songSetLimit=songSetLimit)
    value_gScatter(at=at, songSetLimit=songSetLimit)
    value_gBoxPlot(at=at, songSetLimit=songSetLimit)
    value_gBar(at=at, songSetLimit=songSetLimit)
    all_value_gLine(at=at)
    all_value_gBoxPlot(at=at)


def runMRRBenchmarkGraph(songSetLimit, at=5):
    bench_gBar(at=at, songSetLimit=songSetLimit)
    bench_gLine(at=at, songSetLimit=songSetLimit)
    bench_gBoxPlot(at=at, songSetLimit=songSetLimit)
    bench_gScatter(at=at, songSetLimit=songSetLimit)
    all_bench_gLine(at=at)
    all_bench_gBoxPlot(at=at)


def runAllMRRAnalizers(songSetLimit, at=5):
    runMRRValueGraph(at=at, songSetLimit=songSetLimit)
    runMRRBenchmarkGraph(at=at, songSetLimit=songSetLimit)
