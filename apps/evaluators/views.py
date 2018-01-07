from .MAP.algorithm.views import runMAP
from .MRR.algorithm.views import runMRR
from .NDCG.algorithm.views import runNDCG
from .MAP.analyzer.views import runAllMAPAnalizers
from .MRR.analyzer.views import runAllMRRAnalizers
from .NDCG.analyzer.views import runAllNDCGAnalizers

def runEvaluations(limit=5):
    runMAP(limit=limit)
    runMRR(limit=limit)
    runNDCG(limit=limit)

def runAnalizers():
    runAllMAPAnalizers()
    runAllMRRAnalizers()
    runAllNDCGAnalizers()
