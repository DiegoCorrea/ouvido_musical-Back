from .algorithm import UserAverage, UserAverage_Life
from apps.recommenders.UserAverage.benchmark.models import BenchUserAverage
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)

def runUserAverage(songSetLimit):
    logger.info("[Start Run User Average - Benchmark]")
    startedAt = timezone.now()
    UserAverage(songSetLimit=songSetLimit)
    finishedAt = timezone.now()
    bench = BenchUserAverage(life=UserAverage_Life.objects.last(),started_at=startedAt,finished_at=finishedAt)
    bench.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    logger.info("[Start Run User Average] - Benchmark")
