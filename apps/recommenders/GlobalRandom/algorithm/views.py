from .algorithm import GlobalRandom
from apps.recommenders.GlobalRandom.benchmark.models import BenchGlobalRandom
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)

def runGlobalRandom():
    logger.info("[Start Global Random] - Benchmark")
    startAt = timezone.now()
    GlobalRandom()
    bench = BenchGlobalRandom(started_at=startAt,finished_at=timezone.now())
    bench.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    logger.info("[Start Global Random] - Benchmark")
