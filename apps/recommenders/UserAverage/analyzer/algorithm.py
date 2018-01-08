import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
from apps.recommenders.UserAverage.algorithm.models import UserAverage_Recommendations
from django.db import connection
import logging

logger = logging.getLogger(__name__)
def like_gBar(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Recomended (Graph Bar)]")
    countList = Counter([item.iLike for item in allItens])
    logger.debug('User Averange Benchmark -> List len: ' + str(len(countList)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allItens.last().created_at) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('User Average - Gostou')
    plt.ylabel('Quantidade de votos')
    plt.xlabel('Gostou')
    plt.bar([str(item) for item in countList.keys()], countList.values())
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'like_gBar.png')
    plt.close()
    logger.info("[Finish User Average Score (Graph Bar)]")

def recommended_gBar(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Recomended (Graph Bar)]")
    countList = Counter([item.song.id for item in allItens])
    countListValues = Counter(countList.values())
    logger.debug('User Averange Benchmark -> List len: ' + str(len(countList)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allItens.last().created_at) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('User Average - Score')
    plt.ylabel('Quantidade de músicas')
    plt.xlabel('Vezes recomendada')
    plt.bar(countListValues.values(), countListValues.keys())
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'recommended_gBar.png')
    plt.close()
    logger.info("[Finish User Average Score (Graph Bar)]")

def score_gBar(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Score (Graph Bar)]")
    countList = Counter([evalution.score for evalution in allItens])
    logger.debug('User Averange Score -> List len: ' + str(len(countList)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allItens.last().created_at) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('User Average - Score')
    plt.ylabel('Quantidade de músicas')
    plt.xlabel('Nota')
    plt.bar(countList.keys(), countList.values())
    plt.savefig(str(directory) + 'score_gBar.png')
    plt.close()
    logger.info("[Finish User Average Score (Graph Bar)]")

def similarity_gScatter(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Similarity (Graph Scatter)]")
    itemValues = [ item.similarity for item in allItens]
    itemMeanValues = np.mean(itemValues)
    logger.debug('User Average Similarity -> Mean: ' + str(len(itemValues)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allItens.last().created_at) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('User Average - Similarity')
    plt.ylabel('Similaridade')
    plt.xlabel('Similaridade')
    plt.scatter(itemValues, itemValues, label='Media: ' + str(float("{0:.3f}".format(itemMeanValues))))
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'similarity_gScatter.png')
    plt.close()
    logger.info("[Finish User Average Similarity (Graph Scatter)]")
    
def similarity_gLine(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Similarity (Graph Line)]")
    itemValues = [float("{0:.3f}".format(item.similarity)) for item in allItens]
    countList = Counter(sorted(itemValues))
    logger.debug('User Average Similarity -> List len: ' + str(len(itemValues)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allItens.last().created_at) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('User Average - Similarity')
    plt.ylabel('Quantidade de similares')
    plt.xlabel('Similaridade')
    plt.plot(countList.keys(),countList.values())
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'similarity_gBar.png')
    plt.close()
    logger.info("[Finish User Average Similarity (Graph Line)]")
