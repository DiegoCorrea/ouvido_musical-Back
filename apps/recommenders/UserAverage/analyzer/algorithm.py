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
    itemValues = [item.iLike for item in allItens]
    countList = Counter(itemValues)
    logger.debug('User Averange Benchmark -> List len: ' + str(len(countList)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allItens.last().created_at) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('User Average - Score')
    plt.ylabel('Quantidade de usuários')
    plt.xlabel('Nota')
    plt.bar(countList.keys(), countList.values())
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'like_gBar.png')
    plt.close()
    logger.info("[Finish User Average Score (Graph Bar)]")

def recommended_gBar(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Recomended (Graph Bar)]")
    itemValues = [item.song.id for item in allItens]
    countList = Counter(itemValues)
    countListValues = Counter(countList.values())
    logger.debug('User Averange Benchmark -> List len: ' + str(len(countList)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allItens.last().created_at) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('User Average - Score')
    plt.ylabel('Quantidade de usuários')
    plt.xlabel('Nota')
    plt.bar(countListValues.keys(), countListValues.values())
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'recommended_gBar.png')
    plt.close()
    logger.info("[Finish User Average Score (Graph Bar)]")

def score_gBar(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Score (Graph Bar)]")
    itemValues = [evalution.score for evalution in allItens]
    countList = Counter(itemValues)
    logger.debug('User Averange Score -> List len: ' + str(len(countList)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allItens.last().created_at) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('User Average - Score')
    plt.ylabel('Quantidade de usuários')
    plt.xlabel('Nota')
    plt.bar(countList.keys(), countList.values())
    plt.legend(loc='best')
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
def similarity_gBar(allItens = UserAverage_Recommendations.objects.all()):
    logger.info("[Start User Average Similarity (Graph Bar)]")
    itemValues = [float("{0:.3f}".format(item.similarity)) for item in allItens]
    countList = Counter(itemValues)
    logger.debug('User Average Similarity -> List len: ' + str(len(itemValues)))
    directory = str('./files/apps/recommenders/UserAverange/graphs/' + str(connection.settings_dict['NAME']) + '/algorithm/' + str(allItens.last().created_at) + '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.title('User Average - Similarity')
    plt.ylabel('Quantidade de similares')
    plt.xlabel('Similaridade')
    plt.bar(countList.keys(),countList.values())
    plt.legend(loc='best')
    plt.savefig(str(directory) + 'similarity_gBar.png')
    plt.close()
    logger.info("[Finish User Average Similarity (Graph Bar)]")
