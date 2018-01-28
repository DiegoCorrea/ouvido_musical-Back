from .algorithm import (
    all_similarity_gLine,
    all_similarity_gBoxPlot
)

from .benchmark import (
    all_bench_gLine,
    all_bench_gBoxPlot
)
from apps.CONSTANTS import SET_SIZE


def runAlgorithmAnalizers(size_list):
    all_similarity_gLine(size_list=size_list)
    all_similarity_gBoxPlot(size_list=size_list)


def runBenchmarkAnalizers(size_list):
    all_bench_gLine(size_list=size_list)
    all_bench_gBoxPlot(size_list=size_list)


def runCosineAnalizers(size_list=SET_SIZE):
    runAlgorithmAnalizers(size_list=size_list)
    runBenchmarkAnalizers(size_list=size_list)
