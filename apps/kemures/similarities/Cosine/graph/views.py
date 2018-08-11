from .algorithm import (
    all_similarity_gLine,
    all_similarity_gBoxPlot
)

from .benchmark import (
    all_time_gLine,
    all_time_gBoxPlot
)
from apps.kemures.kernel_var import SET_SIZE_LIST


def runAlgorithmAnalizers(size_list):
    all_similarity_gLine(size_list=size_list)
    all_similarity_gBoxPlot(size_list=size_list)


def runBenchmarkAnalizers(size_list):
    all_time_gLine(size_list=size_list)
    all_time_gBoxPlot(size_list=size_list)


def cosineGraphics(size_list=SET_SIZE_LIST):
    runAlgorithmAnalizers(size_list=size_list)
    runBenchmarkAnalizers(size_list=size_list)
