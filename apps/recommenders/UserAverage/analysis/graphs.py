import matplotlib.pyplot as plt
import pandas
import numpy as np
from collections import Counter

from apps.data.userPlaySong.models import UserPlaySong
from apps.data.songs.models import SongSimilarity
from apps.recommenders.UserAverage.algorithm.models import UserAverage_Recommendations

def playCountBoxPlot():
    heard = {'Ouvidas': [ups.play_count for ups in UserPlaySong.objects.all()]}
    df = pandas.DataFrame(data=heard)
    plt.figure()
    plt.title('Quantidade de vezes que a música foi ouvida')
    df.boxplot(column='Ouvidas', meanline=True, showmeans=True)
    plt.savefig('./api/analysis/playCountBoxPlot.png')

def titleSimilarityScatter():
    songSimi = [songSimi.similarity for songSimi in SongSimilarity.objects.all()]
    songSimi.sort()
    simiMean = np.mean(songSimi)
    simiMedian = np.median(songSimi)
    plt.figure()
    plt.title('Similaridade entre as músicas')
    plt.text(-0.1, 1, r'Media: ' + str(simiMean))
    plt.text(-0.1, .8, r'Mediana: ' + str(simiMedian))
    plt.grid(True)
    plt.ylabel('Similaridade')
    plt.xlabel('Similaridade')
    plt.scatter(songSimi, songSimi)
    plt.axis([-0.2, 1.2, -0.2, 1.2])
    plt.savefig('./api/analysis/titleSimilarityScatter.png')

def ndcgBar():
    avaliations = [rec.score for rec in UserAverage_Recommendations.objects.all()]
    z = Counter(avaliations)
    plt.figure()
    plt.xlabel('Nota')
    plt.ylabel('Avaliações')
    plt.title('NDCG - Quantidade de avaliações por nota')
    plt.bar([0,1,2,3],[z[0],z[1],z[2],z[3]])
    plt.savefig('./api/analysis/ndcgBar.png')
