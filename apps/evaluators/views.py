from .MAP.algorithm.views import runMAP
from .MRR.algorithm.views import runMRR
from .NDCG.algorithm.views import runNDCG
from .MAP.analyzer.views import runAllMAPAnalizers
from .MRR.analyzer.views import runAllMRRAnalizers
from .NDCG.analyzer.views import runAllNDCGAnalizers

from .MRR.analyzer.algorithm import report_MRR_results
from .MRR.analyzer.benchmark import report_MRR_time
from .MAP.analyzer.algorithm import report_MAP_results
from .MAP.analyzer.benchmark import report_MAP_time
from .NDCG.analyzer.algorithm import report_NDCG_results
from .NDCG.analyzer.benchmark import report_NDCG_time


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


def csvResults():
    report_MAP_results()
    report_MAP_time()
    report_MRR_results()
    report_MRR_time()
    report_NDCG_results()
    report_NDCG_time()
