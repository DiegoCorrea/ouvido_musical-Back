from api.users.models import User
from api.userSongRecommendation.models import UserSongRecommendation

import numpy as np
from math import log

#####################################################################
# MAP
# Mean Averange Precision
#
#####################################################################
# <Params>
# songRec é a lista de musicas recomendadas para um usuario
# DEBUG 1 os prints internos da função serão imprimidos na tela
# DEBUG 0 os prints internos da função não serão imprimidos
# </Params>
def getUserAP(songRec, DEBUG=1):
    hitList = []
    relevant = 0
    countDoc = 0
    for rec in songRec:
        countDoc += 1
        if (rec.iLike):
            relevant += 1
            hitList.append(relevant/countDoc)
    ap = sum(hitList)
    if (ap > 0):
        # <DEBUG>
        if (DEBUG != 0):
            print ('\t++ User MAP: ', sum(hitList)/relevant) # </DEBUG>
        return sum(hitList)/relevant
    else:
        # <DEBUG>
        if (DEBUG != 0):
            print ('\t++ User MAP:  0') # </DEBUG>
        return 0
# <Params>
# range é o numero referente a quantas posições quer se calcular o MAP
# range padrão é 5
# DEBUG 1 os prints internos da função serão imprimidos na tela
# DEBUG 0 os prints internos da função não serão imprimidos
# </Params>
def calcUsersMAP(range=5, DEBUG=1):
    # <DEBUG>
    if (DEBUG != 0):
        print ('\nMAP com range de ', range) # </DEBUG>
    ap = [getUserAP(user.usersongrecommendation_set.all()[:range], DEBUG=DEBUG) for user in User.objects.all()]
    # <DEBUG>
    if (DEBUG != 0):
        print ('\n\tMean Averange Precision: ', np.mean(ap))
        print ('\t++ Averange Precision dos usuarios: ', ap)
        print ('\t++ Total de usuarios: ', len(User.objects.all())) # </DEBUG>
    return np.mean(ap)

#####################################################################
# MRR
#
#####################################################################
# <Params>calcUsersMRR
# songRec é a lista de musicas recomendadas para um usuario
# DEBUG 1 os prints internos da função serão imprimidos na tela
# DEBUG 0 os prints internos da função não serão imprimidos
# </Params>
def getUserMRR(songRec, DEBUG=1):
    countDoc = 0
    for rec in songRec:
        countDoc += 1
        if (rec.iLike):
            # <DEBUG>
            if (DEBUG != 0):
                print ('\t++ MRR do usuario é: ', 1/countDoc) # </DEBUG>
            return 1/countDoc
    # <DEBUG>
    if (DEBUG != 0):
        print ('\t++ MRR do usuario é:  0') # </DEBUG>
    return 0
# <Params>
# range é o numero referente a quantas posições quer se calcular o MRR
# range padrão é 5
# </Params>
def calcUsersMRR(range=5, DEBUG=1):
    # <DEBUG>
    if (DEBUG != 0):
        print ('\nMRR com range de ', range) # </DEBUG>
    mrrList = [getUserMRR(user.usersongrecommendation_set.all()[:range], DEBUG=DEBUG) for user in User.objects.all()]
    # <DEBUG>
    if (DEBUG != 0):
        print ('\n\tMean Reciprocal Rank: ', np.mean(mrrList))
        print ('\t++ Lista de MRR dos usuarios: ', mrrList)
        print ('\t++ Total de usuarios: ', len(User.objects.all())) # </DEBUG>
    return np.mean(mrrList)
#####################################################################
#
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

def calcUsersNDCG(DEBUG=1, range=5):
    result = [ndcg_at_k(userScoreList(user.usersongrecommendation_set.all()),k=range, method=0) for user in User.objects.all()]
    return result

def userScoreList(recommendations):
    if len(recommendations) == 0:
        return 0.
    return [rec.score for rec in recommendations]
