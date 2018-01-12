from .algorithm import calcUsersMAP
from .models import MAP
from apps.evaluators.MAP.benchmark.models import BenchMAP
from django.utils import timezone
from apps.recommenders.UserAverage.algorithm.models import UserAverage_Life

import logging
logger = logging.getLogger(__name__)
# Create your views here.
def runMAP(at=5):
    logger.info("[Start MAP Evaluation]")
    startedAt = timezone.now()
    value = calcUsersMAP(at=at)
    finishedAt = timezone.now()
    mapResult = MAP(life=UserAverage_Life.objects.last(), value=value, at=at)
    mapResult.save()
    bench = BenchMAP(id=mapResult, started_at=startedAt,finished_at=finishedAt)
    bench.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    logger.info("[Finish MAP Evaluation]")
