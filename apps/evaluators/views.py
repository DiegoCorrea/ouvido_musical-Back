from .MAP.algorithm.views import runMAP
from .MRR.algorithm.views import runMRR
from .NDCG.algorithm.views import runNDCG

def runEvaluation(limit=5):
    runMAP(limit=limit)
    runMRR(limit=limit)
    runNDCG(limit=limit)
