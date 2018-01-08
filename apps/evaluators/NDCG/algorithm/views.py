from .algorithm import calcUsersNDCG
from apps.evaluators.NDCG.algorithm.models import NDCG
from apps.evaluators.NDCG.benchmark.models import BenchNDCG
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)
# Create your views here.
def runNDCG(at=5):
    logger.info("[Start NDCG Evaluation]")
    startAt = timezone.now()
    value = calcUsersNDCG(limit=at)
    bench = BenchNDCG(started_at=startAt,finished_at=timezone.now())
    bench.save()
    ndcgResult = NDCG(value=value,limit=at)
    ndcgResult.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    logger.info("[Finish NDCG Evaluation]")
