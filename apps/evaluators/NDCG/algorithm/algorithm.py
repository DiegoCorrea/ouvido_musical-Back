from apps.data.users.models import User
import numpy as np

import logging
logger = logging.getLogger(__name__)


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


def calcUsersNDCG(at=5):
    logger.info("[Start Users NDCG]")
    result = [
        ndcg_at_k(
            userScoreList(user.useraverage_recommendations_set.all(
            ).order_by("-similarity")),
            k=at,
            method=0
        ) for user in User.objects.all()
    ]
    uNDCG = np.mean(result)
    logger.debug("Normalized Cumulative Gain@%d: %f", at, uNDCG)
    logger.debug("Total Users Rated: %d", len(result))
    logger.info("[Finish Users NDCG]")
    return uNDCG


def userScoreList(recommendations):
    if len(recommendations) == 0:
        return []
    return [rec.score for rec in recommendations]
