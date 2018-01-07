from .algorithm import value_gLine, value_gScatter, value_gBoxPlot, value_gBar
from .benchmark import bench_gBar, bench_gBoxPlot, bench_gLine, bench_gScatter

def runMRRValueGraph():
    value_gLine()
    value_gScatter()
    value_gBoxPlot()
    value_gBar()
def runMRRBenchmarkGraph():
    bench_gBar()
    bench_gLine()
    bench_gBoxPlot()
    bench_gScatter()
def runAllMRRAnalizers():
    runMRRValueGraph()
    runMRRBenchmarkGraph()
