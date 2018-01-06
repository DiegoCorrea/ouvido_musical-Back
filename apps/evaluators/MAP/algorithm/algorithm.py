from apps.data.users.models import User
from apps.evaluators.MAP.rating.models import RatingMAP
from apps.evaluators.MAP.benchmark.models import benchMAP
from django.utils import timezone
import numpy as np
import logging

logger = logging.getLogger(__name__)

def userLikeArray(recommendations):
    if len(recommendations) == 0:
        return []
    return [rec.iLike for rec in recommendations]
#####################################################################
# MAP
# Mean Averange Precision
#
#####################################################################
def getAP(relevanceArray):
    n_relevances = len(relevanceArray)
    if n_relevances == 0:
        return 0
    hitList = []
    relevant = 0
    for i in range(n_relevances):
        if relevanceArray[i]:
            relevant += 1
            hitList.append(relevant/(i+1))
    ap = sum(hitList)
    if (ap > 0):
        return sum(hitList)/relevant
    else:
        return 0
def calcUsersMAP(limit=5):
    logger.info("[Start User MAP]")
    ap = []
    for user in User.objects.all():
        userec = user.usersongrecommendation_set.all()[:limit]
        if (len(userec) == 0): continue
        ap.append(getAP(userLikeArray(userec)))
    uMap = np.mean(ap)
    logger.debug("Mean Average Precision@%d: %f", limit, uMap)
    logger.debug("Total Users Rated: %d", len(ap))
    logger.info("[Finish User MAP]")
    return uMap
def runMAP(limit=5):
    logger.info("[Start MAP Evaluation]")
    startAt = timezone.now()
    value = calcUsersMAP(limit=limit)
    bench = benchMAP(started_at=startAt,finished_at=timezone.now())
    bench.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    mapResult = RatingMAP(value=value, limit=limit)
    mapResult.save()
    logger.info("[Finish MAP Evaluation]")
