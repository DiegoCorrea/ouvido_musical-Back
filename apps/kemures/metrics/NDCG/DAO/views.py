from .algorithm import calcUsersNDCG
from .models import NDCG
from apps.kemures.metrics import BenchNDCG
from django.utils import timezone
from apps.kemures.recommenders.UserAverage import UserAverage_Life

import logging
logger = logging.getLogger(__name__)


def runNDCG(at=5):
    logger.info("[Start NDCG Evaluation]")
    startedAt = timezone.now()
    value = calcUsersNDCG(at=at)
    finishedAt = timezone.now()
    ndcgResult = NDCG(
        life=UserAverage_Life.objects.last(),
        value=value,
        at=at
    )
    ndcgResult.save()
    BenchNDCG.objects.create(
        id=ndcgResult,
        started_at=startedAt,
        finished_at=finishedAt
    )
    logger.info(
        "Benchmark: Start at - "
        + str(startedAt)
        + " || Finished at -"
        + str(finishedAt)
    )
    logger.info("[Finish NDCG Evaluation]")
