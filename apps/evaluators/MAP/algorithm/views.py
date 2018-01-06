from .algorithm import calcUsersMAP
from apps.evaluators.MAP.algorithm.models import MAP
from apps.evaluators.MAP.benchmark.models import benchMAP
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)
# Create your views here.
def runMAP(limit=5):
    logger.info("[Start MAP Evaluation]")
    startAt = timezone.now()
    value = calcUsersMAP(limit=limit)
    bench = benchMAP(started_at=startAt,finished_at=timezone.now())
    bench.save()
    mapResult = RatingMAP(value=value, limit=limit)
    mapResult.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    logger.info("[Finish MAP Evaluation]")
