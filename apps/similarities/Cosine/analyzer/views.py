from .algorithm import (
    similarity_gScatter,
    similarity_gLine
)

from .benchmark import (
    all_bench_gLine,
    all_bench_gBoxPlot
)


def runAlgorithmAnalizers():
    similarity_gScatter()
    similarity_gLine()


def runBenchmarkAnalizers(size_list=[1500, 3000, 4500]):
    all_bench_gLine(size_list=size_list)
    all_bench_gBoxPlot(size_list=size_list)
