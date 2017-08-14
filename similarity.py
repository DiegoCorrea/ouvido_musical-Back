from math import sqrt
from recommendations.models import Song
from recommendations.models import User
from recommendations.models import UserPlaySong
from recommendations.models import UserSongRecommendation

####################################################################
# Distancia Euclidiana
# raizDa(soma-De-1-Ate-N((usuarioBase - usuarioComparacao)aoQuadrado))
def euclideanDistance(evaluationTable, userBase, userCompare):
    si = {}

    for item in evaluationTable[userBase]:
        if item in evaluationTable[userCompare]: si[item] = 1

    if len(si) == 0: return 0

    distance = sum([pow(evaluationTable[userBase][item] - evaluationTable[userCompare][item], 2)
                for item in evaluationTable[userBase] if item in evaluationTable[userCompare]])

    return 1/(1 + sqrt(distance))

####################################################################
def getUserTable():
    itens = {}
    for line in Song.objects.all():
        itens[line.song] = line.song
    userBase = {}
    for line in UserPlaySong.objects.all():
        userBase.setdefault(line.user_id, {})
        userBase[line.user_id][itens[line.song_id]] = int(line.play_count)
    return userBase

def getItemTable(userTable):
    userTableTransposed = {}

    for user in userTable:
        for item in userTable[user]:
            userTableTransposed.setdefault(item, {})
            userTableTransposed[item].setdefault(user, userTable[user][item])

    return userTableTransposed

####################################################################
# A partir de um usuario base
# Pega o valor da similaridade desse usuario com todos os outros
def getSimilarity(evaluationTable, userBase, limit=30):
    similarity = [(euclideanDistance(evaluationTable, userBase, userCompare), userCompare)
                    for userCompare in evaluationTable if userCompare != userBase]

    similarity.sort()
    similarity.reverse()

    return similarity[0:limit]

def calcSimilarityTable(itemTable):
    similarityTable = {}

    for item in itemTable:
        scores = getSimilarity(itemTable, item)
        similarityTable[item] = scores

    return similarityTable
#####################################################################
def getItemRecommendations(evaluationTable, itensSimilarity, userBase, limit=30):
    userItens = evaluationTable[userBase]
    scores = {}
    totalSimilarity = {}
    for (item, score) in userItens.items():
        for(similarity, unassistedItem) in itensSimilarity[item]:
            if unassistedItem in userItens: continue
            scores.setdefault(unassistedItem, 0)
            scores[unassistedItem] += similarity * score
            totalSimilarity.setdefault(unassistedItem, 0)
            totalSimilarity[unassistedItem] += similarity
    rankings = [(score/totalSimilarity[item], item) for item, score in scores.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:limit]
#####################################################

userTable = getUserTable()
print ("ok... Tabela de usuarios carregada\n")
itemTable = getItemTable(userTable)
print ("ok... Tabela de itens carregada\n")
similarityTable = calcSimilarityTable(itemTable)
print ("ok... Tabela de Similaridade Calculada\n")

for user in User.objects.all():
    for item in getItemRecommendations(userTable, similarityTable, user.user):
        recommendation = UserSongRecommendation()
        recommendation.song_id = item[1]
        recommendation.user_id = user.user
        recommendation.probabilit_play_count = item[0]
        recommendation.save()
print ("ok... Tabela de Recomendações Atualizada\n")
