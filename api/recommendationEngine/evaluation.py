from api.users.models import User
from api.userSongRecommendation.models import UserSongRecommendation

import numpy as np

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
