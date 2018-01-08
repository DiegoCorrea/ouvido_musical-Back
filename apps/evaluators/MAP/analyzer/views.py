from .algorithm import value_gLine, value_gScatter, value_gBoxPlot, value_gBar
from .benchmark import bench_gBar, bench_gBoxPlot, bench_gLine, bench_gScatter

def runMAPValueGraph(at=5):
    value_gLine(at=at)
    value_gScatter(at=at)
    value_gBoxPlot(at=at)
    value_gBar(at=at)
def runMAPBenchmarkGraph():
    bench_gBar()
    bench_gLine()
    bench_gBoxPlot()
    bench_gScatter()
def runAllMAPAnalizers(at=5):
    runMAPValueGraph(at=at)
    runMAPBenchmarkGraph()
