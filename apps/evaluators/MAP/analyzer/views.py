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
    all_bench_gBoxPlot,
    all_bench_gLine
)


def runMAPValueGraphs(songSetLimit, at):
    value_gLine(at=at, songSetLimit=songSetLimit)
    value_gScatter(at=at, songSetLimit=songSetLimit)
    value_gBoxPlot(at=at, songSetLimit=songSetLimit)
    value_gBar(at=at, songSetLimit=songSetLimit)
    all_value_gBoxPlot(at=at)
    all_value_gLine(at=at)


def runMAPBenchmarkGraph(songSetLimit, at):
    bench_gBar(at=at, songSetLimit=songSetLimit)
    bench_gLine(at=at, songSetLimit=songSetLimit)
    bench_gBoxPlot(at=at, songSetLimit=songSetLimit)
    bench_gScatter(at=at, songSetLimit=songSetLimit)
    all_bench_gBoxPlot(at=at)
    all_bench_gLine(at=at)


def runAllMAPAnalizers(songSetLimit, at):
    runMAPValueGraphs(at=at, songSetLimit=songSetLimit)
    runMAPBenchmarkGraph(at=at, songSetLimit=songSetLimit)
