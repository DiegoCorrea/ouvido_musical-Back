from .MAP.algorithm.main import runMAP
from .MRR.algorithm.main import runMRR
from .NDCG.algorithm.main import runNDCG

def runEvaluation(limit=5):
    runMAP(limit=limit)
    runMRR(limit=limit)
    runNDCG(limit=limit)
