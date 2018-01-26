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


def runNDCGValueGraph(songSetLimit, at=5):
    value_gLine(at=at, songSetLimit=songSetLimit)
    value_gScatter(at=at, songSetLimit=songSetLimit)
    value_gBoxPlot(at=at, songSetLimit=songSetLimit)
    value_gBar(at=at, songSetLimit=songSetLimit)
    all_value_gLine(at=at)
    all_value_gBoxPlot(at=at)


def runNDCGBenchmarkGraph(songSetLimit, at=5):
    bench_gBar(at=at, songSetLimit=songSetLimit)
    bench_gLine(at=at, songSetLimit=songSetLimit)
    bench_gBoxPlot(at=at, songSetLimit=songSetLimit)
    bench_gScatter(at=at, songSetLimit=songSetLimit)
    all_bench_gLine(at=at)
    all_bench_gBoxPlot(at=at)


def runAllNDCGAnalizers(songSetLimit, at=5):
    runNDCGValueGraph(at=at, songSetLimit=songSetLimit)
    runNDCGBenchmarkGraph(at=at, songSetLimit=songSetLimit)
