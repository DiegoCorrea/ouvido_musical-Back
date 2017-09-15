from math import sqrt
from recommendations.models import Song
from recommendations.models import User
from recommendations.models import UserPlaySong
from recommendations.models import UserSongRecommendation
from recommendations.models import ItemSimilarity

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

def getItemSimilarityTable():
    itens = {}
    for line in ItemSimilarity.objects.all():
        itens.setdefault(line, {})
        itens[line].setdefault(line.songCompare, int(line.similarity))
    return itens
####################################################################
# A partir de um usuario base
# Pega o valor da similaridade desse usuario com todos os outros
def getSimilarity(evaluationTable, userBase):
    similarity = [(euclideanDistance(evaluationTable, userBase, userCompare), userCompare)
                    for userCompare in evaluationTable if userCompare != userBase]
    similarity.sort()
    similarity.reverse()
    return similarity

def calcSimilarityTable(itemTable):
    similarityTable = {}
    for item in itemTable:
        scores = getSimilarity(itemTable, item)
        similarityTable[item] = scores
    return similarityTable
#####################################################################
def getItemRecommendations(userItens, itensSimilarity):
    scores = {}
    totalSimilarity = {}
    rankings = []
    for (item, score) in userItens.items():
        for(similarity, unassistedItem) in itensSimilarity[item]:
            if unassistedItem in userItens: continue

            scores.setdefault(unassistedItem, 0)
            scores[unassistedItem] += similarity * score
            totalSimilarity.setdefault(unassistedItem, 0)
            totalSimilarity[unassistedItem] += similarity
    #for (item, score) in scores.items():
    #    if totalSimilarity[item] != 0:
    #        rankings = [(score/totalSimilarity[item], item)]
    #    else:
    #        rankings = [0, item]
    rankings = [(score/totalSimilarity[item], item) for item, score in scores.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
#####################################################

print ("1 -> Carregando tabela de usuarios\n")
userTable = getUserTable()
print ("ok... Tabela de usuarios carregada\n")

print ("2 -> Carregando tabela de Itens\n")
itemTable = getItemTable(userTable)
print ("ok... Tabela de itens carregada\n")

print ("3 -> Calculando similaridade entre os itens\n")
similarityTable = calcSimilarityTable(itemTable)
print ("ok... Tabela de Similaridade entre os itens\n")

print ("4 -> Salvando o similaridade entre os itens no Banco\n")
for itemBase in similarityTable:
    for itemCompare in similarityTable[itemBase]:
        itemSimilar = ItemSimilarity()
        itemSimilar.songCompare = itemCompare[1]
        itemSimilar.similarity = itemCompare[0]
        itemSimilar.songBase_id = itemBase[1]
        itemSimilar.save()
print ("ok... Tabela de Similaridade Calculada\n")

print ("5 -> Calculando similaridade entre os usuarios e os itens\n")
for user in User.objects.all():
    #print ("user.user", user.user)
    for item in getItemRecommendations(userTable[user.user], similarityTable):
        if item:
            #print ("song_id", item[1])
            #print ("probabilit_play_count", item[0])
            recommendation = UserSongRecommendation()
            recommendation.song_id = item[1]
            recommendation.user_id = user.user
            recommendation.probabilit_play_count = item[0]
            recommendation.save()
print ("ok... Tabela de Recomendacoes Atualizada\n")
print ("Encerrando Script! Bye bye...\n")
