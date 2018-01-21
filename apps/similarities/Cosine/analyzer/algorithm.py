import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import os
from django.utils import timezone
from apps.data.songs.models import SongSimilarity
from multiprocessing.dummy import Pool as ThreadPool
from apps.CONSTANTS import MAX_THREAD
import logging

logger = logging.getLogger(__name__)


def toFloat(item):
    return float("{0:.3f}".format(item.similarity))


def similarity_gScatter(songSetLimit=SongSimilarity.objects.count()):
    allItens = SongSimilarity.objects.all()
    logger.info("[Start Cosine Similarity (Graph Scatter)]")
    pool = ThreadPool(MAX_THREAD)
    itemValues = pool.map(toFloat, allItens)
    pool.close()
    pool.join()
    itemMeanValues = np.mean(itemValues)
    directory = str(
                    './files/apps/similarities/Cosine/graphs/'
                    + str(songSetLimit)
                    + '/algorithm/'
                    + str(timezone.now())
                    + '/'
                    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('Cosine Similarity')
    plt.ylabel('Similaridade')
    plt.xlabel('Similaridade')
    plt.scatter(
                itemValues,
                itemValues,
                label='Media: '
                + str(float("{0:.3f}".format(itemMeanValues)))
                )
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'similarity_gScatter.png')
    plt.close()
    logger.info("[Finish Cosine Similarity (Graph Scatter)]")


def similarity_gLine(songSetLimit=SongSimilarity.objects.count()):
    allItens = SongSimilarity.objects.all()
    logger.info("[Start Cosine Similarity (Graph Line)]")
    pool = ThreadPool(MAX_THREAD)
    itemValues = pool.map(toFloat, allItens)
    pool.close()
    pool.join()
    countList = Counter(sorted(itemValues))
    itemMeanValues = np.mean(itemValues)
    directory = str(
                    './files/apps/similarities/Cosine/graphs/'
                    + str(songSetLimit)
                    + '/algorithm/'
                    + str(timezone.now())
                    + '/'
                    )
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.figure()
    plt.grid(True)
    plt.title('Cosine Similarity')
    plt.ylabel('Quantidade de similares')
    plt.xlabel('Similaridade')
    plt.plot(countList.keys(), countList.values())
    plt.scatter(
                itemValues,
                itemValues,
                label='Media: '
                + str(float("{0:.3f}".format(itemMeanValues)))
                )
    plt.legend(loc='upper left')
    plt.savefig(str(directory) + 'similarity_gLine.png')
    plt.close()
    logger.info("[Finish Cosine Similarity (Graph Line)]")
