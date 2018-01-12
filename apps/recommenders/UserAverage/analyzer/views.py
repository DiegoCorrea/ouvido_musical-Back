from .algorithm import score_gBar, recommended_gBar, like_gBar, similarity_gScatter, similarity_gLine
from .benchmark import bench_gBar, bench_gBoxPlot, bench_gLine, bench_gScatter

def runUserAverageValueGraph(songSetLimit):
    like_gBar(songSetLimit=songSetLimit)
    recommended_gBar(songSetLimit=songSetLimit)
    score_gBar(songSetLimit=songSetLimit)
    similarity_gLine(songSetLimit=songSetLimit)
    similarity_gScatter(songSetLimit=songSetLimit)
def runUserAverageBenchmarkGraph(songSetLimit):
    bench_gBar(songSetLimit=songSetLimit)
    bench_gLine(songSetLimit=songSetLimit)
    bench_gBoxPlot(songSetLimit=songSetLimit)
    bench_gScatter(songSetLimit=songSetLimit)
def runUserAverageAnalizers(songSetLimit):
    runUserAverageValueGraph(songSetLimit=songSetLimit)
    runUserAverageBenchmarkGraph(songSetLimit=songSetLimit)
