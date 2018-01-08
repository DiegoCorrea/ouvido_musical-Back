from .algorithm import score_gBar, recommended_gBar, like_gBar, similarity_gScatter, similarity_gBar
from .benchmark import bench_gBar, bench_gBoxPlot, bench_gLine, bench_gScatter

def runUserAverageValueGraph():
    #like_gBar()
    #recommended_gBar()
    #score_gBar()
    similarity_gBar()
    similarity_gScatter()
def runUserAverageBenchmarkGraph():
    bench_gBar()
    bench_gLine()
    bench_gBoxPlot()
    bench_gScatter()
def runAllUserAverageAnalizers():
    runUserAverageValueGraph()
    runUserAverageBenchmarkGraph()
