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
    itemValues = []
    for item in allItens:
        itemValues.append(item.iLike)
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
    itemValues = []
    for item in allItens:
        itemValues.append(item.song.id)
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
    logger.debug('User Averange Benchmark -> List: ' + str(len(countList)))
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
