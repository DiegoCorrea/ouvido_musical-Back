from .algorithm import value_gLine, value_gScatter, value_gBoxPlot, value_gBar
from .benchmark import bench_gBar, bench_gBoxPlot, bench_gLine, bench_gScatter

def runMRRValueGraph(at=5):
    value_gLine(at=5)
    value_gScatter(at=at)
    value_gBoxPlot(at=at)
    value_gBar(at=at)
def runMRRBenchmarkGraph():
    bench_gBar()
    bench_gLine()
    bench_gBoxPlot()
    bench_gScatter()
def runAllMRRAnalizers(at=5):
    runMRRValueGraph(at=at)
    runMRRBenchmarkGraph()
