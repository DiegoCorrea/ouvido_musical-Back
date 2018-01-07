from .algorithm import value_gLine, value_gScatter, value_gBoxPlot, value_gBar
from .benchmark import bench_gBar, bench_gBoxPlot, bench_gLine, bench_gScatter

def runMAPValueGraph():
    value_gLine()
    value_gScatter()
    value_gBoxPlot()
    value_gBar()
def runMAPBenchmarkGraph():
    bench_gBar()
    bench_gLine()
    bench_gBoxPlot()
    bench_gScatter()
def runAllMAPAnalizers():
    runMAPValueGraph()
    runMAPBenchmarkGraph()
