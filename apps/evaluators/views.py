from .MAP.algorithm.views import runMAP
from .MRR.algorithm.views import runMRR
from .NDCG.algorithm.views import runNDCG
from .MAP.analyzer.views import runAllMAPAnalizers
from .MRR.analyzer.views import runAllMRRAnalizers
from .NDCG.analyzer.views import runAllNDCGAnalizers


def runEvaluations(songSetLimit, at=5):
    runMAP(at=at)
    runMRR(at=at)
    runNDCG(at=at)


def runAnalizerEvaluations(songSetLimit, at=5):
    runAllMAPAnalizers(at=at, songSetLimit=songSetLimit)
    runAllMRRAnalizers(at=at, songSetLimit=songSetLimit)
    runAllNDCGAnalizers(at=at, songSetLimit=songSetLimit)


def testAnalizers():
    runAnalizerEvaluations(at=5, songSetLimit=1000)
    runAnalizerEvaluations(at=10, songSetLimit=1000)
    runAnalizerEvaluations(at=5, songSetLimit=2000)
    runAnalizerEvaluations(at=10, songSetLimit=2000)
    runAnalizerEvaluations(at=5, songSetLimit=3000)
    runAnalizerEvaluations(at=10, songSetLimit=3000)
