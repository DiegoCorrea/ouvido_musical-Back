from .MAP.algorithm.views import runMAP
from .MRR.algorithm.views import runMRR
from .NDCG.algorithm.views import runNDCG
from .MAP.analyzer.views import runAllMAPAnalizers
from .MRR.analyzer.views import runAllMRRAnalizers
from .NDCG.analyzer.views import runAllNDCGAnalizers


def runEvaluations(songSetLimit, at=5):
    runMAP(at=at)
    # runAllMAPAnalizers(at=at, songSetLimit=songSetLimit)
    runMRR(at=at)
    # runAllMRRAnalizers(at=at, songSetLimit=songSetLimit)
    runNDCG(at=at)
    # runAllNDCGAnalizers(at=at, songSetLimit=songSetLimit)


def runAnalizerEvaluations(songSetLimit, at=5):
    runAllMAPAnalizers(at=at, songSetLimit=songSetLimit)
    runAllMRRAnalizers(at=at, songSetLimit=songSetLimit)
    runAllNDCGAnalizers(at=at, songSetLimit=songSetLimit)
