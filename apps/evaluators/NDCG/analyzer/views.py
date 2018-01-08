from .algorithm import value_gLine, value_gScatter, value_gBoxPlot, value_gBar
from .benchmark import bench_gBar, bench_gBoxPlot, bench_gLine, bench_gScatter

def runNDCGValueGraph(at=5):
    value_gLine(at=at)
    value_gScatter(at=at)
    value_gBoxPlot(at=at)
    value_gBar(at=at)
def runNDCGBenchmarkGraph():
    bench_gBar()
    bench_gLine()
    bench_gBoxPlot()
    bench_gScatter()
def runAllNDCGAnalizers(at=5):
    runNDCGValueGraph(at=at)
    runNDCGBenchmarkGraph()
