from api.users.models import User

import numpy as np

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

def calcUsersMAP(range=5, DEBUG=0):
    ap = []
    for user in User.objects.all():
        userec = user.usersongrecommendation_set.all()[:range]
        if (len(userec) == 0): continue
        ap.append(getAP(userLikeArray(userec)))
    # <DEBUG>
    if (DEBUG != 0):
        print ('\n\tMean Averange Precision: ', np.mean(ap))
        print ('\t++ Total de usuarios: ', len(User.objects.all()))
        print ('\t++ Total de usuarios avaliados no MAP: ', len(ap)) # </DEBUG>
    return np.mean(ap)

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

def calcUsersMRR(range=5, DEBUG=0):
    mrrList = []
    for user in User.objects.all():
        userec = user.usersongrecommendation_set.all()[:range]
        if (len(userec) == 0): continue
        mrrList.append(getAP(userLikeArray(userec)))
    # <DEBUG>
    if (DEBUG != 0):
        print ('\n\tMRR Reciprocal Rank: ', np.mean(mrrList))
        print ('\t++ Total de usuarios: ', len(User.objects.all()))
        print ('\t++ Total de usuarios avaliados no MRR: ', len(mrrList)) # </DEBUG>
    return np.mean(mrrList)

#####################################################################
# NDCG
#
#####################################################################
""" Reference from https://gist.github.com/bwhite/3726239
"""
def dcg_at_k(r, k, method=0):
    """Score is discounted cumulative gain (dcg)
    Relevance is positive real values.  Can use binary
    as the previous methods.
    Example from
    http://www.stanford.edu/class/cs276/handouts/EvaluationNew-handout-6-per.pdf
    >>> r = [3, 2, 3, 0, 0, 1, 2, 2, 3, 0]
    >>> dcg_at_k(r, 1)
    3.0
    >>> dcg_at_k(r, 1, method=1)
    3.0
    >>> dcg_at_k(r, 2)
    5.0
    >>> dcg_at_k(r, 2, method=1)
    4.2618595071429155
    >>> dcg_at_k(r, 10)
    9.6051177391888114
    >>> dcg_at_k(r, 11)
    9.6051177391888114
    Args:
        r: Relevance scores (list or numpy) in rank order
            (first element is the first item)
        k: Number of results to consider
        method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
                If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
    Returns:
        Discounted cumulative gain
    """
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
    """Score is normalized discounted cumulative gain (ndcg)
    Relevance is positive real values.  Can use binary
    as the previous methods.
    Example from
    http://www.stanford.edu/class/cs276/handouts/EvaluationNew-handout-6-per.pdf
    >>> r = [3, 2, 3, 0, 0, 1, 2, 2, 3, 0]
    >>> ndcg_at_k(r, 1)
    1.0
    >>> r = [2, 1, 2, 0]
    >>> ndcg_at_k(r, 4)
    0.9203032077642922
    >>> ndcg_at_k(r, 4, method=1)
    0.96519546960144276
    >>> ndcg_at_k([0], 1)
    0.0
    >>> ndcg_at_k([1], 2)
    1.0
    Args:
        r: Relevance scores (list or numpy) in rank order
            (first element is the first item)
        k: Number of results to consider
        method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
                If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
    Returns:
        Normalized discounted cumulative gain
    """
    dcg_max = dcg_at_k(sorted(r, reverse=True), k, method)
    if not dcg_max:
        return 0.
    return dcg_at_k(r, k, method) / dcg_max

def calcUsersNDCG(DEBUG=0, range=5):
    # <DEBUG>
    if (DEBUG != 0):
        print ('\nNDCG com range de ', range) # </DEBUG>
    result = [ndcg_at_k(userScoreList(user.usersongrecommendation_set.all()),k=range, method=0) for user in User.objects.all()]
    # <DEBUG>
    if (DEBUG != 0):
        print ('\n\tNDCG: ', np.mean(result))
        print ('\t++ Total de usuarios: ', len(User.objects.all())) # </DEBUG>
    return np.mean(result)

def userScoreList(recommendations):
    if len(recommendations) == 0:
        return []
    return [rec.score for rec in recommendations]
