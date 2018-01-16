from apps.data.users.models import User
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
def calcUsersMRR(at=5):
    logger.info("[Start User MRR]")
    mrrList = []
    for user in User.objects.all():
        userec = user.useraverage_recommendations_set.all()[:at]
        if (len(userec) == 0): continue
        mrrList.append(getMRR(userLikeArray(userec)))
    uMrr = np.mean(mrrList)
    logger.debug("Mean Reciprocal Rank@%d: %f", at, uMrr)
    logger.debug("Total Users Rated: %d", len(mrrList))
    logger.info("[Finish User MRR]")
    return uMrr
