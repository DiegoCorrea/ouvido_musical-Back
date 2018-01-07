from .algorithm import value_gLine, value_gScatter, value_gBoxPlot, value_gBar
from .benchmark import bench_gBar, bench_gBoxPlot, bench_gLine, bench_gScatter

def runNDCGValueGraph():
    value_gLine()
    value_gScatter()
    value_gBoxPlot()
    value_gBar()
def runNDCGBenchmarkGraph():
    bench_gBar()
    bench_gLine()
    bench_gBoxPlot()
    bench_gScatter()
def runAllNDCGAnalizers():
    #runNDCGValueGraph()
    runNDCGBenchmarkGraph()
