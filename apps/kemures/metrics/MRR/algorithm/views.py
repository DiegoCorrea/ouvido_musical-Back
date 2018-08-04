from .algorithm import calcUsersMRR
from .models import MRR
from apps.kemures.metrics.MRR.runtime.models import BenchMRR
from django.utils import timezone
from apps.kemures.recommenders.UserAverage import UserAverage_Life

import logging
logger = logging.getLogger(__name__)


def runMRR(at=5):
    logger.info("[Start MRR Evaluation]")
    startedAt = timezone.now()
    value = calcUsersMRR(at=at)
    finishedAt = timezone.now()
    mrrResult = MRR(
        life=UserAverage_Life.objects.last(),
        value=value,
        at=at
    )
    mrrResult.save()
    BenchMRR.objects.create(
        id=mrrResult,
        started_at=startedAt,
        finished_at=finishedAt
    )
    logger.info(
        "Benchmark: Start at - "
        + str(startedAt)
        + " || Finished at -"
        + str(finishedAt)
    )
    logger.info("[Finish MRR Evaluation]")
