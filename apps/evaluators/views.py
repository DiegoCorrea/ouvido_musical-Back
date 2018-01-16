from .MAP.algorithm.views import runMAP
from .MRR.algorithm.views import runMRR
from .NDCG.algorithm.views import runNDCG
from .MAP.analyzer.views import runAllMAPAnalizers
from .MRR.analyzer.views import runAllMRRAnalizers
from .NDCG.analyzer.views import runAllNDCGAnalizers

def runEvaluations(at=5,songSetLimit):
    runMAP(at=at)
    #runAllMAPAnalizers(at=at,songSetLimit=songSetLimit)
    runMRR(at=at)
    #runAllMRRAnalizers(at=at,songSetLimit=songSetLimit)
    runNDCG(at=at)
    #runAllNDCGAnalizers(at=at,songSetLimit=songSetLimit)
