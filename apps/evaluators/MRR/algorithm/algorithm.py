from apps.data.users.models import User
from apps.evaluators.MRR.rating.models import RatingMRR
from apps.evaluators.MRR.benchmark.models import benchMRR
from django.utils import timezone
import numpy as np
import logging

logger = logging.getLogger(__name__)

def userLikeArray(recommendations):
    if len(recommendations) == 0:
        return []
    return [rec.iLike for rec in recommendations]
#####################################################################
# MRR
#
#####################################################################
def getMRR(relevanceArray):
    n_relevances = len(relevanceArray)
    if n_relevances == 0:
        return 0
    for i in range(n_relevances):
        if relevanceArray[i]:
            return 1/(i+1)
    return 0
def calcUsersMRR(limit=5):
    logger.info("[Start User MRR]")
    mrrList = []
    for user in User.objects.all():
        userec = user.usersongrecommendation_set.all()[:limit]
        if (len(userec) == 0): continue
        mrrList.append(getAP(userLikeArray(userec)))
    uMrr = np.mean(mrrList)
    logger.debug("Mean Reciprocal Rank@%d: %f", limit, uMrr)
    logger.debug("Total Users Rated: %d", len(mrrList))
    logger.info("[Finish User MRR]")
    return uMrr
def runMRR(limit=5):
    logger.info("[Start MRR Evaluation]")
    startAt = timezone.now()
    value = calcUsersMRR(limit=limit)
    bench = benchMRR(started_at=startAt,finished_at=timezone.now())
    bench.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    mrrResult = MRR(value=value, limit=limit)
    mrrResult.save()
    logger.info("[Finish MRR Evaluation]")
