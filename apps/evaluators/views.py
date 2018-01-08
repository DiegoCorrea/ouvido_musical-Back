from .MAP.algorithm.views import runMAP
from .MRR.algorithm.views import runMRR
from .NDCG.algorithm.views import runNDCG
from .MAP.analyzer.views import runAllMAPAnalizers
from .MRR.analyzer.views import runAllMRRAnalizers
from .NDCG.analyzer.views import runAllNDCGAnalizers

def runEvaluations(at=5):
    runMAP(at=at)
    runMRR(at=at)
    runNDCG(at=at)
def runAnalizers(at=5):
    runAllMAPAnalizers(at=at)
    runAllMRRAnalizers(at=at)
    runAllNDCGAnalizers(at=at)
