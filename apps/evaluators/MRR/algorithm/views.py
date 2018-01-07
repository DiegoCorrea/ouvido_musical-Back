from .algorithm import calcUsersMRR
from .models import MRR
from apps.evaluators.MRR.benchmark.models import BenchMRR
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)
# Create your views here.
def runMRR(limit=5):
    logger.info("[Start MRR Evaluation]")
    startAt = timezone.now()
    value = calcUsersMRR(limit=limit)
    bench = BenchMRR(started_at=startAt,finished_at=timezone.now())
    bench.save()
    mrrResult = MRR(value=value, limit=limit)
    mrrResult.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    logger.info("[Finish MRR Evaluation]")
