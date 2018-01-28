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


def testAnalizersEvaluations():
    runAnalizerEvaluations(at=5, songSetLimit=1500)
    runAnalizerEvaluations(at=10, songSetLimit=1500)
    runAnalizerEvaluations(at=5, songSetLimit=3000)
    runAnalizerEvaluations(at=10, songSetLimit=3000)
    runAnalizerEvaluations(at=5, songSetLimit=4500)
    runAnalizerEvaluations(at=10, songSetLimit=4500)
