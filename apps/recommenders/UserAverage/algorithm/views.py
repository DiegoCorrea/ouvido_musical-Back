from .algorithm import UserAverage
from apps.recommenders.UserAverage.benchmark.models import BenchUserAverage
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)

def runUserAverage():
    logger.info("[Start User Average - Benchmark]")
    startAt = timezone.now()
    UserAverage()
    bench = BenchUserAverage(started_at=startAt,finished_at=timezone.now())
    bench.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    logger.info("[Start User Average] - Benchmark")
