from apps.data.users.models import User
import numpy as np

import logging
logger = logging.getLogger(__name__)


def userLikeArray(recommendations):
    if len(recommendations) == 0:
        return []
    return [rec.iLike for rec in recommendations]


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


def calcUsersMAP(at=5):
    logger.info("[Start User MAP]")
    ap = []
    for user in User.objects.all():
        userec = user.useraverage_recommendations_set.all()[:at]
        if len(userec) == 0:
            continue
        ap.append(getAP(userLikeArray(userec)))
    uMap = np.mean(ap)
    logger.debug("Mean Average Precision@%d: %f", at, uMap)
    logger.debug("Total Users Rated: %d", len(ap))
    logger.info("[Finish User MAP]")
    return uMap
