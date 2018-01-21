from .MAP.algorithm.views import runMAP
from .MRR.algorithm.views import runMRR
from .NDCG.algorithm.views import runNDCG


def runEvaluations(songSetLimit, at=5):
    runMAP(at=at)
    # runAllMAPAnalizers(at=at, songSetLimit=songSetLimit)
    runMRR(at=at)
    # runAllMRRAnalizers(at=at, songSetLimit=songSetLimit)
    runNDCG(at=at)
    # runAllNDCGAnalizers(at=at, songSetLimit=songSetLimit)
