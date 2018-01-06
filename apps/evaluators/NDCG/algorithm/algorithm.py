from apps.data.users.models import User
from apps.evaluators.NDCG.rating.models import RatingNDCG
from apps.evaluators.NDCG.benchmark.models import benchNDCG
from django.utils import timezone
import numpy as np
import logging

logger = logging.getLogger(__name__)

def userLikeArray(recommendations):
    if len(recommendations) == 0:
        return []
    return [rec.iLike for rec in recommendations]
#####################################################################
# NDCG
#
#####################################################################
""" Reference from https://gist.github.com/bwhite/3726239
"""
def dcg_at_k(r, k, method=0):
    r = np.asfarray(r)[:k]
    if r.size:
        if method == 0:
            return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
        elif method == 1:
            return np.sum(r / np.log2(np.arange(2, r.size + 2)))
        else:
            raise ValueError('method must be 0 or 1.')
    return 0.
def ndcg_at_k(r, k, method=0):
    dcg_max = dcg_at_k(sorted(r, reverse=True), k, method)
    if not dcg_max:
        return 0.
    return dcg_at_k(r, k, method) / dcg_max
def calcUsersNDCG(limit=5):
    logger.info("[Start Users NDCG]")
    result = [ndcg_at_k(userScoreList(user.usersongrecommendation_set.all()),k=limit, method=0) for user in User.objects.all()]
    uNDCG = np.mean(result)
    logger.debug("Normalized Cumulative Gain@%d: %f", limit, uNDCG)
    logger.debug("Total Users Rated: %d", len(result))
    logger.info("[Finish Users NDCG]")
    return uNDCG
def userScoreList(recommendations):
    if len(recommendations) == 0:
        return []
    return [rec.score for rec in recommendations]
def runNDCG(limit=5):
    logger.info("[Start NDCG Evaluation]")
    startAt = timezone.now()
    value = calcUsersNDCG(limit=limit)
    bench = benchNDCG(started_at=startAt,finished_at=timezone.now())
    bench.save()
    logger.info("Benchmark: Start at - " + str(bench.started_at) + " || Finished at -" + str(bench.finished_at))
    ndcgResult = NDCG(value=value,limit=limit)
    ndcgResult.save()
    logger.info("[Finish NDCG Evaluation]")
